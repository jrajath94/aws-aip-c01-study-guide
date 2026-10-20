{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html",
      "title": "Use multi-agent collaboration with Amazon Bedrock Agents",
      "context": "Configure a supervisor agent and associate collaborator agents to enable multi-agent collaboration in Amazon Bedrock",
      "recommended_sections": [
        "Use multi-agent collaboration with Amazon Bedrock Agents"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/create-multi-agent-collaboration.html",
      "title": "Create multi-agent collaboration",
      "context": "End-to-end procedure to set up a multi-agent collaboration team in Amazon Bedrock by creating collaborator agents, configuring a supervisor agent, associating collaborators, and deploying",
      "recommended_sections": [
        "Create multi-agent collaboration"
      ],
      "sections": [
        "Create multi-agent collaboration"
      ],
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/disable-multi-agents-collaboration.html",
      "title": "PrepareAgent",
      "context": "Creates a DRAFT version of the agent that can be used for internal testing.",
      "recommended_sections": null,
      "sections": [
        "Disable a multi-agent collaboration"
      ],
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/saga-orchestration-patterns.html",
      "title": "collaborator agent",
      "context": "A specialized agent in Bedrock's multi-agent collaboration model that contributes specific expertise under the direction of a supervisor agent",
      "recommended_sections": [
        "Supervisor"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/disassociate-collaborator-agent.html",
      "title": "DisassociateAgentCollaborator",
      "context": "Disassociates an agent collaborator.",
      "recommended_sections": null,
      "sections": [
        "Disassociate collaborator agent"
      ],
      "metadata": null
    },
    {
      "rank_order": 6,
      "url": "https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/architecture-overview.html",
      "title": "supervisor agent",
      "context": "An orchestration agent in the multi-agent pattern that creates local instances of specialized agents, delegates work to them, and aggregates their results into a final response.",
      "recommended_sections": [
        "Workflow Builder use case"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 7,
      "url": "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-agentcollaborator.html",
      "title": "AWS::Bedrock::Agent",
      "context": "Definition of AWS::Bedrock::Agent Resource Type",
      "recommended_sections": [
        "AWS::Bedrock::Agent AgentCollaborator"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 8,
      "url": "https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/agent-builder-1.html",
      "title": "supervisor agent",
      "context": "An orchestration agent in the multi-agent pattern that creates local instances of specialized agents, delegates work to them, and aggregates their results into a final response.",
      "recommended_sections": [
        "Workflow Builder"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 9,
      "url": "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Collaborator.html",
      "title": "Collaborator",
      "context": "A user added to an EMR Studio Workspace who can view and work in the Workspace in real time alongside the owner",
      "recommended_sections": null,
      "sections": [
        "Collaborator",
        "Contents",
        "See Also"
      ],
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "ec1067e1-14af-4754-929b-483e8f41f6b5",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "references",
        "to": "multi-agent collaboration",
        "to_description": "Amazon Bedrock Agents capability that allows developers to build, deploy, and manage multiple specialized agents working together to address complex business workflows.",
        "from": "Use multi-agent collaboration with Amazon Bedrock Agents"
      },
      {
        "relation": "hasChild",
        "to": "online mortgage assistant",
        "to_description": "Demonstrates a multi-agent collaboration setup where a supervisor agent routes mortgage-related questions to specialized collaborator agents",
        "from": "Use multi-agent collaboration with Amazon Bedrock Agents"
      },
      {
        "relation": "references",
        "to": "hierarchical collaboration model",
        "to_description": "A structural pattern in multi-agent collaboration where a supervisor agent coordinates one or more collaborator agents to respond to user queries",
        "from": "Use multi-agent collaboration with Amazon Bedrock Agents"
      },
      {
        "relation": "references",
        "to": "collaborator agent",
        "to_description": "A specialized agent in Bedrock's multi-agent collaboration model that contributes specific expertise under the direction of a supervisor agent",
        "from": "Use multi-agent collaboration with Amazon Bedrock Agents"
      },
      {
        "relation": "references",
        "to": "supervisor agent",
        "to_description": "An orchestration agent in the multi-agent pattern that creates local instances of specialized agents, delegates work to them, and aggregates their results into a final response.",
        "from": "Use multi-agent collaboration with Amazon Bedrock Agents"
      }
    ]
  }
}