AWS Documentation from https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-aws-infrastructure-operations-by-using-amazon-bedrock.html:

# Automate AWS infrastructure operations by using Amazon Bedrock

*Ishwar Chauthaiwale and Anand Bukkapatnam Tirumala, Amazon Web Services*

## Summary

In cloud native solutions, automating common infrastructure operations play a vital role in maintaining efficient, secure, and cost-effective environments. Manually handling operations is time-consuming and prone to human error. Additionally, team members with varying levels of AWS expertise need to perform these tasks while ensuring compliance with security protocols. This pattern demonstrates how to use Amazon Bedrock to automate common AWS infrastructure operations through natural language processing (NLP).

This pattern can help organizations to develop reusable, modular, and secure code for deploying generative AI-based infrastructure across multiple environments. Through its focus on infrastructure as code (IaC) and automation, it delivers key DevOps benefits including version control, consistent deployments, reduced errors, faster provisioning, and improved collaboration.

The pattern implements a secure architecture that enables teams to manage operations related to key AWS services including:

* Amazon Simple Storage Service (Amazon S3) bucket versioning management
* Amazon Relational Database Service (Amazon RDS) snapshot creation
* Amazon Elastic Compute Cloud (Amazon EC2) instance management

The architecture employs Amazon Virtual Private Cloud (Amazon VPC) endpoints and private networking for secure communication, with AWS Lambda functions operating as task executors within private subnets. Amazon S3 provides data management and implements comprehensive AWS Identity and Access Management (IAM) roles and permissions to ensure proper access controls. This solution doesn’t include a chat history feature, and the chat isn’t stored.

## Prerequisites and limitations

