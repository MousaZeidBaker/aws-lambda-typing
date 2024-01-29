#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Any, Dict, Literal, Optional, TypedDict, Union
else:
    from typing import Any, Dict, Optional, Union

    from typing_extensions import Literal, TypedDict


class CallerContext(TypedDict):
    """
    CallerContext

    Attributes:
    ----------:
    awsSdkVersion: str

    clientId: str
    """

    awsSdkVersion: str
    clientId: str


class Request(TypedDict, total=False):
    """
    Request

    Attributes:
    ----------:
    userAttributes: Dict[str, Any]

    clientMetadata: Optional[Dict[str, Any]]
    """

    userAttributes: Dict[str, Any]
    clientMetadata: Optional[Dict[str, Any]]


class Response(TypedDict):
    """
    Response
    """

    pass


class CognitoPostConfirmationCommon(TypedDict):
    """
    CognitoPostConfirmationCommon
    https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools-working-with-aws-lambda-triggers.html#cognito-user-pools-lambda-trigger-syntax-shared

    Attributes:
    ----------
    version: str

    region: str

    userPoolId: str

    userName: str

    callerContext: :py:class:`CallerContext`

    request: :py:class:`Request`

    response: :py:class:`Response`
    """

    version: str
    region: str
    userPoolId: str
    userName: str
    callerContext: CallerContext
    request: Request
    response: Response


class CognitoPostConfirmationForgotPasswordEvent(
    CognitoPostConfirmationCommon,
):
    """
    CognitoPostConfirmationForgotPasswordEvent
    https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-post-confirmation.html

    Attributes:
    ----------
    triggerSource: Literal['PostConfirmation_ConfirmForgotPassword']
    """

    triggerSource: Literal["PostConfirmation_ConfirmForgotPassword"]


class CognitoPostConfirmationSignUpEvent(
    CognitoPostConfirmationCommon,
):
    """
    CognitoPostConfirmationSignUpEvent
    https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-post-confirmation.html

    Attributes:
    ----------
    triggerSource: Literal['PostConfirmation_ConfirmSignUp']
    """

    triggerSource: Literal["PostConfirmation_ConfirmSignUp"]


CognitoPostConfirmationEvent = Union[
    CognitoPostConfirmationForgotPasswordEvent,
    CognitoPostConfirmationSignUpEvent,
]
"""
CognitoPostConfirmationEvent
https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-post-confirmation.html

Attributes:
----------
version: str

triggerSource: Literal[
    "PostConfirmation_ConfirmForgotPassword",
    "PostConfirmation_ConfirmSignUp"
]

region: str

userPoolId: str

userName: str

callerContext: :py:class:`CallerContext`

request: :py:class:`Request`

response: :py:class:`Response`
"""
