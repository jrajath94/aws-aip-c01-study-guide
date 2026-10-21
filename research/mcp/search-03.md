{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgentActionGroup.html",
      "title": "AgentActionGroup",
      "context": "A CloudFormation resource type that defines an inline Amazon Bedrock agent's action group and its associated executor, schema, and state",
      "recommended_sections": null,
      "sections": [
        "AgentActionGroup",
        "Contents",
        "See Also"
      ],
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_Types_Agents_for_Amazon_Bedrock_Runtime.html",
      "title": "AgentActionGroup",
      "context": "A CloudFormation resource type that defines an inline Amazon Bedrock agent's action group and its associated executor, schema, and state",
      "recommended_sections": [
        "Agents for Amazon Bedrock Runtime"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/agents-how.html",
      "title": "action group",
      "context": "A set of actions defined in a Lambda function with an API schema that Amazon Bedrock Agents uses to perform specific tasks such as querying availability or completing bookings",
      "recommended_sections": [
        "Runtime process"
      ],
      "sections": [
        "How Amazon Bedrock Agents works",
        "Build-time configuration",
        "Runtime process"
      ],
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_FunctionSchema.html",
      "title": "action group",
      "context": "A set of actions defined in a Lambda function with an API schema that Amazon Bedrock Agents uses to perform specific tasks such as querying availability or completing bookings",
      "recommended_sections": [
        "Contents",
        "FunctionSchema"
      ],
      "sections": [
        "FunctionSchema",
        "Contents",
        "See Also"
      ],
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-agentactiongroup.html",
      "title": "AgentActionGroup",
      "context": "A CloudFormation resource type that defines an inline Amazon Bedrock agent's action group and its associated executor, schema, and state",
      "recommended_sections": null,
      "sections": [
        "AWS::Bedrock::Agent AgentActionGroup",
        "Syntax",
        "JSON",
        "YAML",
        "Properties"
      ],
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "d3105f88-e5c4-4b31-8fd0-98af5512ee96",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "relatesTo",
        "to": "wave planning",
        "to_description": "The process by which the portfolio team prioritizes applications and assigns them to waves in logical move groups, considering migration complexity and dependencies.",
        "from": "orchestration"
      },
      {
        "relation": "relatesTo",
        "to": "Jenkins",
        "to_description": "A GUI-managed orchestration platform that uses Groovy-based Jenkinsfile pipelines to connect and schedule DevOps jobs across modern codebases and technologies",
        "from": "orchestration"
      },
      {
        "relation": "relatesTo",
        "to": "configuration management",
        "to_description": "An AWS Systems Manager State Manager capability that maintains consistent configuration of EC2 or on-premises instances including server configurations, antivirus definitions, and firewall settings.",
        "from": "orchestration"
      },
      {
        "relation": "relatesTo",
        "to": "Action",
        "to_description": "A record created when a customer, dealer, or rule approves or declines a Finding, tracking the decision, execution status, and audit trail for dispatch to a target system.",
        "from": "action group"
      },
      {
        "relation": "relatesTo",
        "to": "workflow definition file",
        "to_description": "A valid YAML file stored in Amazon S3 that defines workflow behavior using supported AWS operators and Amazon Managed Workflows for Apache Airflow Serverless syntax",
        "from": "action group"
      }
    ]
  }
}