# cloudwatch-sns-lambda-teams
This repository contains the architecture diagram and Lambda function implementation for a system that automatically sends notifications to Microsoft Teams whenever a CloudWatch alarm is triggered. The solution leverages AWS SNS to invoke the Lambda function, which then formats and sends the alarm details to a  Teams channel.

We cannot hit a webhook which accepts the content type of application/json in sns topic , because the SNS only supports application/text type, so we are using lambda.

The lambda sends a post request to a custom url generated in power automate, Feel free to change the payload and you can change it for your need.