* An active AWS account.
* Proper access control measures should be in place to help secure and control access. Examples of access control include using AWS Systems Manager, foundation models access, an IAM role for deployment, and service-based roles, disabling public access to Amazon S3 buckets, and setting up a dead-letter queue.
* An AWS Key Management Service (AWS KMS) [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk).
* AWS Command Line Interface (AWS CLI) version 2 or later, [installed](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) on the deployment environment.
* Terraform AWS Provider version 4 or later [installed](https://registry.terraform.io/providers/-/aws/latest/docs/guides/version-4-upgrade) and configured.
* Terraform version 1.5.7 or later [installed](https://developer.hashicorp.com/terraform/install) and configured.
* Review and [Define OpenAPI schemas for your agent's action groups in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-api-schema.html) to help protect against unauthorized access and maintain data integrity.
* [Access enabled](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access-modify.html) in your AWS account for the required Amazon Titan Text Embeddings v2 and either the Claude 3.5 Sonnet or Claude 3 Haiku [foundation models.](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) To avoid deployment failure, confirm that your target deployment AWS Region [supports the required models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html).
* A configured virtual private cloud (VPC) that follows the [AWS Well Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html) best practices.
* Completed review of the [Amazon Responsible AI policy](https://aws.amazon.com/ai/responsible-ai/policy/).

**Product versions**

* Amazon Titan Text Embeddings v2
* Anthropic Claude 3.5 Sonnet or Claude 3 Haiku
* Terraform AWS Provider version 4 or later
* Terraform version 1.5.7 or later

## Architecture

The following diagram shows the workflow and architecture components for this pattern.

![Workflow to automate common AWS infrastructure operations by using Amazon Bedrock.](/images/prescriptive-guidance/latest/patterns/images/pattern-img/924e503f-bfc5-4452-abdf-d72a58d4d36f/images/bd56ad29-b435-4543-8ee8-dc4e1d38df18.png)

The solution architecture consists of multiple layers that work together to process natural language requests and execute corresponding AWS operations:

1. The user makes operations requests through the Amazon Bedrock chat console.
2. The chatbot uses Amazon Bedrock Knowledge Bases for request processing. It implements the Amazon Titan Text Embeddings v2 model for natural language processing.
3. If the user prompt includes an action request, the Amazon Bedrock action group uses either the Anthropic Claude 3 Haiku or the Claude 3.5 Sonnet model (depending on your choice) for execution logic and defines operations through an OpenAPI schema.
4. The action group reaches the Amazon VPC [endpoints](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/what-are-vpc-endpoints.html) using AWS PrivateLink for secure service communication.
5. The AWS Lambda function is reached through Amazon VPC endpoints for Amazon Bedrock services.
6. The Lambda functions are the primary execution engine. Based on the request, the Lambda function calls the API to perform actions on the AWS services. The Lambda function also handles operation routing and execution.
7. The AWS services get the API request from the Lambda function and corresponding operations are performed.
8. The Lambda function computes an output payload that is understood by Amazon Bedrock.
9. This payload is sent to Amazon Bedrock by using PrivateLink for secure service communication. The large language model (LLM) used by Amazon Bedrock understands this payload and converts it into human understandable format.
10. The output is then shown to the user on the Amazon Bedrock chat console.

The solution enables the following primary operations:

* Amazon S3 – Enable bucket versioning for version control.
* Amazon RDS – Create database snapshots for backup.
* Amazon EC2 – List instances and control the start and stop of instances.

## Tools

**AWS services**

* [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) is a fully managed service that makes high-performing foundation models (FMs) from leading AI startups and Amazon available for your use through a unified API.
* [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open source tool that helps you interact with AWS services through commands in your command-line shell.
* [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
* [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
* [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
* [Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html) is an on-demand serverless configuration for Amazon OpenSearch Service.
* [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) helps you create unidirectional, private connections from your virtual private clouds (VPCs) to services outside of the VPC.
* [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud.
* [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
* [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) helps you manage your applications and infrastructure running in the AWS Cloud. It simplifies application and resource management, shortens the time to detect and resolve operational problems, and helps you manage your AWS resources securely at scale.
* [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

**Other tools**

* [Git](https://git-scm.com/docs) is an open source, distributed version control system.
* [Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool from HashiCorp that helps you create and manage cloud and on-premises resources.

**Code repository**

The code for this pattern is available in the GitHub [aws-samples/infra-ops-orchestrator](https://github.com/aws-samples/infra-ops-orchestrator) repository.

## Best practices

* Monitor Lambda execution logs regularly. For more information, see [Monitoring and troubleshooting Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html). For more information about best practices, see [Best practices for working with AWS Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html).
* Review security configurations periodically to ensure compliance with your organization's requirements. For more information, see [Security best practices](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-bp.html).
* Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.

## Epics

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | To clone the repository on your local machine, run the following command:   ```   git clone "git@github.com:aws-samples/infra-ops-orchestrator.git" cd infra-ops-orchestrator ``` | AWS DevOps, DevOps engineer |
| Edit the environment variables. | Edit the `terraform.tfvars` file. in the root directory of the cloned repository. Review the placeholders that are indicated by `[XXXXX]`, and update them according to your environment. | AWS DevOps, DevOps engineer |
| Create the infrastructure. | To create the infrastructure, run the following commands:   ```   terraform init ```  ```   terraform plan ```   Review the execution plan carefully. If the planned changes are acceptable, then run the following command:   ```   terraform apply --auto-approve ``` | AWS DevOps, DevOps engineer |

| Task | Description | Skills required |
| --- | --- | --- |
| Access the solution. | After successful deployment, follow these steps to use the chat-based interface:  1. To access the Infrastructure Orchestrator Assistant, sign in to the AWS Management Console using an [IAM role with Amazon Bedrock permissions](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html), and open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock/](https://console.aws.amazon.com/bedrock/). Select **Agents** from the left navigation pane. Then, choose the Infrastructure Orchestrator Assistant in the **Agents** section. 2. Make sure that target resources exist in your AWS environment for the following suggestions, and then try these example operations:  * Create a snapshot backup of an Amazon RDS instance by asking: 'Create a snapshot of RDS instance [instance-name]'    * Enable versioning on an Amazon S3 bucket by asking: 'Enable versioning for bucket [bucket-name]'    * List Amazon EC2 instances by asking: 'List all EC2 instances'    * Start or stop an Amazon EC2 instance by asking: 'Start EC2 instance [instance-id]' or 'Stop EC2 instance [instance-id]'  Note: Replace the values in brackets with the actual resource names or IDs from your AWS environment. | AWS DevOps, DevOps engineer |

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the created resources. | To delete all infrastructure created by this pattern, run the following command:   ```   terraform plan -destroy ```   Review the destruction plan carefully. If the planned deletions are acceptable, then run the following command:   ```   terraform destroy ```   Note: This command will permanently delete all resources created by this pattern. The command will prompt for confirmation before removing any resources. | AWS DevOps, DevOps engineer |

## Troubleshooting

| Issue | Solution |
| --- | --- |
| Agent behavior | For information about this issue, see [Test and troubleshoot agent behavior](https://docs.aws.amazon.com/lambda/latest/dg/troubleshooting-networking.html) in the Amazon Bedrock documentation. |
| Lambda network issues | For information about these issues, see [Troubleshoot networking issues in Lambda](https://docs.aws.amazon.com/lambda/latest/dg/troubleshooting-networking.html) in the Lambda documentation. |
| IAM permissions | For information about these issues, see [Troubleshoot IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot.html) in the IAM documentation. |

## Related resources

* [Creating a DB snapshot for a Single-AZ DB instance for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html)
* [Define OpenAPI schemas for your agent's action groups in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-api-schema.html)
* [Enabling versioning on buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html)
* [How Amazon Bedrock Agents works](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-how.html)
* [Retrieve data and generate AI responses with Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/aws-privatelink.html)
* [Securely Access Services Over AWS PrivateLink](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/aws-privatelink.html)
* [Stop and start Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html)
* [Use action groups to define actions for your agent to perform](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html)