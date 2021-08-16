#!/usr/bin/env python

import abc
import sys

if sys.version_info >= (3, 8):
    from typing import Dict, TypedDict
else:
    from typing import Dict

    from typing_extensions import TypedDict


class Identity(TypedDict):
    """
    Identity

    Attributes:
    ----------
    cognito_identity_id: str
        The authenticated Amazon Cognito identity

    cognito_identity_pool_id: str
        The Amazon Cognito identity pool that authorized the invocation
    """

    cognito_identity_id: str
    cognito_identity_pool_id: str


class Client(TypedDict):
    """
    Client

    Attributes:
    ----------
    installation_id: str

    app_title: str

    app_version_name: str

    app_version_code: str

    app_package_name: str
    """

    installation_id: str
    app_title: str
    app_version_name: str
    app_version_code: str
    app_package_name: str


class ClientContext(TypedDict):
    """
    ClientContext

    Attributes:
    ----------
    client: :py:class:`Client`

    custom: Dict
        A dict of custom values set by the mobile client application

    env: Dict
        A dict of environment information provided by the AWS SDK
    """

    client: Client
    custom: Dict
    env: Dict


class Context(metaclass=abc.ABCMeta):
    """
    Context https://docs.aws.amazon.com/lambda/latest/dg/python-context.html

    A context object is passed to your function by Lambda at runtime. This object provides methods and properties that
    provide information about the invocation, function, and runtime environment.

    Attributes:
    ----------
    function_name: str
        The name of the Lambda function

    function_version: str
        The version of the function

    invoked_function_arn: str
        The Amazon Resource Name (ARN) that's used to invoke the function. Indicates if the invoker specified a version
        number or alias

    memory_limit_in_mb: str
        The amount of memory that's allocated for the function

    aws_request_id: str
        The identifier of the invocation request

    log_group_name: str
        The log group for the function

    log_stream_name: str
        The log stream for the function instance

    identity: :py:class:`Identity`
        Information about the Amazon Cognito identity that authorized the request

    client_context: :py:class:`ClientContext`
        Client context that's provided to Lambda by the client application

    Methods:
    -------
    get_remaining_time_in_millis()
        Returns the number of milliseconds left before the execution times out
    """

    function_name: str
    function_version: str
    invoked_function_arn: str
    memory_limit_in_mb: str
    aws_request_id: str
    log_group_name: str
    log_stream_name: str
    identity: Identity
    client_context: ClientContext

    @staticmethod
    def get_remaining_time_in_millis() -> int:
        """Returns the number of milliseconds left before the execution times out"""
        pass
