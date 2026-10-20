AWS Documentation from https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html:

# Process multiple prompts with batch inference

With batch inference, you can submit multiple prompts and generate responses asynchronously. You can format your input data by using either the `InvokeModel` or `Converse` API format. Batch inference helps you process a large number of requests efficiently by sending a single request and generating the responses in an Amazon S3 bucket. After defining model inputs in files you create, you upload the files to an S3 bucket. You then submit a batch inference request and specify the S3 bucket. After the job is complete, you can retrieve the output files from S3. You can use batch inference to improve the performance of model inference on large datasets.

###### Note

Batch inference isn't supported for provisioned models.

###### Note

Batch inference doesn't support tool calling (function calling) for jobs that use the `Converse` invocation type. Records that include `toolConfig` fail with a 400 error. To use tool calling with batch inference, create the job with the `InvokeModel` invocation type and format each `modelInput` in the model's native request format. Structured outputs are supported with both invocation types. For more information, see [Get validated JSON results from models](./structured-output.html).

See the following resources for general information about batch inference:

* To see pricing for batch inference, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/).
* To see quotas for batch inference, see [Amazon Bedrock endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/bedrock.html) in the AWS General Reference.
* To receive notifications when batch inference jobs complete or change state instead of polling, see [Monitor Amazon Bedrock job state changes using Amazon EventBridge](./monitoring-eventbridge.html).

###### Topics

* [Supported Regions and models for batch inference](./batch-inference-supported.html)
* [Prerequisites for batch inference](./batch-inference-prereq.html)
* [Create a batch inference job](./batch-inference-create.html)
* [Monitor batch inference jobs](./batch-inference-monitor.html)
* [Stop a batch inference job](./batch-inference-stop.html)
* [View the results of a batch inference job](./batch-inference-results.html)
* [Code example for batch inference](./batch-inference-example.html)
* [Submit a batch of prompts with the OpenAI Batch API](./inference-openai-batch.html)