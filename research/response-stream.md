Title: Stream the integration response for your proxy integrations in API Gateway

URL Source: https://docs.aws.amazon.com/apigateway/latest/developerguide/response-transfer-mode.html

Markdown Content:
## Select your cookie preferences

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies.   
  
 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Accept Decline Customize

## Customize cookie preferences

We use cookies and similar tools (collectively, "cookies") for the following purposes.

### Essential

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

- [x]  

Allowed

### Performance

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

- [x]  

Allowed

### Functional

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

- [x]  

Allowed

### Advertising

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

- [x]  

Allowed

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the[AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

Cancel Save preferences

## Your privacy choices

We and our advertising partners (“we”) may use information we collect from or about you to show you ads on other websites and online services. Under certain laws, this activity is referred to as “cross-context behavioral advertising” or “targeted advertising.”

To opt out of our use of cookies or similar technologies to engage in these activities, select “Opt out of cross-context behavioral ads” and “Save preferences” below. If you clear your browser cookies or visit this site from a different device or browser, you will need to make your selection again. For more information about cookies and how we use them, read our[Cookie Notice](https://aws.amazon.com/legal/cookies/).

Allow cross-context behavioral ads Opt out of cross-context behavioral ads 

To opt out of the use of other identifiers, such as contact information, for these activities, fill out the form[here](https://pulse.aws/application/ZRPLWLL6?p=0).

For more information about how AWS handles your information, read the[AWS Privacy Notice](https://aws.amazon.com/privacy/).

Cancel Save preferences

## Unable to save cookie preferences

We will only store essential cookies at this time, because we were unable to save your cookie preferences.  
  
If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

Dismiss

[Skip to main content](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-transfer-mode.html#skip-link)

[English](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-transfer-mode.html# "Language Selector. Currently set to: English")

[Preferences](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-transfer-mode.html#)

[Contact Us](https://aws.amazon.com/contact-us/?cmpid=docs_headercta_contactus)

[Feedback](https://docs.aws.amazon.com/feedback/doc-feedback.html?hidden_service_name=API+Gateway&topic_url=https%3A%2F%2Fdocs.aws.amazon.com%2Fapigateway%2Flatest%2Fdeveloperguide%2Fresponse-transfer-mode.html)

[![Image 1: AWS Documentation](https://docs.aws.amazon.com/assets/r/images/aws_logo_light.svg)](https://docs.aws.amazon.com/)

[Get started](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-transfer-mode.html#)

[Service guides](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-transfer-mode.html#)

[Developer tools](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-transfer-mode.html#)

[AI resources](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-transfer-mode.html#)

Search

[Create an AWS Account](https://portal.aws.amazon.com/)

## Amazon API Gateway

### Developer Guide

*   
[What is Amazon API Gateway?](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) 

    *   [API Gateway use cases](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-overview-developer-experience.html)
    *   [API Gateway concepts](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-basic-concept.html)
    *   [Choose between REST APIs and HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html)
    *   [Get started with the REST API console](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-rest-new-console.html)

*   [Prerequisites](https://docs.aws.amazon.com/apigateway/latest/developerguide/setting-up.html)
*   [Get started](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started.html)
*   
[Tutorials and workshops](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-tutorials.html) 

    *   
[REST API tutorials](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-rest-tutorials.html) 

        *   
[Choose a Lambda integration tutorial](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-lambda-integration.html) 

            *   [Tutorial: Create a REST API with a Lambda proxy integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-api-as-simple-proxy-for-lambda.html)
            *   [Tutorial: Create a REST API with a Lambda non-proxy integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-lambda-non-proxy-integration.html)
            *   [Tutorial: Create a REST API with a cross-account Lambda proxy integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-cross-account-lambda-integrations.html)

        *   [Tutorial: Create a REST API by importing an example](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-api-from-example.html)
        *   
[Choose an HTTP integration tutorial](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-http-integrations.html) 

            *   [Tutorial: Create a REST API with an HTTP proxy integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-api-as-simple-proxy-for-http.html)
            *   [Tutorial: Create a REST API with an HTTP non-proxy integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-api-step-by-step.html)

        *   [Tutorial: Create a REST API with a private integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-private-integration.html)
        *   [Tutorial: Create a REST API with an AWS integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-aws-proxy.html)
        *   
[Tutorial: Create a calculator REST API with three integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/integrating-api-with-aws-services-lambda.html) 

            *   [OpenAPI definitions of a sample API for a Lambda function](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-as-lambda-proxy-export-swagger-with-extensions.html)

        *   
[Tutorial: Create a REST API as an Amazon S3 proxy](https://docs.aws.amazon.com/apigateway/latest/developerguide/integrating-api-with-aws-services-s3.html) 

            *   [OpenAPI definitions of a sample API as an Amazon S3 proxy](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-as-s3-proxy-export-swagger-with-extensions.html)
            *   [Call the API using a REST API client](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-as-s3-proxy-test-using-postman.html)

        *   
[Tutorial: Create a REST API as an Amazon Kinesis proxy](https://docs.aws.amazon.com/apigateway/latest/developerguide/integrating-api-with-aws-services-kinesis.html) 

            *   [OpenAPI definitions of a sample API as a Kinesis proxy](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-as-kinesis-proxy-export-swagger-with-extensions.html)

        *   [Tutorial: Create a REST API using AWS SDKs or the AWS CLI](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-api-cli-sdk.html)
        *   [Tutorial: Create a private REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/private-api-tutorial.html)

    *   
[HTTP API tutorials](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-http-tutorials.html) 

        *   [Tutorial: Build a CRUD HTTP API with Lambda and DynamoDB](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-dynamo-db.html)
        *   [Tutorial: Create an HTTP API with a private integration to Amazon ECS](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-private-integration.html)

    *   
[WebSocket API tutorials](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-websocket-tutorials.html) 

        *   [Tutorial: Create a WebSocket chat app](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-chat-app.html)
        *   [Tutorial: Create a WebSocket API with an AWS integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-step-functions-tutorial.html)

*   
[API Gateway REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-rest-api.html) 

    *   
[Develop](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-develop.html) 

        *   
[API Gateway endpoint types](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-endpoint-types.html) 

            *   [Change a public or private API endpoint type](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-api-migration.html)

        *   
[Security policies](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-security-policies.html) 

            *   [Supported security policies](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-security-policies-list.html)
            *   [How to change a security policy](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-security-policies-update.html)

        *   
[IP address types for REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-ip-address-type.html) 

            *   [Change the IP address type of a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-ip-address-type-change.html)

        *   
[Methods](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-method-settings.html) 

            *   [Set up method request](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-settings-method-request.html)
            *   [Set up method response](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-settings-method-response.html)
            *   [Set up method using the console](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-set-up-method-using-console.html)

        *   
[Access control](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html) 

            *   
[Use API Gateway resource policies](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies.html) 

                *   [Access policy language overview for Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-policy-language-overview.html)
                *   [How resource policies affect authorization workflow](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-authorization-flow.html)
                *   [API Gateway resource policy examples](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies-examples.html)
                *   [Create and attach an API Gateway resource policy to an API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies-create-attach.html)
                *   [AWS condition keys that can be used in API Gateway resource policies](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies-aws-condition-keys.html)

            *   
[Use IAM permissions](https://docs.aws.amazon.com/apigateway/latest/developerguide/permissions.html) 

                *   [Control access for invoking an API](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html)
                *   [IAM policy examples for API execution permissions](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-iam-policy-examples-for-api-execution.html)

            *   [Use VPC endpoint policies for private APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-vpc-endpoint-policies.html)
            *   [Using tags to control access to a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-tags.html)
            *   
[Use Lambda authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html) 

                *   [Configure a Lambda authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/configure-api-gateway-lambda-authorization.html)
                *   [Input to a Lambda authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-lambda-authorizer-input.html)
                *   [Output from an API Gateway Lambda authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-lambda-authorizer-output.html)
                *   [Call an API with Lambda authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/call-api-with-api-gateway-lambda-authorization.html)
                *   [Configure a cross-account Lambda authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-lambda-authorizer-cross-account-lambda-authorizer.html)
                *   [Control access based on an identity’s attributes with Verified Permissions](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-lambda-authorizer-verified-permissions.html)

            *   
[Use Amazon Cognito user pool as authorizer for a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html) 

                *   [Create an Amazon Cognito user pool for a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-create-cognito-user-pool.html)
                *   [Integrate a REST API with an Amazon Cognito user pool](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-enable-cognito-user-pool.html)
                *   [Call a REST API integrated with a user pool](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-invoke-api-integrated-with-cognito-user-pool.html)
                *   [Configure cross-account Amazon Cognito authorizer for a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-cross-account-cognito-authorizer.html)
                *   [Create an Amazon Cognito authorizer for a REST API using CloudFormation](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-cognito-authorizer-cfn.html)

        *   
[Integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-integration-settings.html) 

            *   
[Integration request](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-integration-settings-integration-request.html) 

                *   [Basic tasks of an API integration request](https://docs.aws.amazon.com/apigateway/latest/developerguide/integration-request-basic-setup.html)
                *   [Choose an API integration type](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-integration-types.html)
                *   [Set up proxy integrations with a proxy resource](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-set-up-simple-proxy.html)
                *   [Set up integration request using the console](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-method-settings-console.html)

            *   [Integration response](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-integration-settings-integration-response.html)
            *   
[Lambda integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-integrations.html) 

                *   
[Lambda proxy integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html) 

                    *   [Set up Lambda proxy integration for API Gateway using the AWS CLI](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integration-using-cli.html)
                    *   [Set up a proxy resource with Lambda proxy integration with an OpenAPI definition](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-set-up-lambda-proxy-integration-on-proxy-resource.html)

                *   [Set up Lambda custom integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-custom-integrations.html)
                *   [Set up asynchronous invocation of the backend Lambda function](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-integration-async.html)
                *   [Handle Lambda errors in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/handle-errors-in-lambda-integration.html)

            *   [HTTP integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/setup-http-integrations.html)
            *   
[Stream the integration response for your proxy integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-transfer-mode.html) 

                *   [Set up an HTTP proxy integration with payload response streaming](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-streaming-http.html)
                *   
[Set up a Lambda proxy integration with payload response streaming](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-transfer-mode-lambda.html) 

                    *   [Configure a Lambda proxy integration with payload response streaming](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-streaming-lambda-configure.html)

                *   [Troubleshoot issues with response streaming](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-streaming-troubleshoot.html)

            *   
[Private integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/private-integration.html) 

                *   [VPC links V2](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-vpc-links-v2.html)
                *   [Set up a private integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-private-integration.html)
                *   
[Private integration using VPC links V1 (legacy)](https://docs.aws.amazon.com/apigateway/latest/developerguide/vpc-links-v1.html) 

                    *   [Set up a Network Load Balancer for private integrations (legacy)](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-nlb-for-vpclink-using-console.html)
                    *   [Grant permissions for API Gateway to create a VPC link (legacy)](https://docs.aws.amazon.com/apigateway/latest/developerguide/grant-permissions-to-create-vpclink.html)
                    *   [Set up an API with private integrations using AWS CLI (legacy)](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-api-with-vpclink-cli.html)
                    *   [API Gateway accounts used for private integrations (legacy)](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-api-with-vpclink-accounts.html)

            *   
[Mock integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-mock-integration.html) 

                *   [Enable mock integration using the API Gateway console](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-mock-integration-console.html)

        *   
[Request validation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html) 

            *   [Data models for REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings-models.html)
            *   [Set up basic request validation in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-validation-set-up.html)
            *   [AWS CloudFormation template of a sample API with basic request validation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-validation-sample-cloudformation.html)

        *   
[Data transformations](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-data-transformations.html) 

            *   
[Parameter mapping](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-parameter-mapping.html) 

                *   [Parameter mapping examples](https://docs.aws.amazon.com/apigateway/latest/developerguide/request-response-data-mappings.html)
                *   [Parameter mapping source reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-parameter-mapping-sources.html)

            *   
[Mapping template transformations](https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html) 

                *   [Method request behavior for payloads without mapping templates](https://docs.aws.amazon.com/apigateway/latest/developerguide/integration-passthrough-behaviors.html)
                *   [Additional mapping template example](https://docs.aws.amazon.com/apigateway/latest/developerguide/example-photos.html)
                *   [Override your API's request and response parameters and status codes](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-override-request-response-parameters.html)
                *   [Tutorial: Modify the integration request and response for integrations to AWS services](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-data-transformations-in-api-gateway.html)
                *   [Examples using variables for mapping template transformations](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-variable-examples.html)

            *   [Variables for data transformations](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html)

        *   
[Gateway responses](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-gatewayResponse-definition.html) 

            *   [Set up a gateway response for a REST API using the API Gateway console](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-gateway-response-using-the-console.html)
            *   [Set up a gateway response using the API Gateway REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-gateway-response-using-the-api.html)
            *   [Set up gateway response customization in OpenAPI](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-gateway-responses-in-swagger.html)
            *   [Gateway response types for API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/supported-gateway-response-types.html)

        *   
[CORS](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors.html) 

            *   [Enable CORS using the console](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors-console.html)
            *   [Enable CORS using OpenAPI definition](https://docs.aws.amazon.com/apigateway/latest/developerguide/enable-cors-for-resource-using-swagger-importer-tool.html)
            *   [Test CORS for an API Gateway API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-test-cors.html)

        *   
[Binary media types](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-payload-encodings.html) 

            *   [Content type conversions in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-payload-encodings-workflow.html)
            *   [Enabling binary support using the API Gateway console](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-payload-encodings-configure-with-console.html)
            *   [Enabling binary support using the API Gateway REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-payload-encodings-configure-with-control-service-api.html)
            *   [Import and export content encodings for API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-payload-encodings-import-and-export.html)
            *   [Return binary media from a Lambda proxy integration in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/lambda-proxy-binary-media.html)
            *   [Access binary files in Amazon S3 through an API Gateway API](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-content-encodings-examples-image-s3.html)
            *   [Access binary files in Lambda using an API Gateway API](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-content-encodings-examples-image-lambda.html)

        *   
[Invoke](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-call-api.html) 

            *   [Use the console to test a REST API method](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-test-method.html)
            *   [Use a Java SDK generated by API Gateway for a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-call-apigateway-generated-java-sdk.html)
            *   [Use an Android SDK generated by API Gateway for a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-generate-sdk-android.html)
            *   [Use a JavaScript SDK generated by API Gateway for a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-generate-sdk-javascript.html)
            *   [Use a Ruby SDK generated by API Gateway for a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-call-sdk-ruby.html)
            *   [Use iOS SDK generated by API Gateway for a REST API in Objective-C or Swift](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-generate-sdk-ios.html)

        *   
[OpenAPI](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api.html) 

            *   [Import an edge-optimized API](https://docs.aws.amazon.com/apigateway/latest/developerguide/import-edge-optimized-api.html)
            *   [Import a Regional API](https://docs.aws.amazon.com/apigateway/latest/developerguide/import-export-api-endpoints.html)
            *   [Import an OpenAPI file to update an existing API definition](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-update.html)
            *   [Set the OpenAPI basePath property](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-basePath.html)
            *   [AWS variables](https://docs.aws.amazon.com/apigateway/latest/developerguide/import-api-aws-variables.html)
            *   [Errors and warnings from importing your API into API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-errors-warnings.html)
            *   [Export a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-export-api.html)

    *   
[Publish](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-publish.html) 

        *   
[Deploy REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html) 

            *   [Create a deployment](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-deployments.html)
            *   
[Set up a stage](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-stages.html) 

                *   [Add a stage to an Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/mcp-server.html)
                *   [Delete a stage](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-delete-stage.html)
                *   [Set up tags](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-tags.html)
                *   
[Use stage variables](https://docs.aws.amazon.com/apigateway/latest/developerguide/stage-variables.html) 

                    *   [Set up stage variables for REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-set-stage-variables-aws-console.html)
                    *   [Stage variables reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/aws-api-gateway-stage-variables-reference.html)

            *   
[Set up a canary release deployment](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.html) 

                *   [Create a canary release deployment](https://docs.aws.amazon.com/apigateway/latest/developerguide/create-canary-deployment.html)
                *   [Update a canary release](https://docs.aws.amazon.com/apigateway/latest/developerguide/update-canary-deployment.html)
                *   [Promote a canary release](https://docs.aws.amazon.com/apigateway/latest/developerguide/promote-canary-deployment.html)
                *   [Turn off a canary release](https://docs.aws.amazon.com/apigateway/latest/developerguide/delete-canary-deployment.html)

            *   [Redeploy a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/updating-api.html)

        *   
[Custom domain names](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html) 

            *   [Get certificates ready in AWS Certificate Manager](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-specify-certificate-for-custom-domain-name.html)
            *   [Set up a Regional custom domain name](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html)
            *   [Set up an edge-optimized custom domain name in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-edge-optimized-custom-domain-name.html)
            *   [Migrate custom domain names](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-migrate.html)
            *   
[Send traffic to your APIs through your custom domain name in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-routing-mode.html) 

                *   [Set the routing mode for your custom domain name](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-routing-mode.html)
                *   
[Routing rules](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-routing-rules.html) 

                    *   [Examples of how API Gateway evaluates routing rules](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-routing-rules-examples.html)
                    *   [How to use routing rules](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-routing-rules-use.html)
                    *   [Recreate an API mapping using routing rules](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-routing-rules-recreate-api-mapping.html)
                    *   [Troubleshooting issues with routing rules](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-routing-rules-troubleshoot.html)

                *   [API mappings](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-mappings.html)

            *   [IP address types for custom domain names in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-custom-domain-ip-address-type.html)
            *   [Choose a security policy](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html)
            *   [Disable the default endpoint](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-disable-default-endpoint.html)
            *   [DNS failover](https://docs.aws.amazon.com/apigateway/latest/developerguide/dns-failover.html)

    *   
[Optimize](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-optimize.html) 

        *   [Cache settings](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html)
        *   
[Content encoding](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-gzip-compression-decompression.html) 

            *   [Enable payload compression for an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-enable-compression.html)
            *   [Call a method with a compressed payload](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-make-request-with-compressed-payload.html)
            *   [Receive a response with a compressed payload](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-receive-response-with-compressed-payload.html)

    *   
[Distribute](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-distribute.html) 

        *   
[Usage plans](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html) 

            *   [Choose an API key source in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-key-source.html)
            *   [API Gateway API key file format](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-key-file-format.html)
            *   [Set up API keys for REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-setup-api-keys.html)
            *   [Set up usage plans for REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-usage-plans.html)
            *   [Maintain a usage plan for REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-usage-plan-manage-usage.html)
            *   [Create and configure API keys and usage plans with CloudFormation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-key-usage-plan-cfn.html)
            *   [Configure a method to use API keys with an OpenAPI definition](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-key-usage-plan-oas.html)
            *   [Test usage plans for REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-usage-plan-test-with-postman.html)
            *   [Call a method using an API key](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-key-call.html)

        *   
[API documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html) 

            *   [Representation of API documentation in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api-content-representation.html)
            *   [Document an API using the API Gateway console](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api-quick-start-with-console.html)
            *   [Publish API documentation using the API Gateway console](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-documenting-api-with-console.html)
            *   [Document an API using the API Gateway REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api-quick-start-with-restapi.html)
            *   [Publish API documentation using the API Gateway REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api-quick-start-publishing.html)
            *   [Import API documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api-quick-start-import-export.html)
            *   [Control access to API documentation in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api-content-provision-and-consumption.html)

        *   
[SDK generation](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-generate-sdk.html) 

            *   [Simple calculator Lambda function](https://docs.aws.amazon.com/apigateway/latest/developerguide/simple-calc-nodejs-lambda-function.html)
            *   [Simple calculator API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/simple-calc-lambda-api.html)
            *   [Simple calculator API OpenAPI definition](https://docs.aws.amazon.com/apigateway/latest/developerguide/simple-calc-lambda-api-swagger-definition.html)
            *   [Generate the Java SDK of an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/generate-java-sdk-of-an-api.html)
            *   [Generate the Android SDK of an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/generate-android-sdk-of-an-api.html)
            *   [Generate the iOS SDK of an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/generate-ios-sdk-of-an-api.html)
            *   [Generate the JavaScript SDK of a REST API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/generate-javascript-sdk-of-an-api.html)
            *   [Generate the Ruby SDK of an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/generate-ruby-sdk-of-an-api.html)
            *   [Generate SDKs for an API using AWS CLI commands in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-generate-sdk-cli.html)

        *   [Sell your APIs as SaaS](https://docs.aws.amazon.com/apigateway/latest/developerguide/sell-api-as-saas-on-aws-marketplace.html)

    *   
[Protect](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-protect.html) 

        *   [Require client certificates](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-mutual-tls.html)
        *   
[Backend client certificates](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-backend-authentication.html) 

            *   [How it works](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-backend-auth-overview.html)
            *   [Use your own ACM certificate](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-acm-client-certificates.html)
            *   [API Gateway-generated certificates](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-client-side-ssl-authentication.html)
            *   [Supported certificate authorities for HTTP and HTTP proxy integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-supported-certificate-authorities-for-http-endpoints.html)

        *   [AWS WAF](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-aws-waf.html)
        *   [Throttling](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)
        *   
[Private REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html) 

            *   [Create a private API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-api-create.html)
            *   
[Custom domain names for private APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains.html) 

                *   [API providers and API consumers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains-associations.html)
                *   [Tutorial: Create and invoke a custom domain name for private APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains-tutorial.html)
                *   
[Working with cross-account private custom domain names](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains-other-accounts.html) 

                    *   [API provider: Share your private custom domain name using AWS RAM](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains-provider-share.html)
                    *   [API provider: Stop sharing a private custom domain name using AWS RAM](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains-provider-stop-sharing.html)
                    *   [API provider: Share your private custom domain name using the API Gateway AWS CLI](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains-provider-share-cli.html)
                    *   [API consumer: Associate your VPC endpoint with a private custom domain name shared with you](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains-consumer-create.html)
                    *   [API consumer: Delete your domain name access association with a private custom domain name](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains-consumer-delete-domain-name-access-association.html)

                *   [Create a custom domain name for private APIs using CloudFormation](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains-cfn.html)

            *   [Invoke a private API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-api-test-invoke-url.html)

    *   
[Monitor](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-monitor.html) 

        *   
[CloudWatch metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/monitoring-cloudwatch.html) 

            *   [Amazon API Gateway dimensions and metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-metrics-and-dimensions.html)
            *   [View metrics with the API dashboard](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-dashboard.html)
            *   [View metrics in the CloudWatch console](https://docs.aws.amazon.com/apigateway/latest/developerguide/metrics_dimensions_view_in_cloud_watch.html)
            *   [View log event in the CloudWatch console](https://docs.aws.amazon.com/apigateway/latest/developerguide/view-cloudwatch-log-events-in-cloudwatch-console.html)
            *   [Monitoring tools in AWS for API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/monitoring_automated_manual.html)

        *   
[CloudWatch logs](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html) 

            *   
[Execution logging](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-execution-logging.html) 

                *   [Create a log delivery](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-create-log-delivery.html)
                *   [Verify log delivery](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-verify-log-delivery.html)
                *   [Delete a log delivery](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-delete-log-delivery.html)

            *   
[Access logging](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-access-logging.html) 

                *   [Firehose](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-logging-to-kinesis.html)
                *   [Variables for access logging for API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-variables-for-access-logging.html)

        *   
[X-Ray](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-xray.html) 

            *   [Set up AWS X-Ray](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-enabling-xray.html)
            *   [Use AWS X-Ray service maps and trace views](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-using-xray-maps.html)
            *   [Configure AWS X-Ray sampling rules](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-configuring-xray-sampling-rules.html)
            *   [X-Ray traces](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-understanding-xray-traces.html)

*   
[API Gateway portals](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals.html) 

    *   
[Portal product](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-portal-product.html) 

        *   [Create a portal product](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-create-portal-product.html)
        *   [Create a product REST endpoint](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-create-product-rest-endpoint.html)
        *   [Create a product page](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-create-product-page.html)
        *   [Update a portal product](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-update-portal-product.html)
        *   [Update a product REST endpoint](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-update-product-endpoint.html)
        *   [Update product page](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-update-product-page.html)
        *   
[Share portal products](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-share-resources.html) 

            *   [Share your portal product with a portal owner](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-share-products.html)
            *   [Add a shared portal product to your portal](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-use-shared-products.html)

        *   [Enable try it for a product REST endpoint in your portal](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-try-it.html)
        *   [Delete a portal product](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-delete-product.html)

    *   [Create a portal](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-create-portal.html)
    *   [Update a portal](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-update-portal.html)
    *   [Preview a portal](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-prview-portal.html)
    *   [Publish a portal](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-publish-portal.html)
    *   [Use a portal](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-use-portal.html)
    *   [Disable a portal](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-disable-portal.html)
    *   [Delete a portal](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-delete-portal.html)

*   
[API Gateway HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html) 

    *   
[Develop](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop.html) 

        *   [Routes](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-routes.html)
        *   [IP address types for HTTP APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-ip-address-type.html)
        *   
[Access control](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-access-control.html) 

            *   [Lambda authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html)
            *   [JWT authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html)
            *   [IAM authorization](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-access-control-iam.html)

        *   
[Integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations.html) 

            *   [AWS Lambda integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html)
            *   [HTTP integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-http.html)
            *   
[AWS service integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services.html) 

                *   [AWS service integrations reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services-reference.html)

            *   [Private integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-private.html)

        *   [CORS](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html)
        *   [Parameter mapping](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html)
        *   
[OpenAPI](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-open-api.html) 

            *   [Export](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-export.html)

    *   
[Publish](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-publish.html) 

        *   
[Stages](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-stages.html) 

            *   [Use stage variables for HTTP APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-stages.stage-variables.html)
            *   [API Gateway stage variables reference for HTTP APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-stages.stage-variables-reference.html)

        *   [Security policy for HTTP APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-ciphers.html)
        *   
[Custom domain names](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-custom-domain-names.html) 

            *   [API mappings](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-mappings.html)
            *   [Disable the default endpoint](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-disable-default-endpoint.html)
            *   [IP address types for custom domain names for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-custom-domain-names-ip-address-type.html)

    *   
[Protect](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-protect.html) 

        *   [Throttling](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-throttling.html)
        *   [Mutual TLS](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-mutual-tls.html)

    *   
[Monitor](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-monitor.html) 

        *   [Metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-metrics.html)
        *   
[Logging](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-logging.html) 

            *   [Logging variables](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-logging-variables.html)

    *   
[Troubleshooting](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-troubleshooting.html) 

        *   [Lambda integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-troubleshooting-lambda.html)
        *   [JWT authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-troubleshooting-jwt.html)

*   
[API Gateway WebSocket APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html) 

    *   
[Overview of WebSocket APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-overview.html) 

        *   [Manage connected users and client apps](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-route-keys-connect-disconnect.html)
        *   [Invoke your backend integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-routes-integrations.html)
        *   [WebSocket selection expressions](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html)

    *   
[Develop](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-develop.html) 

        *   [Create and configure](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-create-empty-api.html)
        *   [IP address types for WebSocket APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-ip-address-type.html)
        *   
[Routes](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-develop-routes.html) 

            *   [Set up WebSocket API route responses](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-route-response.html)
            *   [Subprotocol support](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-connect-route-subprotocol.html)

        *   
[Access control](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-control-access.html) 

            *   [Control access to WebSocket APIs with IAM authorization](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-control-access-iam.html)
            *   [Control access to WebSocket APIs with AWS Lambda REQUEST authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-lambda-auth.html)

        *   
[Integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-integrations.html) 

            *   [Integration request](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-integration-requests.html)
            *   [Integration responses](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-integration-responses.html)

        *   [Request validation](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-request-validation.html)
        *   
[Data transformations](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-data-transformations.html) 

            *   [Data mapping](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-data-mapping.html)
            *   [WebSocket mapping template reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-mapping-template-reference.html)

        *   [Binary media types](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-develop-binary-media-types.html)
        *   
[Invoke](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api.html) 

            *   [Use wscat to connect to a WebSocket API and send messages to it](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-wscat.html)
            *   [Use @connections commands in your backend service](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html)

    *   
[Publish](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-publish.html) 

        *   [Stages](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-stages.html)
        *   [Deploy a WebSocket API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-set-up-websocket-deployment.html)
        *   [Security policy for WebSocket APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-ciphers.html)
        *   
[Custom domain names](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-custom-domain-names.html) 

            *   [API mappings](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-mappings.html)
            *   [IP address types for custom domain names for WebSocket APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-custom-domain-names-ip-address-type.html)
            *   [Disable the default endpoint](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-disable-default-endpoint.html)

    *   [Protect](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-protect.html)
    *   
[Monitor](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-monitor.html) 

        *   [Metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-logging.html)
        *   [Logging](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-logging.html)

*   [API Gateway ARNs](https://docs.aws.amazon.com/apigateway/latest/developerguide/arn-format-reference.html)
*   
[OpenAPI extensions](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html) 

    *   [x-amazon-apigateway-any-method](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-any-method.html)
    *   [x-amazon-apigateway-cors](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-cors-configuration.html)
    *   [x-amazon-apigateway-api-key-source](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-api-key-source.html)
    *   [x-amazon-apigateway-auth](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-auth.html)
    *   [x-amazon-apigateway-authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-authorizer.html)
    *   [x-amazon-apigateway-authtype](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-authtype.html)
    *   [x-amazon-apigateway-binary-media-type](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-binary-media-types.html)
    *   [x-amazon-apigateway-documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-documentation.html)
    *   [x-amazon-apigateway-endpoint-access-mode](https://docs.aws.amazon.com/apigateway/latest/developerguide/openapi-extensions-endpoint-access-mode.html)
    *   [x-amazon-apigateway-endpoint-configuration](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-endpoint-configuration.html)
    *   [x-amazon-apigateway-gateway-responses](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-gateway-responses.html)
    *   [x-amazon-apigateway-gateway-responses.gatewayResponse](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-gateway-responses.gatewayResponse.html)
    *   [x-amazon-apigateway-gateway-responses.responseParameters](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-gateway-responses.responseParameters.html)
    *   [x-amazon-apigateway-gateway-responses.responseTemplates](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-gateway-responses.responseTemplates.html)
    *   [x-amazon-apigateway-importexport-version](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-extensions-importexport-version.html)
    *   [x-amazon-apigateway-integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration.html)
    *   [x-amazon-apigateway-integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-extensions-integrations.html)
    *   [x-amazon-apigateway-integration.requestTemplates](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-requestTemplates.html)
    *   [x-amazon-apigateway-integration.requestParameters](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-requestParameters.html)
    *   [x-amazon-apigateway-integration.responses](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-responses.html)
    *   [x-amazon-apigateway-integration.response](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-response.html)
    *   [x-amazon-apigateway-integration.responseTemplates](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-responseTemplates.html)
    *   [x-amazon-apigateway-integration.responseParameters](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-responseParameters.html)
    *   [x-amazon-apigateway-integration.tlsConfig](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-extensions-integration-tls-config.html)
    *   [x-amazon-apigateway-minimum-compression-size](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-openapi-minimum-compression-size.html)
    *   [x-amazon-apigateway-policy](https://docs.aws.amazon.com/apigateway/latest/developerguide/openapi-extensions-policy.html)
    *   [x-amazon-apigateway-request-validator](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-request-validator.html)
    *   [x-amazon-apigateway-request-validators](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-request-validators.html)
    *   [x-amazon-apigateway-request-validators.requestValidator](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-request-validators.requestValidator.html)
    *   [x-amazon-apigateway-security-policy](https://docs.aws.amazon.com/apigateway/latest/developerguide/openapi-extensions-security-policy.html)
    *   [x-amazon-apigateway-tag-value](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-openapi-extensions-x-amazon-apigateway-tag-value.html)

*   
[Security](https://docs.aws.amazon.com/apigateway/latest/developerguide/security.html) 

    *   
[Data protection](https://docs.aws.amazon.com/apigateway/latest/developerguide/data-protection.html) 

        *   [Data encryption](https://docs.aws.amazon.com/apigateway/latest/developerguide/data-protection-encryption.html)
        *   [Internetwork traffic privacy](https://docs.aws.amazon.com/apigateway/latest/developerguide/security-traffic-privacy.html)

    *   
[Identity and access management](https://docs.aws.amazon.com/apigateway/latest/developerguide/security-iam.html) 

        *   [How Amazon API Gateway works with IAM](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)
        *   [Identity-based policy examples](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_id-based-policy-examples.html)
        *   [Resource-based policy examples](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_resource-based-policy-examples.html)
        *   [Troubleshooting](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_troubleshoot.html)
        *   [Using service-linked roles](https://docs.aws.amazon.com/apigateway/latest/developerguide/using-service-linked-roles.html)

    *   
[Logging and monitoring](https://docs.aws.amazon.com/apigateway/latest/developerguide/security-monitoring.html) 

        *   [Working with CloudTrail](https://docs.aws.amazon.com/apigateway/latest/developerguide/cloudtrail.html)
        *   [Working with AWS Config](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-config.html)

    *   [Compliance validation](https://docs.aws.amazon.com/apigateway/latest/developerguide/compliance-validation.html)
    *   [Resilience](https://docs.aws.amazon.com/apigateway/latest/developerguide/disaster-recovery-resiliency.html)
    *   [Infrastructure security](https://docs.aws.amazon.com/apigateway/latest/developerguide/infrastructure-security.html)
    *   [Configuration and vulnerability analysis](https://docs.aws.amazon.com/apigateway/latest/developerguide/vulnerability-analysis.html)
    *   [Best practices](https://docs.aws.amazon.com/apigateway/latest/developerguide/security-best-practices.html)

*   
[Tagging](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-tagging.html) 

    *   [API Gateway resources that can be tagged](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-tagging-supported-resources.html)
    *   [Attribute-based access control](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-tagging-iam-policy.html)

*   [API references](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-ref.html)
*   
[Quotas and important notes](https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html) 

    *   [REST API quotas](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-execution-service-limits-table.html)
    *   [HTTP API quotas](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-quotas.html)
    *   [Portal quotas](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-portal-quotas.html)
    *   [WebSocket API quotas](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-execution-service-websocket-limits-table.html)
    *   [Important notes](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-known-issues.html)

*   [Document history](https://docs.aws.amazon.com/apigateway/latest/developerguide/history.html)

1.   [Documentation](https://docs.aws.amazon.com/index.html) 
2.   ...           
3.   [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/index.html) 
4.   Developer Guide 

1.   [Documentation](https://docs.aws.amazon.com/index.html) 
2.   [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/index.html) 
3.   Developer Guide 

# Stream the integration response for your proxy integrations in API Gateway

[PDF](https://docs.aws.amazon.com/pdfs/apigateway/latest/developerguide/apigateway-dg.pdf#response-transfer-mode)

[RSS](https://docs.aws.amazon.com/apigateway/latest/developerguide/amazon-apigateway-release-notes.rss)

[Markdown](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-transfer-mode.md "Download Markdown")

Agent Setup Up-to-date AWS docs, tested procedures, and IAM guardrails via a single setup prompt in your AI coding agent.

- [x] Focus mode

Stream the integration response for your proxy integrations in API Gateway - Amazon API Gateway

[](https://docs.aws.amazon.com/pdfs/apigateway/latest/developerguide/apigateway-dg.pdf#response-transfer-mode "Open PDF")

[Documentation](https://docs.aws.amazon.com/index.html)[Amazon API Gateway](https://docs.aws.amazon.com/apigateway/index.html)[Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)

[Considerations for response payload streaming](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-transfer-mode.html#response-transfer-mode-considerations)

You can configure your proxy integration to control how API Gateway returns your integration response. By default, API Gateway waits to receive the complete response before beginning transmission. However, if you set your integration's response transfer mode to `STREAM`, API Gateway doesn't wait for a response to be completely computed before sending it to the client. Response streaming works for all REST API endpoint types.

Use response streaming for the following use cases:

*   Lower the time-to-first-byte (TTFB) for generative AI applications like chatbots.

*   Stream large image, video, or music files without using an S3 pre-signed URL.

*   Perform long-running operations while reporting incremental progress like server-sent events (SSE).

*   Exceed API Gateway's 10 MB response payload limit.

*   Exceed API Gateway's 29 second timeout limit without requesting an integration timeout limit increase.

*   Receive a binary payload without configuring the binary media types.

## Considerations for response payload streaming

The following considerations might impact your use of response payload streaming:

*   You can only use response payload streaming for `HTTP_PROXY` or `AWS_PROXY` integration types. This includes Lambda proxy integrations and private integrations that use `HTTP_PROXY` integrations.

*   The default transfer mode setting is `BUFFERED`. To use response streaming you must change the response transfer mode to `STREAM`.

*   Response streaming is only supported for REST APIs.

*   Request streaming isn't supported.

*   You can stream your response for up to 15 minutes.

*   Your streams are subject to idle timeouts. For Regional or private endpoints, the timeout is 5 minutes. For edge-optimized endpoints, the timeout is 30 seconds.

*   If you use response streaming for a Regional REST API with your own CloudFront distribution, you can achieve an idle time out greater than 30 seconds by increasing the response timeout of your CloudFront distribution. For more information, see [Response timeout](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html#DownloadDistValuesOriginResponseTimeout).

*   When the response transfer mode is set to `STREAM`, API Gateway can’t support features that require buffering the entire integration response. Because of this, the following features aren't supported with response streaming:

    *   Endpoint caching

    *   Content encoding. If you want to compress your integration response, do this in your integration.

    *   Response transformation with VTL

*   Within each streaming response, the first 10MB of response payload is not subject to any bandwidth restrictions. Response payload data exceeding 10MB is restricted to 2MB/s.

*   When the connection between the client and API Gateway or between API Gateway and Lambda is closed due to timeout, the Lambda function might continue to execute. For more information, see [Configure Lambda function timeout](https://docs.aws.amazon.com/lambda/latest/dg/configuration-timeout.html).

*   Response streaming incurs a cost. For more information, see [API Gateway Pricing](https://aws.amazon.com/api-gateway/pricing/).

[Document Conventions](https://docs.aws.amazon.com/general/latest/gr/docconventions.html)

HTTP integration

Set up an HTTP proxy integration with payload response streaming

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

*   
### On this page

    1.   [Considerations for response payload streaming](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-transfer-mode.html#response-transfer-mode-considerations)

*   ### Related resources [Amazon API Gateway API Reference](https://docs.aws.amazon.com/apigateway/api-reference/index.html) [AWS CLI commands for Amazon API Gateway](https://docs.aws.amazon.com/cli/latest/reference/apigateway/) [SDKs & Tools](https://aws.amazon.com/tools/)    
*   Did this page help you?   Yes No       [Provide feedback](https://docs.aws.amazon.com/feedback/doc-feedback.html?hidden_service_name=API+Gateway&topic_url=https%3A%2F%2Fdocs.aws.amazon.com%2Fapigateway%2Flatest%2Fdeveloperguide%2Fresponse-transfer-mode.html)     

#### Next topic:

[Set up an HTTP proxy integration with payload response streaming](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-streaming-http.html)

#### Previous topic:

[HTTP integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/setup-http-integrations.html)

## Get Started

[AWS Hands-On Tutorials](https://aws.amazon.com/getting-started/hands-on/)

[AWS Solutions Library](https://aws.amazon.com/solutions/)

[AWS Decision Guides](https://docs.aws.amazon.com/decision-guides/)

## Service Guides

[Choosing a generative AI service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/genai-guide.html)

[AWS service guides](https://docs.aws.amazon.com/#products)

[AWS CLI Tutorials on GitHub](https://github.com/aws-samples/sample-developer-tutorials)

## Developer Tools

[AWS Code Example Library](https://docs.aws.amazon.com/code-library/latest/ug/what-is-code-library.html)

[AWS CLI](https://docs.aws.amazon.com/cli/)

[AWS Builder Center](https://builder.aws.com/)

[AWS Developer Tools Blog](https://aws.amazon.com/blogs/developer/)

## Helpful Links

[Download the AWS Docs MCP Server](https://github.com/awslabs/mcp/tree/main/src/aws-documentation-mcp-server)

[Sign into the AWS Console](https://console.aws.amazon.com/)

[AWS re:Post](https://repost.aws/)

[Privacy](https://aws.amazon.com/privacy)

[Site terms](https://aws.amazon.com/terms)

[Cookie preferences](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-transfer-mode.html#)

 © 2026, Amazon Web Services, Inc. or its affiliates. All rights reserved.

English

Language selector

Top
