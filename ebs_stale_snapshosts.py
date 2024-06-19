import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Get current timestamp
    current_time = datetime.utcnow()

    # Get all EBS snapshots
    response = ec2.describe_snapshots(OwnerIds=['self'])

    # Get all active EC2 instance IDs
    active_instance_ids = set()
    instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for reservation in instances_response['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])

    # Iterate through each snapshot
    for snapshot in response['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')
        snapshot_time = snapshot['StartTime'].replace(tzinfo=None)
        age = current_time - snapshot_time

        # Print snapshot details including creation time
        print(f"Snapshot ID: {snapshot_id}, Creation Time: {snapshot_time}, Age: {age}")

        # Check if the snapshot is older than 30 days
        if age > timedelta(days=30):
            print(f"Snapshot {snapshot_id} is older than 30 days ({age.days} days).")

        # Check if the snapshot should be deleted
        if not volume_id or (volume_id and volume_id not in active_instance_ids):
            try:
                # Delete the snapshot if it's not attached to any volume or the volume is not attached to a running instance
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                if not volume_id:
                    print(f"Deleted EBS snapshot {snapshot_id} as it was not attached to any volume.")
                else:
                    print(f"Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any running instance.")
            except ec2.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'InvalidSnapshot.NotFound':
                    print(f"Snapshot {snapshot_id} does not exist.")
                else:
                    print(f"Error deleting snapshot {snapshot_id}: {e}")
        else:
            print(f"Keeping snapshot {snapshot_id} as it's associated with an active volume.")

