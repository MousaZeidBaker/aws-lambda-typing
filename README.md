# AWS Lambda Typing

![build](https://github.com/MousaZeidBaker/aws-lambda-typing/workflows/Build%20and%20Publish/badge.svg)
![test](https://github.com/MousaZeidBaker/aws-lambda-typing/workflows/Test/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![pypi_v](https://img.shields.io/pypi/v/aws-lambda-typing.svg)](https://pypi.org/project/aws-lambda-typing)
[![pypi_dm](https://img.shields.io/pypi/dm/aws-lambda-typing.svg)](https://pypi.org/project/aws-lambda-typing)

A package that provides type hints for AWS Lambda event, context and response
objects. It's a convenient way to get autocomplete and type hints built into
IDEs. Type annotations are not checked at runtime but are only enforced by
third party tools such as type checkers, IDEs, linters, etc.

## Usage
AWS SQS message event example

```python
import aws_lambda_typing as lambda_typing


def handler(event: lambda_typing.SQSEvent, context: lambda_typing.Context) -> None:

    for record in event['Records']:
        print(context.get_remaining_time_in_millis())

        print(record['body'])
```

## Demo
### IDE autocomplete
![ide_autocomplete](https://raw.githubusercontent.com/MousaZeidBaker/aws-lambda-typing/master/media/ide_autocomplete.gif)

### IDE code reference information
![code_reference_information](https://raw.githubusercontent.com/MousaZeidBaker/aws-lambda-typing/master/media/code_reference_information.gif)

## Test
Create and activate virtualenv

`python3 -m venv .venv && source .venv/bin/activate`

Install mypy

`pip install mypy`

Run tests

`mypy tests`

## License
### The MIT License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
