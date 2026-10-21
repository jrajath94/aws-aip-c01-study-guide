AWS Documentation from https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgentActionGroup.html:

# AgentActionGroup

Contains details of the inline agent's action group.

## Contents

**actionGroupName**
:   The name of the action group.

    Type: String

    Pattern: `([0-9a-zA-Z][_-]?){1,100}`

    Required: Yes

**actionGroupExecutor**
:   The Amazon Resource Name (ARN) of the Lambda function containing the business logic that is carried out upon invoking
    the action or the custom control method for handling the information elicited from the user.

    Type: [ActionGroupExecutor](./API_agent-runtime_ActionGroupExecutor.html) object

    **Note:** This object is a Union. Only one member of this object can be specified or returned.

    Required: No

**apiSchema**
:   Contains either details about the S3 object containing the OpenAPI schema for the action group or the JSON or YAML-formatted
    payload defining the schema. For more information, see [Action group OpenAPI schemas](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-api-schema.html).

    Type: [APISchema](./API_agent-runtime_APISchema.html) object

    **Note:** This object is a Union. Only one member of this object can be specified or returned.

    Required: No

**description**
:   A description of the action group.

    Type: String

    Length Constraints: Minimum length of 1. Maximum length of 200.

    Required: No

**functionSchema**
:   Contains details about the function schema for the action group or the JSON or YAML-formatted payload defining the schema.

    Type: [FunctionSchema](./API_agent-runtime_FunctionSchema.html) object

    **Note:** This object is a Union. Only one member of this object can be specified or returned.

    Required: No

**parentActionGroupSignature**
:   Specify a built-in or computer use action for this action group. If you specify a value, you must leave the `description`, `apiSchema`, and `actionGroupExecutor` fields empty for this action group.

    * To allow your agent to request the user for additional information when trying to complete a task, set this field to `AMAZON.UserInput`.
    * To allow your agent to generate, run, and troubleshoot code when trying to complete a task, set this field to `AMAZON.CodeInterpreter`.
    * To allow your agent to use an Anthropic computer use tool, specify one of the following values.

      ###### Important

      Computer use is a new Anthropic Claude model capability (in beta) available with Anthropic Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only.
      When operating computer use functionality, we recommend taking additional security precautions,
      such as executing computer actions in virtual environments with restricted data access and limited internet connectivity.
      For more information, see [Configure an Amazon Bedrock Agent to complete tasks with computer use tools](https://docs.aws.amazon.com/bedrock/latest/userguide/agent-computer-use.html).

      + `ANTHROPIC.Computer` - Gives the agent permission to use the mouse and keyboard and
        take screenshots.
      + `ANTHROPIC.TextEditor` - Gives the agent permission to view, create and edit files.
      + `ANTHROPIC.Bash` - Gives the agent permission to run commands in a bash shell.

    Type: String

    Valid Values: `AMAZON.UserInput | AMAZON.CodeInterpreter | ANTHROPIC.Computer | ANTHROPIC.Bash | ANTHROPIC.TextEditor`

    Required: No

**parentActionGroupSignatureParams**
:   The configuration settings for a computer use action.

    ###### Important

    Computer use is a new Anthropic Claude model capability (in beta) available with Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. For more information, see [Configure an Amazon Bedrock Agent to complete tasks with computer use tools](https://docs.aws.amazon.com/bedrock/latest/userguide/agent-computer-use.html).

    Type: String to string map

    Key Length Constraints: Minimum length of 0. Maximum length of 100.

    Value Length Constraints: Minimum length of 0. Maximum length of 100.

    Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgentActionGroup)
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgentActionGroup)
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgentActionGroup)