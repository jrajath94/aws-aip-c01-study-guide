{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html",
      "title": "generative AI workflow",
      "context": "A sequence of connected nodes in Amazon Bedrock Flows where each node corresponds to a step that invokes an Amazon Bedrock or related resource",
      "recommended_sections": [
        "How Amazon Bedrock Flows works"
      ],
      "sections": [
        "How Amazon Bedrock Flows works"
      ],
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/code-library/latest/ug/bedrock-agent-runtime_example_bedrock-agent_GettingStartedWithBedrockFlows_section.html",
      "title": "create the flow",
      "context": "Define and configure an Amazon Bedrock Flow by specifying its name, IAM permissions, nodes, and node connections.",
      "recommended_sections": [
        "An end-to-end example showing how to create and invoke an Amazon Bedrock flow using an AWS SDK"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/flows-create.html",
      "title": "Try example flows",
      "context": "Explore pre-built example flows in Amazon Bedrock Flows to learn how to construct flows using the console",
      "recommended_sections": [
        "Create and design a flow in Amazon Bedrock"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/flows-ex.html",
      "title": "Try example flows",
      "context": "Explore pre-built example flows in Amazon Bedrock Flows to learn how to construct flows using the console",
      "recommended_sections": [
        "Try example flows"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/flows-get-started.html",
      "title": "Create your first flow in Amazon Bedrock",
      "context": "Step-by-step procedure to create, configure, and run a getting started flow in Amazon Bedrock Flows using the console",
      "recommended_sections": [
        "Create your first flow in Amazon Bedrock"
      ],
      "sections": null,
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "fed6b2c4-3ec5-49d0-8fc8-d4eef7d92b19",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "references",
        "to": "Amazon Bedrock Console",
        "to_description": "The web-based interface for experimenting with and testing Amazon Bedrock foundation models, including scaled-up prompt evaluation.",
        "from": "Try example flows"
      },
      {
        "relation": "hasChild",
        "to": "Create a flow with a condition node",
        "to_description": "A procedure to build and test an Amazon Bedrock flow that uses a condition node to route execution based on evaluated conditions",
        "from": "Try example flows"
      },
      {
        "relation": "references",
        "to": "Amazon Bedrock flow template",
        "to_description": "Pre-built JSON template from the Amazon Bedrock Flows Samples GitHub repository used to create and run flows for common configurations",
        "from": "Try example flows"
      },
      {
        "relation": "hasChild",
        "to": "Create a flow with a single prompt",
        "to_description": "A procedure to build and test an Amazon Bedrock flow that uses a single inline prompt node to generate a song playlist from a JSON input",
        "from": "Try example flows"
      },
      {
        "relation": "references",
        "to": "prompt node",
        "to_description": "An orchestration node in the Amazon Bedrock flow canvas that sends input to a foundation model and returns the model's completion",
        "from": "Create your first flow in Amazon Bedrock"
      }
    ]
  }
}