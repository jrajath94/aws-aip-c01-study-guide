AWS Documentation from https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-agentactiongroup.html:

This is the new *CloudFormation Template Reference Guide*.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Agent AgentActionGroup

Contains details of the inline agent's action group.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ActionGroupExecutor" : ActionGroupExecutor,
  "ActionGroupName" : String,
  "ActionGroupState" : String,
  "ApiSchema" : APISchema,
  "Description" : String,
  "FunctionSchema" : FunctionSchema,
  "ParentActionGroupSignature" : String,
  "SkipResourceInUseCheckOnDelete" : Boolean
}
```

### YAML

```
  ActionGroupExecutor: 
    ActionGroupExecutor
  ActionGroupName: String
  ActionGroupState: String
  ApiSchema: 
    APISchema
  Description: String
  FunctionSchema: 
    FunctionSchema
  ParentActionGroupSignature: String
  SkipResourceInUseCheckOnDelete: Boolean
```

## Properties

`ActionGroupExecutor`
:   The Amazon Resource Name (ARN) of the Lambda function containing the business logic that is carried out upon invoking
    the action or the custom control method for handling the information elicited from the user.

    *Required*: No

    *Type*: [ActionGroupExecutor](./aws-properties-bedrock-agent-actiongroupexecutor.html)

    *Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ActionGroupName`
:   The name of the action group.

    *Required*: Yes

    *Type*: String

    *Pattern*: `^([0-9a-zA-Z][_-]?){1,100}$`

    *Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ActionGroupState`
:   Specifies whether the action group is available for the agent to invoke or not when sending an [InvokeAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html) request.

    *Required*: No

    *Type*: String

    *Allowed values*: `ENABLED | DISABLED`

    *Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApiSchema`
:   Contains either details about the S3 object containing the OpenAPI schema for the action group or the JSON or YAML-formatted
    payload defining the schema. For more information, see [Action group OpenAPI schemas](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-api-schema.html).

    *Required*: No

    *Type*: [APISchema](./aws-properties-bedrock-agent-apischema.html)

    *Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`
:   A description of the action group.

    *Required*: No

    *Type*: String

    *Minimum*: `1`

    *Maximum*: `200`

    *Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FunctionSchema`
:   Contains details about the function schema for the action group or the JSON or YAML-formatted payload defining the schema.

    *Required*: No

    *Type*: [FunctionSchema](./aws-properties-bedrock-agent-functionschema.html)

    *Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParentActionGroupSignature`
:   If this field is set as `AMAZON.UserInput`, the agent can request the user for additional information when trying to complete a task. The `description`, `apiSchema`, and `actionGroupExecutor` fields must be blank for this action group.

    During orchestration, if the agent determines that it needs to invoke an API in an action group, but doesn't have enough information to complete the API request, it will invoke this action group instead and return an [Observation](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Observation.html) reprompting the user for more information.

    *Required*: No

    *Type*: String

    *Allowed values*: `AMAZON.UserInput | AMAZON.CodeInterpreter`

    *Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SkipResourceInUseCheckOnDelete`
:   Specifies whether to delete the resource even if it's in use. By default, this value
    is `false`.

    *Required*: No

    *Type*: Boolean

    *Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)