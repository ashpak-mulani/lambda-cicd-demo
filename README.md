# Summary

This repo can be used as a generic start to applications that will be built and provisioned using CodePipeline.


# Prerequisites

Rename the files to what you need for your project.

Currently supports Python 3.7, see [Python](src/example-function/README.md)

# Usage

When you want to build applications on AWS, you can use services such as Lambda, Kinesis or ElasticSearch. To provision these, you can use CloudFormation. The pipeline will be expecting a `Parent` CloudFormation Template.


| Filename | Location | Description |
|-----------|------------|----------|
| project-skeleton.cf-template.yml | templates/ | Use this file as the parent CloudFormation template that specifies the resources required by the application, such as Kinesis, SNS etc.
| project-example-ecs-dev.eu-central-1.cf-config.json | ci/ | Use this file to specify parameters that the CloudFormation template will use to build the stack.
| src/ | ./ | The location to place all Lambda applications, scripts or other code, using a subdirectory for each. The handler defined in the CFN template should refer to these |
| test/ | integration/ | The location to place all Lambda integration tests |
| test/ | unit/ | The location to place all Lambda unit tests |
