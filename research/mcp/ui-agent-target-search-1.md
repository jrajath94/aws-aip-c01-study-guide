{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/playgrounds.html",
      "title": "Amazon Bedrock console playgrounds",
      "context": "Interactive console environments in Amazon Bedrock for submitting prompts and generating text or image responses without writing code",
      "recommended_sections": [
        "Generate responses in the console using playgrounds"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started-console.html",
      "title": "Amazon Bedrock console playgrounds",
      "context": "Interactive console environments in Amazon Bedrock for submitting prompts and generating text or image responses without writing code",
      "recommended_sections": [
        "Explore the text playground",
        "Explore the image playground"
      ],
      "sections": [
        "Get started in the Amazon Bedrock console",
        "Explore the text playground",
        "Explore the image playground"
      ],
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/getting-started-use-amazon-bedrock-ide.html",
      "title": "Amazon Bedrock chat playground",
      "context": "Interactive environment in Amazon Bedrock in SageMaker Unified Studio where users can send text and image prompts to a model and receive responses",
      "recommended_sections": [
        "Chat with a model in the chat playground"
      ],
      "sections": [
        "Get started with Amazon Bedrock in SageMaker Unified Studio",
        "Chat with a model in the chat playground"
      ],
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/next-generation-sagemaker/latest/userguide/getting-started-use-amazon-bedrock-ide.html",
      "title": "Explore Amazon Bedrock foundation models",
      "context": "Select and access a foundation model from the Amazon Bedrock model catalog in the SageMaker Unified Studio playground",
      "recommended_sections": [
        "Step 1: Explore Amazon Bedrock foundation models",
        "Step 2: Chat with a model in the chat playground"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/inference-api.html",
      "title": "aws bedrock-runtime invoke-model --model-id openai.gpt-oss-120b-1:0 service-tier priority CLI",
      "context": "AWS CLI command to invoke the OpenAI GPT model with a priority service tier and generate a text response",
      "recommended_sections": null,
      "sections": [
        "Inference using Invoke API",
        "Submit a single prompt with InvokeModel",
        "Invoke model code examples",
        "Generate text with a text prompt",
        "Generate text with a text prompt using service tier",
        "Generate an image with a text prompt",
        "Generate embeddings from text",
        "Generate embeddings from an image",
        "Generate a text response to an image with an accompanying text prompt",
        "Generate a text response to a video uploaded to Amazon S3 with an accompanying text prompt",
        "Generate a text response to a video converted to a base64-encoded string with an accompanying text prompt",
        "Invoke model with streaming code example"
      ],
      "metadata": null
    },
    {
      "rank_order": 6,
      "url": "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html",
      "title": "bedrock:Converse",
      "context": "Sends messages to the specified Amazon Bedrock model. Converse provides a consistent interface that works with all models that support messages. This allows you to write code once and use it with different models. If a model has unique inference parameters, you can also pass those unique parameters to the model.",
      "recommended_sections": null,
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 7,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-use.html",
      "title": "Converse",
      "context": "Sends messages to the specified Amazon Bedrock model. Converse provides a consistent interface that works with all models that support messages. This allows you to write code once and use it with different models. If a model has unique inference parameters, you can also pass those unique parameters to the model. Amazon Bedrock doesn't store any text, images, or documents that you provide as content. The data is only used to generate the response. You can submit a prompt by including it in the…",
      "recommended_sections": null,
      "sections": [
        "Use an inference profile in model invocation"
      ],
      "metadata": null
    },
    {
      "rank_order": 8,
      "url": "https://docs.aws.amazon.com/nova/latest/userguide/getting-started-console.html",
      "title": "Amazon Bedrock image playground",
      "context": "A console playground in Amazon Bedrock for submitting text prompts and receiving generated image responses from a foundation model",
      "recommended_sections": [
        "Getting started with Amazon Nova in the Amazon Bedrock console"
      ],
      "sections": null,
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "aadbaf92-0390-46e0-af23-ae0feff09967",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "references",
        "to": "Claude Fable 5.1 model ID",
        "to_description": "Programmatic identifier used to invoke Claude Fable 5.1 via Amazon Bedrock APIs",
        "from": "Converse"
      },
      {
        "relation": "references",
        "to": "Command R",
        "to_description": "Cohere's scalable large language model optimized for retrieval-augmented generation and tool use in enterprise applications with a 128K context window",
        "from": "Converse"
      },
      {
        "relation": "hasChild",
        "to": "suspend fun converse(): String",
        "to_description": "Send a text message to Amazon Nova using the Bedrock Converse API and return the model's text response",
        "from": "Converse"
      },
      {
        "relation": "hasChild",
        "to": "send text message to Anthropic Claude using Converse API async",
        "to_description": "Send a text message to Anthropic Claude using the Amazon Bedrock Converse API with the asynchronous Java SDK client and retrieve the response via CompletableFuture",
        "from": "Converse"
      },
      {
        "relation": "references",
        "to": "AI21 Labs foundation model",
        "to_description": "Third-party foundation models from AI21 Labs available for inference in Amazon Bedrock",
        "from": "Converse"
      }
    ]
  }
}