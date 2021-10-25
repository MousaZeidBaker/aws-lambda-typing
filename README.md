# AWS Lambda Typing

![build](https://github.com/MousaZeidBaker/aws-lambda-typing/workflows/Publish/badge.svg)
![test](https://github.com/MousaZeidBaker/aws-lambda-typing/workflows/Test/badge.svg)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![python_version](https://img.shields.io/badge/python-%3E=3.6-blue.svg)
[![pypi_v](https://img.shields.io/pypi/v/aws-lambda-typing.svg)](https://pypi.org/project/aws-lambda-typing)
[![pypi_dm](https://img.shields.io/pypi/dm/aws-lambda-typing.svg)](https://pypi.org/project/aws-lambda-typing)

A package that provides type hints for AWS Lambda event, context and response
objects. It's a convenient way to get autocomplete and type hints built into
IDEs. Type annotations are not checked at runtime but are only enforced by third
party tools such as type checkers, IDEs, linters, etc.

##### Table of Contents
- [Usage](#usage)
- [Demo](#demo)
- [Types](#types)
  - [Context](#context)
  - [Events](#events)
  - [Responses](#responses)
- [Test](#test)
- [Contributing](#contributing)
- [Issues](#issues)

## Usage
### Example: AWS SQS event

```python
from aws_lambda_typing import context as context_, events


def handler(event: events.SQSEvent, context: context_.Context) -> None:
    for record in event['Records']:
        print(record['body'])

    print(context.get_remaining_time_in_millis())

    message: events.sqs.SQSMessage

```

## Demo
### IDE autocomplete
![ide_autocomplete](https://raw.githubusercontent.com/MousaZeidBaker/aws-lambda-typing/master/media/ide_autocomplete.gif)

### IDE code reference information
![code_reference_information](https://raw.githubusercontent.com/MousaZeidBaker/aws-lambda-typing/master/media/code_reference_information.gif)

## Types
### Context
- Context

### Events
- APIGatewayProxyEventV1
- APIGatewayProxyEventV2
- CloudWatchEventsMessageEvent
- CloudWatchLogsEvent
- CodeCommitMessageEvent
- CodePipelineEvent
- ConfigEvent
- DynamoDBStreamEvent
- KinesisFirehoseEvent
- KinesisStreamEvent
- MQEvent
- S3Event
- S3BatchEvent
- SESEvent
- SNSEvent
- SQSEvent

### Responses
- APIGatewayProxyResponseV1
- APIGatewayProxyResponseV2
- S3BatchResponse

## Develop
Activate virtual environment
```shell
poetry shell
```

Install dependencies
```shell
poetry install --remove-untracked
```

Install git hooks
```shell
pre-commit install --hook-type pre-commit
```

Run tests
```shell
pytest tests
```

Run linter
```shell
flake8 .
```

Format code
```shell
black .
```

Sort imports
```shell
isort .
```

## Contributing
Contributions are welcome via pull requests.

## Issues
If you encounter any problems, please file an
[issue](https://github.com/MousaZeidBaker/aws-lambda-typing/issues) along with a
detailed description.
