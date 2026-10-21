{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/bda-using-api.html",
      "title": "Blueprint ARN",
      "context": "An Amazon Resource Name identifying a blueprint used to retrieve custom output for processed data in Bedrock Data Automation",
      "recommended_sections": [
        "Using the Bedrock Data Automation API"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/bda-cli-guide.html",
      "title": "InvokeDataAutomation",
      "context": "Sync API: Invoke data automation.",
      "recommended_sections": [
        "Using Amazon Bedrock Data Automation CLI"
      ],
      "sections": [
        "Using Amazon Bedrock Data Automation CLI",
        "Create your first Data Automation project",
        "Complete parameter reference",
        "Creating a Blueprint",
        "Using your Blueprint",
        "Adding a Blueprint to a project",
        "Verifying Blueprint integration",
        "Managing multiple Blueprints",
        "Process Documents Asynchronously",
        "Check Processing Status",
        "Retrieve Results",
        "Process Documents Synchronously",
        "Process Images Synchronously"
      ],
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-aws-infrastructure-operations-by-using-amazon-bedrock.html",
      "title": "Amazon Bedrock action group",
      "context": "A component of Amazon Bedrock agents that defines the actions an agent can perform, enabling automated remediation and API calls to AWS services.",
      "recommended_sections": [
        "Architecture"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation-runtime_InvokeDataAutomation.html",
      "title": "InvokeDataAutomation",
      "context": "Sync API: Invoke data automation.",
      "recommended_sections": null,
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_Types_Data_Automation_for_Amazon_Bedrock.html",
      "title": "DataAutomationLibrary",
      "context": "A data automation library resource in Amazon Bedrock that stores entity types and metadata for data automation workflows",
      "recommended_sections": [
        "Data Automation for Amazon Bedrock"
      ],
      "sections": null,
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "35dfb2e3-8123-4c43-9969-62fe2d15b137",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "references",
        "to": "BDA figure entity response",
        "to_description": "BDA response object for figure elements such as charts and graphs, including summary, representation, cropped images in S3 for async, subtype, title, and reading order",
        "from": "InvokeDataAutomation"
      },
      {
        "relation": "hasChild",
        "to": "InvokeDataAutomation JSON response example",
        "to_description": "JSON response example from InvokeDataAutomation showing standard and custom output for an image including IAB categories, logos, text detection, and custom inference results",
        "from": "InvokeDataAutomation"
      },
      {
        "relation": "hasChild",
        "to": "topics response example",
        "to_description": "JSON snippet showing the topics section of a BDA InvokeDataAutomation response with a generated topic summary, transcript text, and segment indices.",
        "from": "InvokeDataAutomation"
      },
      {
        "relation": "hasChild",
        "to": "content_moderation response example",
        "to_description": "JSON snippet showing the content_moderation section of a BDA InvokeDataAutomation response with per-segment moderation category confidence scores.",
        "from": "InvokeDataAutomation"
      },
      {
        "relation": "references",
        "to": "BDA audio standard output",
        "to_description": "Structured response object returned by InvokeDataAutomation for audio files, containing metadata, audio items, segments, content moderation, topics, and statistics.",
        "from": "InvokeDataAutomation"
      }
    ]
  }
}