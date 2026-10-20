AWS Documentation from https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html:

# Use action groups to define actions for your agent to perform

###### Note

Amazon Bedrock Agents (now Amazon Bedrock Agents Classic) is no longer open to new customers. For capabilities similar to Bedrock Agents Classic, explore [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-get-started-cli.html). Existing customers can continue to use the service as normal. For more information, see [Amazon Bedrock Agents Classic maintenance mode](./agents-classic-maintenance-mode.html).

An action group defines actions that the agent can help the user perform. For example, you could define an action group called `BookHotel` that helps users carry out actions that you can define such as:

* `CreateBooking` – Helps users book a hotel.
* `GetBooking` – Helps users get information about a hotel they booked.
* `CancelBooking` – Helps users cancel a booking.

You create an action group by performing the following steps:

1. Define the parameters and information that the agent must elicit from the user for each action in the action group to be carried out.
2. Decide how the agent handles the parameters and information that it receives from the user and where it sends the information it elicits from the user.

To learn more about the components of an action group and how to create the action group after you set it up, select from the following topics:

###### Topics

* [Define actions in the action group](./action-define.html)
* [Handle fulfillment of the action](./action-handle.html)
* [Add an action group to your agent in Amazon Bedrock](./agents-action-add.html)
* [View information about an action group](./agents-action-view.html)
* [Modify an action group](./agents-action-edit.html)
* [Delete an action group](./agents-action-delete.html)