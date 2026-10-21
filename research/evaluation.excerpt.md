# Evaluate the performance of Amazon Bedrock resources

[PDF](https://docs.aws.amazon.com/pdfs/bedrock/latest/userguide/bedrock-ug.pdf#evaluation)

[RSS](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-ug.rss)

[Markdown](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.md "Download Markdown")

Agent Setup Up-to-date AWS docs, tested procedures, and IAM guardrails via a single setup prompt in your AI coding agent.

- [x] Focus mode

Evaluate the performance of Amazon Bedrock resources - Amazon Bedrock

[](https://docs.aws.amazon.com/pdfs/bedrock/latest/userguide/bedrock-ug.pdf#evaluation "Open PDF")

[Documentation](https://docs.aws.amazon.com/index.html)[Amazon Bedrock](https://docs.aws.amazon.com/bedrock/index.html)[User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)

Use Amazon Bedrock evaluations to evaluate the performance and effectiveness of Amazon Bedrock models and knowledge bases, as well as models and Retrieval Augmented Generation (RAG) sources outside of Amazon Bedrock. Amazon Bedrock can compute performance metrics such as the semantic robustness of a model and the correctness of a knowledge base in retrieving information and generating responses. For model evaluations, you can also use a team of human workers to rate and provide their input for the evaluation.

Automatic evaluations, including evaluations that use Large Language Models (LLMs), produce computed scores and metrics that help you assess the effectiveness of a model and knowledge base. Human-based evaluations use a team of people who provide their ratings and preferences in relation to certain metrics.

Programmatic model evaluation jobs
Programmatic model evaluation jobs allow you to quickly evaluate a model's ability to perform a task. You can either provide your own custom prompt dataset that you've tailored to a specific use case, or you can use an available built-in dataset.

Model evaluation jobs that use human workers
Model evaluation jobs that use human workers allow you to bring human input to the model evaluation process. They can be employees of your company or a group of subject-matter experts from your industry.

Model evaluation jobs that use a judge model
Model evaluation jobs that use a judge model allow you to quickly evaluate a model's responses through using a second LLM. The second LLM scores the response and provides an explanation for each response.

RAG evaluations that use Large Language Models (LLMs)
LLM-based evaluations compute performance metrics for the knowledge base. The metrics reveal if a RAG source or Amazon Bedrock Knowledge Base is able to retrieve highly relevant information and generate useful, appropriate responses. You provide a dataset that contains the prompts or user queries for evaluating how a knowledge base retrieves information and generates responses for those given queries. The dataset must also include ‘ground truth’ or the expected retrieved texts and responses for the queries so that the evaluation can check if your knowledge base is aligned with what’s expected.

Model evaluation jobs support using the following types of Amazon Bedrock models:

*   Foundation models

*   Amazon Bedrock Marketplace models

*   Customized foundation models

*   Imported foundation models

*   Prompt routers

*   Models that you have purchased Provisioned Throughput

###### Topics

*   [Supported Regions and models for model evaluation](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-support.html)

*   [Creating an automatic model evaluation job in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-automatic.html)

*   [Creating a model evaluation job that use human workers in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-human.html)

*   [Evaluate model performance using another LLM as a judge](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html)

*   [Evaluate the performance of RAG sources using Amazon Bedrock evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html)

*   [Required Cross Origin Resource Sharing (CORS) permissions on S3 buckets](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-security-cors.html)

*   [Review model evaluation job reports and metrics in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-report.html)

*   [Data management and encryption in Amazon Bedrock evaluation job](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-data-management.html)

*   [CloudTrail management events in model evaluation jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/cloudtrail-events-in-model-evaluations.html)

