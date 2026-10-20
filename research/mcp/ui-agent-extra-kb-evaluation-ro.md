AWS Documentation from https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-create-ro.html:

# Creating a retrieve-only RAG evaluation job

You can create a RAG evaluation job using the AWS Management Console, AWS CLI, or a supported AWS SDK.

This type of job requires access to an evaluator model.
For a list of supported evaluator models, see [Supported models](./evaluation-kb.html#evaluation-kb-supported).

To create a job using the following instructions, you also need a prompt dataset. If you haven't already created one, see [Create a prompt dataset for a RAG evaluation in Amazon Bedrock](./knowledge-base-evaluation-prompt.html).

Console
:   1. Open the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home).
    2. In the left-hand pane under **Inference and assessment**, select **Evaluations**.
    3. In the **RAG evaluations** pane, choose **Create**.
    4. Enter your RAG evaluation details by doing the following:

       1. In the **Evaluation details** pane under **Evaluation name**, enter a name for your evaluation job. The name
          you choose must be unique within your AWS Region.
       2. Optionally, under **Description - *optional***, enter a description for your evaluation job.
       3. Under **Evaluator model**, choose **Select model** and select the evaluator model you want to perform your
          evaluation.
    5. Enter the inference source for your evaluation job. With Amazon Bedrock RAG evaluations, you can either evaluate the performance of Amazon Bedrock Knowledge Bases,
       or of other RAG sources by providing your own inference response data in the [prompt dataset](./knowledge-base-evaluation-prompt.html).
       To select an Amazon Bedrock Knowledge Base, do the following:

       1. In the **Inference source** pane, under **Select source** select **Bedrock Knowledge Base**.
       2. Under **Choose a Knowledge Base**, select a Knowledge Base using the dropdown list.
    6. To bring your own inference response data, do the following:

       1. In the **Inference source** pane, under **Select source** select **Bring your own inference responses**.
       2. For **Source name**, enter a name for the RAG source you used to create the response data. The name you enter must match the
          `knowledgeBaseIdentifier` parameter in your [prompt dataset](./knowledge-base-evaluation-prompt.html).
    7. In the **Inference source** pane, under **Evaluation type**, select **Retrieval only**.
    8. Select the built-in metrics you want the evaluator model to use by selecting
       at least one metric in the **Metrics** pane.
    9. Define your input and output locations for your dataset and results by doing the following:

       1. In the **Datasets** pane under **Choose a prompt dataset**, enter the Amazon S3 URI for your prompt dataset,
          or choose **Browse S3** and select your file. To see a definition of the required prompt dataset format for a retrieve-only
          evaluation job, see [Create a prompt dataset for retrieve-only RAG evaluation jobs](./knowledge-base-evaluation-prompt-retrieve.html).
       2. Under **Evaluation results**, enter an Amazon S3 location for Amazon Bedrock to save your results, or choose **Browse S3** to
          select a location.
    10. Under **Amazon Bedrock IAM role - Permissions**, select **Create and use a new service role** to have Amazon Bedrock create a
        new IAM role for the evaluation job, or select **Use an existing service role** to pick an existing IAM role. For a list of the required
        permissions to create and run an evaluation job, see [Prerequisites](./knowledge-base-evaluation-create.html#knowledge-base-evaluation-create-prereqs).
    11. (Optional) to use your own KMS key to encrypt your evaluation data, under **KMSkey - *Optional***,
        check **Customize encryption settings (advanced)** and select your AWS KMS key. By default, Amazon Bedrock encrypts your evaluation job data with an
        AWS-owned KMS key.
    12. Choose **Create** to finish creating your evaluation job.

AWS CLI
:   ###### Create a retrieve-only evaluation job for an Amazon Bedrock Knowledge Base

    * Run the following AWS CLI command using the example JSON file.

      ```
      aws bedrock create-evaluation-job --cli-input-json file://my_eval_job.json
      ```

      ```
      {
          "jobName": "my_rag_eval",
          "roleArn": "arn:aws:iam::111122223333:role/service-role/Amazon-Bedrock-IAM-Role-Amazon-Bedrock-IAM-Role-20250218T063974",
          "applicationType": "RagEvaluation",
          "evaluationConfig": {
              "automated": {
                  "datasetMetricConfigs": [
                      {
                          "taskType": "General",
                          "dataset": {
                              "name": "text_dataset",
                              "datasetLocation": {
                                  "s3Uri": "s3://amzn-s3-demo-bucket/input/retrieval-only/retrieve-eval-byoir.jsonl"
                              }
                          },
                          "metricNames": [
                              "Builtin.ContextCoverage",
                              "Builtin.ContextRelevance"
                          ]
                      }
                  ],
                  "evaluatorModelConfig": {
                      "bedrockEvaluatorModels": [
                          {
                              "modelIdentifier": "us.meta.llama3-1-70b-instruct-v1:0"
                          }
                      ]
                  }
              }
          },
         "inferenceConfig": {
              "ragConfigs": [
                  {
                      "knowledgeBaseConfig": {
                          "retrieveConfig": {
                              "knowledgeBaseId": "your-knowledge-base-id",
                              "knowledgeBaseRetrievalConfiguration": {
                                  "vectorSearchConfiguration": {
                                      "numberOfResults": 3
                                  }
                              }
                          }
                      }
                  }
              ]
          },
          "outputDataConfig": {
              "s3Uri": "s3://amzn-s3-demo-bucket/output/"
          }
      }
      ```

    ###### Create a retrieve-only evaluation job with your own inference response data

    * Run the following AWS CLI command using the example JSON file.

      ```
      aws bedrock create-evaluation-job --cli-input-json file://my_eval_job.json
      ```

      ```
      {
          "jobName": "my_rag_eval",
          "roleArn": "arn:aws:iam::111122223333:role/service-role/Amazon-Bedrock-IAM-Role-Amazon-Bedrock-IAM-Role-20250218T063974",
          "applicationType": "RagEvaluation",
          "evaluationConfig": {
              "automated": {
                  "datasetMetricConfigs": [
                      {
                          "taskType": "General",
                          "dataset": {
                              "name": "text_dataset",
                              "datasetLocation": {
                                  "s3Uri": "s3://amzn-s3-demo-bucket/input/retrieval-only/retrieve-eval-byoir.jsonl"
                              }
                          },
                          "metricNames": [
                              "Builtin.ContextCoverage",
                              "Builtin.ContextRelevance"
                          ]
                      }
                  ],
                  "evaluatorModelConfig": {
                      "bedrockEvaluatorModels": [
                          {
                              "modelIdentifier": "us.meta.llama3-1-70b-instruct-v1:0"
                          }
                      ]
                  }
              }
          },
          "inferenceConfig": {
              "ragConfigs": [
                  {
                      "precomputedRagSourceConfig": {
                          "retrieveSourceConfig": {
                              "ragSourceIdentifier": "my_rag_source"
                          }
                      }
                  }
              ]
          },
          "outputDataConfig": {
              "s3Uri": "s3://amzn-s3-demo-bucket/output/"
          }
      }
      ```

SDK for Python (Boto3)
:   The following python example demonstrates how to create a retrieve-only job for an Amazon Bedrock Knowledge Base using the AWS SDK for Python (Boto3) To learn more about creating an evaluation job using Boto3, refer to
    [`create_evaluation_job`](https://boto3.amazonaws.com/v1/documentation/api/1.35.6/reference/services/bedrock/client/create_evaluation_job.html) in the Boto3
    documentation.

    ```
    import boto3
    client = boto3.client('bedrock')

    job_response = client.create_evaluation_job(
        jobName="my_evaluation_job",
        jobDescription="two different task types",
        roleArn="arn:aws:iam::111122223333:role/service-role/Amazon-Bedrock-IAM-RoleAmazon-Bedrock-IAM-Role",
        applicationType="RagEvaluation",
        inferenceConfig={
            "ragConfigs": [
                {
                    "knowledgeBaseConfig": {
                        "retrieveConfig": {
                            "knowledgeBaseId": "your-knowledge-base-id",
                            "knowledgeBaseRetrievalConfiguration": {
                                "vectorSearchConfiguration": {
                                    "numberOfResults": 10,
                                    "overrideSearchType": "HYBRID"
                                }
                            }
                        }
                    }
                }
            ]
        },
        outputDataConfig={
            "s3Uri":"s3://amzn-s3-demo-bucket-model-evaluations/outputs/"
        },
        evaluationConfig={
            "automated": {
                "datasetMetricConfigs": [
                    {
                        "taskType": "Summarization",
                        "dataset": {
                            "name": "RagDataset",
                            "datasetLocation": {
                                "s3Uri": "s3://amzn-s3-demo-bucket/input_data/data_3_rng.jsonl"
                            }
                        },
                        "metricNames": [
                            "Builtin.ContextCoverage"
                        ]
                    }
                ],
                "evaluatorModelConfig":
                    {
                        "bedrockEvaluatorModels": [{
                            "modelIdentifier": "meta.llama3-1-70b-instruct-v1:0"
                        }]
                    }
            }
        }
    )

    print(job_request)
    ```