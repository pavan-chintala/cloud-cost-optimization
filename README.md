**AWS Cloud Cost Optimization 🌟 - Identifying Stale EBS Snapshots 📸**

**Overview 🚀**

In cloud environments like AWS, managing storage costs effectively is crucial. One area often overlooked is the management of EBS snapshots. These snapshots, while essential for backup and recovery, can accumulate over time, leading to unnecessary costs if not managed properly. This project aims to automate the identification and deletion of stale EBS snapshots, thereby optimizing storage costs without compromising data integrity.

**Lambda Function Purpose 🎯**

The Lambda function developed here fetches all EBS snapshots owned by the AWS account ('self') and retrieves a list of active EC2 instances (both running and stopped). It evaluates each snapshot to determine if its associated volume is no longer attached to any active instance. If a snapshot is found to be stale (not associated with any active instance), the Lambda function deletes it. Additionally, it identifies snapshots that haven't been used in a configurable period (e.g., 3 or 6 months) and deletes them to further optimize costs.

**Benefits 🌈**

- **Cost Savings**: By automating the deletion of stale snapshots, unnecessary storage costs are minimized.
- **Efficiency**: The function ensures that only actively used snapshots are retained, maintaining a lean and cost-effective infrastructure.
- **Automation**: Once deployed, the Lambda function runs periodically, reducing manual intervention and ensuring ongoing cost optimization.

**Implementation Details 🛠️**

- **Technologies Used**: Python 3, AWS Lambda, Boto3 (AWS SDK for Python), AWS APIs.
- **Snapshot Evaluation Criteria**:
    Snapshots not associated with any active EC2 instance.
    Snapshots that haven't been used for a specified period (e.g., 3 or 6 months).
- **Error Handling**: The function includes robust error handling to manage any exceptions encountered during snapshot deletion operations.
- **Logging**: Detailed logging is implemented to provide visibility into snapshot evaluation and deletion activities.

**Example Use Case 📝**

Imagine a scenario where an EC2 instance named "test instance 1" was launched for testing purposes. After terminating the instance, the associated EBS volume was deleted automatically, but the snapshot created for backup purposes remained. Without this automated cleanup, such snapshots could accrue storage costs over time.

**Usage Instructions 📋**
1. **Deploy the Lambda Function:**
   Copy the Python code provided into an AWS Lambda function configured to run on a schedule (e.g., daily or weekly).

2. **Set Permissions:**
Ensure the Lambda function has appropriate IAM permissions to describe and delete EC2 snapshots (ec2:DescribeSnapshots, ec2:DeleteSnapshot, etc.).

3.**Configure Schedule:** 
Schedule the Lambda function to run at intervals that suit your operational needs and cost optimization goals.

4. **Monitor Execution:**
Monitor CloudWatch Logs for insights into snapshot evaluation and deletion activities. Set up alerts to notify of any unexpected issues.

**Conclusion 🌟** 

Managing AWS resources efficiently is essential for controlling costs and maintaining a streamlined infrastructure. By automating the identification and deletion of stale EBS snapshots, this project contributes to a more cost-effective cloud environment while ensuring that backup and recovery capabilities remain intact.
