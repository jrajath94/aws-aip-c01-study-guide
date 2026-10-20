{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-view.html",
      "title": "GetAgentActionGroup",
      "context": "Gets information about an action group for an agent.",
      "recommended_sections": [
        "View information about an action group"
      ],
      "sections": [
        "View information about an action group"
      ],
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-add.html",
      "title": "CreateAgentActionGroup",
      "context": "Creates an action group for an agent. An action group represents the actions that an agent can carry out for the customer by defining the APIs that an agent can call and the logic for calling them. To allow your agent to request the user for additional information when trying to complete a task, add an action group with the parentActionGroupSignature field set to AMAZON.UserInput . To allow your agent to generate, run, and troubleshoot code when trying to complete a task, add an action group…",
      "recommended_sections": [
        "Add an action group to your agent in Amazon Bedrock"
      ],
      "sections": [
        "Add an action group to your agent in Amazon Bedrock"
      ],
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/trace-view.html",
      "title": "View the trace",
      "context": "Procedure to view the agent orchestration trace during or after a conversation with an Amazon Bedrock agent",
      "recommended_sections": [
        "View the trace"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-agentactiongroup.html",
      "title": "AgentActionGroup",
      "context": "A CloudFormation resource type that defines an inline Amazon Bedrock agent's action group and its associated executor, schema, and state",
      "recommended_sections": [
        "Properties",
        "AWS::Bedrock::Agent AgentActionGroup"
      ],
      "sections": [
        "AWS::Bedrock::Agent AgentActionGroup",
        "Syntax",
        "JSON",
        "YAML",
        "Properties"
      ],
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html",
      "title": "configure tracing for runtime resources (console)",
      "context": "Procedure to enable trace delivery to CloudWatch for AgentCore agent runtime resources using the console",
      "recommended_sections": [
        "Configure tracing delivery to CloudWatch using the console"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 6,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html",
      "title": "View information about an action group",
      "context": "Retrieve details about a specific action group associated with an Amazon Bedrock agent using the console or API",
      "recommended_sections": [
        "Use action groups to define actions for your agent to perform"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 7,
      "url": "https://docs.aws.amazon.com/cli/latest/reference/bedrock-agent/create-agent-action-group.html",
      "title": "CreateAgentActionGroup",
      "context": "Creates an action group for an agent. An action group represents the actions that an agent can carry out for the customer by defining the APIs that an agent can call and the logic for calling them. To allow your agent to request the user for additional information when trying to complete a task, add an action group with the parentActionGroupSignature field set to AMAZON.UserInput . To allow your agent to generate, run, and troubleshoot code when trying to complete a task, add an action group…",
      "recommended_sections": null,
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 8,
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
    }
  ],
  "facets": null,
  "query_id": "3fe919e0-4cdf-4494-b4dd-8bc488d58702",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "references",
        "to": "Bedrock agent action group",
        "to_description": "A grouping of functions and parameters that a Bedrock agent uses to determine what information to collect from users and what actions to perform",
        "from": "Add an action group to an agent"
      },
      {
        "relation": "references",
        "to": "actionGroupExecutor field",
        "to_description": "A field in CreateAgentActionGroup that configures how the action group handles invocation after eliciting parameters, accepting either a Lambda ARN or RETURN_CONTROL",
        "from": "Add an action group to an agent"
      },
      {
        "relation": "references",
        "to": "CreateAgentActionGroup",
        "to_description": "Creates an action group for an agent. An action group represents the actions that an agent can carry out for the customer by defining the APIs that an agent can call and the logic for calling them. To allow your agent to request the user for additional information when trying to complete a task, add an action group with the parentActionGroupSignature field set to AMAZON.UserInput . To allow your agent to generate, run, and troubleshoot code when trying to complete a task, add an action group…",
        "from": "Add an action group to an agent"
      },
      {
        "relation": "references",
        "to": "parentActionGroupSignature",
        "to_description": "A field that specifies a built-in or computer use action for an action group, such as AMAZON.UserInput, AMAZON.CodeInterpreter, or Anthropic computer use tools",
        "from": "Add an action group to an agent"
      },
      {
        "relation": "references",
        "to": "Return control",
        "to_description": "An action group invocation option that returns the predicted action, parameters, and session information to the calling application via the InvokeAgent response instead of invoking a Lambda function",
        "from": "Add an action group to an agent"
      }
    ]
  }
}