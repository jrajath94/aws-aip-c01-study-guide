AWS Documentation from https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-report.html:

# Review model evaluation job reports and metrics in Amazon Bedrock

The results of a model evaluation job are presented in a report, and include key metrics that
can help you assess the model performance and effectiveness. The results of a model evaluation job are
available through the Amazon Bedrock console or by downloading the results from the Amazon S3 bucket you
specified when the job was created.

Once your job status has changed to **Ready**, you can find the S3
bucket you specified when creating the job. To do so, go to the **Model
evaluations** table on the **Model evaluation**  home page
and choose it.

Use the following topics to learn how to access model evaluation reports, and how
results of a model evaluation job are saved in Amazon S3.

###### Topics

* [Review metrics for an automated model evaluation job in Amazon Bedrock (console)](./model-evaluation-report-programmatic.html)
* [Review a human-based model evaluation job in Amazon Bedrock (console)](./model-evaluation-report-human-customer.html)
* [Understand how the results of your model evaluation job are saved in Amazon S3](./model-evaluation-report-s3.html)