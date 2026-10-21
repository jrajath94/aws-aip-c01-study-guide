{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/generative-ai-nlp-healthcare/llms.html",
      "title": "prompt engineering",
      "context": "The practice of crafting and optimizing input prompts by selecting appropriate words, phrases, and characters to effectively use LLMs for a wide variety of applications.",
      "recommended_sections": [
        "Prompt engineering",
        "Few-shot prompting"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html",
      "title": "prompt engineering techniques",
      "context": "Methods such as chain-of-thought, logic-of-thought, and few-shot prompting that encourage a model to reason through response generation steps",
      "recommended_sections": [
        "Task Statement 3.2: Choose effective prompt engineering techniques."
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-engineering-guidelines.html",
      "title": "prompt",
      "context": "A specific set of inputs provided by the user that guide LLMs on Amazon Bedrock to generate an appropriate response or output for a given task or instruction",
      "recommended_sections": null,
      "sections": [
        "Prompt engineering concepts",
        "What is a prompt?",
        "Components of a prompt",
        "Few-shot prompting vs. zero-shot prompting",
        "Prompt template",
        "Maintain recall over Amazon Bedrock inference requests"
      ],
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gencost03-bp01.html",
      "title": "Amazon Bedrock prompt optimization",
      "context": "An Amazon Bedrock feature for automatically optimizing prompts, supported on the bedrock-runtime endpoint for Claude Sonnet 5",
      "recommended_sections": [
        "Resources",
        "Implementation steps"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-customize-prompt-engineering.html",
      "title": "few-shot image classification prompt example",
      "context": "A prompt template that incorporates labeled image examples to guide a foundation model to classify a new image class with minimal training data",
      "recommended_sections": [
        "Few-shot learning"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 6,
      "url": "https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops05-bp01.html",
      "title": "prompt engineering",
      "context": "The practice of crafting and optimizing input prompts by selecting appropriate words, phrases, and characters to effectively use LLMs for a wide variety of applications.",
      "recommended_sections": [
        "Implementation steps"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 7,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/dev-experimenting-prompt-optimization.html",
      "title": "prompt optimization",
      "context": "Technique to reduce generative AI inference costs by refining prompts, truncating responses, caching outputs, and downgrading models for non-critical paths",
      "recommended_sections": [
        "Prompt optimization techniques"
      ],
      "sections": null,
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "8bf84a19-4f8d-47b5-8f13-a2bdfc03db42",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "references",
        "to": "few-shot learning",
        "to_description": "A technique where a model is guided using a limited number of labeled examples to generalize to new classes or tasks.",
        "from": "few-shot image classification prompt example"
      },
      {
        "relation": "references",
        "to": "foundation model",
        "to_description": "Large pre-trained AI model accessible via Amazon Bedrock that can handle tasks like text generation, summarization, and content creation without requiring model training",
        "from": "few-shot image classification prompt example"
      },
      {
        "relation": "relatesTo",
        "to": "Simple optimization",
        "to_description": "A fast, heuristic rewrite of a single short prompt for one model in Amazon Bedrock",
        "from": "prompt optimization"
      },
      {
        "relation": "relatesTo",
        "to": "ensemble learning",
        "to_description": "The practice of combining multiple LLMs to achieve performance that surpasses that of a single model.",
        "from": "prompt optimization"
      },
      {
        "relation": "relatesTo",
        "to": "agent caching strategies",
        "to_description": "Design principle to implement appropriate caching for repetitive agent tasks to reduce inference costs",
        "from": "prompt optimization"
      }
    ]
  }
}