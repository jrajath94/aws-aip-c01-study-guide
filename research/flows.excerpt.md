# Build an end-to-end generative AI workflow with Amazon Bedrock Flows

[PDF](https://docs.aws.amazon.com/pdfs/bedrock/latest/userguide/bedrock-ug.pdf#flows)

[RSS](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-ug.rss)

[Markdown](https://docs.aws.amazon.com/bedrock/latest/userguide/flows.md "Download Markdown")

Agent Setup Up-to-date AWS docs, tested procedures, and IAM guardrails via a single setup prompt in your AI coding agent.

- [x] Focus mode

Build an end-to-end generative AI workflow with Amazon Bedrock Flows - Amazon Bedrock

[](https://docs.aws.amazon.com/pdfs/bedrock/latest/userguide/bedrock-ug.pdf#flows "Open PDF")

[Documentation](https://docs.aws.amazon.com/index.html)[Amazon Bedrock](https://docs.aws.amazon.com/bedrock/index.html)[User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)

Amazon Bedrock Flows offers the ability for you to use supported foundation models (FMs) to build workflows by linking prompts, foundational models, and other AWS services to create end-to-end solutions.

With flows, you can quickly build complex generative AI workflows using a visual builder, easily integrate with Amazon Bedrock offerings such as FMs, knowledge bases, and other AWS services such as AWS Lambda by transferring data between them, and deploying immutable workflows to move from testing to production in few clicks.

Refer to the following resources for more information about Amazon Bedrock Flows:

*   Pricing for Amazon Bedrock Flows is dependent on the resources that you use. For example, if you invoke a flow with a prompt node that uses an Amazon Titan model, you'll be charged for invoking that model. For more information, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/).

*   To see quotas for flows, see [Amazon Bedrock endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/bedrock.html) in the AWS General Reference.

The following are some example tasks that you can build a flow for in Amazon Bedrock:

*   **Create and send an email invite** – Create a flow connecting a prompt node, knowledge base node, and Lambda function node. Provide the following prompt to generate an email body: `Send invite to John Smith’s extended team for in-person documentation read for an hour at 2PM EST next Tuesday`. After processing the prompt, the flow queries a knowledge base to look up the email addresses of John Smith's extended team, and then sends the input to a Lambda function to send the invite to all the team members in the list.

*   **Troubleshoot using the error message and the ID of the resource that is causing the error** – The flow looks up the possible causes of the error from a documentation knowledge base, pulls system logs and other relevant information about the resource, and updates the faulty configurations and values for the resource.

*   **Generate reports** – Build a flow to generate metrics for top products. The flow looks for the sales metrics in a database, aggregates the metrics, generates a summary report for top product purchases, and publishes the report on the specified portal.

*   **Ingest data from a specified dataset** – Provide a prompt such as the following: 
```
Start ingesting new datasets added after 3/31 and report
                    failures
```
. The flow starts preparing data for ingestion and keeps reporting on the status. After the data preparation is complete, the flow starts the ingestion process filtering the failed data. After data ingestion is complete, the flow summarizes the failures and publishes a failure report.

Flows for Amazon Bedrock makes it easy for you link foundation models (FMs), prompts, and other AWS services to quickly create, test, and run your flows. You can manage flows using the visual builder in the Amazon Bedrock console or through the APIs.

The general steps for creating, testing, and deploying a flow are as follows:

###### Create the flow:

1.   Specify a flow name, description, and appropriate IAM permissions.

2.   Design your flow by deciding the nodes you want to use.

3.   Create or define all the resources you require for each node. For example, if you are planning to use an AWS Lambda function, define the functions you need for the node to complete its task.

4.   Add nodes to your flow, configure them, and create connections between the nodes by linking the output of a node to the input of another node in the flow.

###### Test the flow:

1.   Prepare the flow, so that the latest changes apply to the _working draft_ of the flow, a version of the flow that you can use to iteratively test and update your flow

2.   Test the flow by invoking it with sample inputs to see the outputs it yields.

3.   When you're satisfied with a flow's configuration, you can create a snapshot of it by publishing a _version_. The version preserves flow definition as it exists at the time of the creation. Versions are immutable because they act as a snapshot of the flow at the time it was created.

###### Deploy the flow

1.   Create an alias that points to the version of your flow that you want to use in your application.

2.   Set up your application to make `InvokeFlow` requests to the alias. If you need to revert to an older version or upgrade to a newer one, you can change the routing configuration of the alias.

###### Topics

*   [How Amazon Bedrock Flows works](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html)

*   [Supported Regions and models for flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-supported.html)

*   [Prerequisites for Amazon Bedrock Flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-prereq.html)

*   [Create and design a flow in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-create.html)

*   [View information about flows in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-view.html)

*   [Modify a flow in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-modify.html)

*   [Include guardrails in your flow in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-guardrails.html)

*   [Test a flow in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-test.html)

*   [Run Amazon Bedrock flows asynchronously with flow executions](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-create-async.html)

*   [Deploy a flow to your application using versions and aliases](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-deploy.html)

*   [Invoke an AWS Lambda function from an Amazon Bedrock flow in a different AWS account](https://docs.aws.amazon.com/bedrock/latest/userguide/flow-cross-account-lambda.html)

*   [Converse with an Amazon Bedrock flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-multi-turn-invocation.html)

*   [Run Amazon Bedrock Flows code samples](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-code-ex.html)

*   [Delete a flow in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-delete.html)

