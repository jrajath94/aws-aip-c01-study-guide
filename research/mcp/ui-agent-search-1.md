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
        "Explore the text playground"
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
      "url": "https://docs.aws.amazon.com/nova/latest/nova2-userguide/getting-started-console.html",
      "title": "Explore the text playground",
      "context": "Use the Amazon Bedrock console text playground to submit prompts and explore text, image, document, and video understanding capabilities of Amazon Nova models",
      "recommended_sections": [
        "Explore the text playground"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-inference-topics.html",
      "title": "Amazon Bedrock playgrounds",
      "context": "Interactive environments in Amazon Bedrock where users can apply inference parameters and system instructions to foundation models",
      "recommended_sections": [
        "Advanced inference topics"
      ],
      "sections": [
        "Advanced inference topics"
      ],
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/nova/latest/userguide/getting-started-console.html",
      "title": "Amazon Bedrock image playground",
      "context": "A console playground in Amazon Bedrock for submitting text prompts and receiving generated image responses from a foundation model",
      "recommended_sections": [
        "Explore the text playground",
        "Getting started with Amazon Nova in the Amazon Bedrock console"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 6,
      "url": "https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/getting-started-use-amazon-bedrock-ide.html",
      "title": "Amazon Bedrock chat playground",
      "context": "Interactive environment in Amazon Bedrock in SageMaker Unified Studio where users can send text and image prompts to a model and receive responses",
      "recommended_sections": [
        "Chat with a model in the chat playground"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 7,
      "url": "https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/bedrock-playgrounds.html",
      "title": "image and video playground",
      "context": "An interactive environment in Amazon Bedrock for generating and manipulating images using natural language prompts, reference images, and foundation models",
      "recommended_sections": [
        "Experiment with the Amazon Bedrock playgrounds"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 8,
      "url": "https://docs.aws.amazon.com/code-library/latest/ug/java_2_bedrock-runtime_code_examples.html",
      "title": "Java Foundation Model (FM) Playground",
      "context": "Spring Boot sample application that demonstrates how to use Amazon Bedrock with Java through text, chat, and image playgrounds",
      "recommended_sections": [
        "Create a playground application to interact with Amazon Bedrock foundation models"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 9,
      "url": "https://docs.aws.amazon.com/next-generation-sagemaker/latest/userguide/getting-started-use-amazon-bedrock-ide.html",
      "title": "Amazon Bedrock chat playground",
      "context": "Interactive environment in Amazon Bedrock in SageMaker Unified Studio where users can send text and image prompts to a model and receive responses",
      "recommended_sections": [
        "Step 2: Chat with a model in the chat playground"
      ],
      "sections": null,
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "4c9719fe-2c78-48ab-a60b-3e51727e185d",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "references",
        "to": "Amazon Nova Lite",
        "to_description": "Amazon Nova model that balances intelligence, latency, and cost-effectiveness, optimized for complex low-latency scenarios with image, video, and text inputs",
        "from": "Explore the text playground"
      },
      {
        "relation": "references",
        "to": "Amazon Titan Text G1 - Lite",
        "to_description": "An Amazon Titan text model supporting fine-tuning with up to 4,096 tokens at batch sizes 1–2 and 2,048 tokens at batch sizes 3–6",
        "from": "Explore the text playground"
      },
      {
        "relation": "references",
        "to": "Amazon Nova video understanding",
        "to_description": "Amazon Nova's capability to process video inputs and perform tasks such as frame analysis, video QA, object tracking, and temporal segmentation.",
        "from": "Explore the text playground"
      },
      {
        "relation": "references",
        "to": "Claude Fable 5.1 model ID",
        "to_description": "Programmatic identifier used to invoke Claude Fable 5.1 via Amazon Bedrock APIs",
        "from": "Converse"
      },
      {
        "relation": "hasChild",
        "to": "suspend fun converse(): String",
        "to_description": "Send a text message to Amazon Nova using the Bedrock Converse API and return the model's text response",
        "from": "Converse"
      }
    ]
  }
}