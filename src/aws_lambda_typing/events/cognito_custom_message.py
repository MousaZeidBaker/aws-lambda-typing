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

    codeParameter: str

    usernameParameter: str

    clientMetadata: Optional[Dict[str, Any]]
    """

    userAttributes: Dict[str, Any]
    codeParameter: str
    usernameParameter: str
    clientMetadata: Optional[Dict[str, Any]]


class Response(TypedDict):
    """
    Response

    Attributes:
    ----------:
    smsMessage: str

    emailMessage: str

    emailSubject: str
    """

    smsMessage: str
    emailMessage: str
    emailSubject: str


class CognitoCustomMessageCommon(TypedDict):
    """
    CognitoCustomMessageCommon
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


class CognitoCustomMessageSignUpEvent(
    CognitoCustomMessageCommon,
):
    """
    CognitoCustomMessageSignUpEvent
    https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-custom-message.html

    Attributes:
    ----------
    triggerSource: Literal['CustomMessage_SignUp']
    """

    triggerSource: Literal["CustomMessage_SignUp"]


class CognitoCustomMessageAdminCreateUserEvent(
    CognitoCustomMessageCommon,
):
    """
    CognitoCustomMessageAdminCreateUserEvent
    https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-custom-message.html

    Attributes:
    ----------
    triggerSource: Literal['CustomMessage_AdminCreateUser']
    """

    triggerSource: Literal["CustomMessage_AdminCreateUser"]


class CognitoCustomMessageResendCodeEvent(
    CognitoCustomMessageCommon,
):
    """
    CognitoCustomMessageResendCodeEvent
    https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-custom-message.html

    Attributes:
    ----------
    triggerSource: Literal['CustomMessage_ResendCode']
    """

    triggerSource: Literal["CustomMessage_ResendCode"]


class CognitoCustomMessageForgotPasswordEvent(
    CognitoCustomMessageCommon,
):
    """
    CognitoCustomMessageForgotPasswordEvent
    https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-custom-message.html

    Attributes:
    ----------
    triggerSource: Literal['CustomMessage_ForgotPassword']
    """

    triggerSource: Literal["CustomMessage_ForgotPassword"]


class CognitoCustomMessageUpdateUserAttributeEvent(
    CognitoCustomMessageCommon,
):
    """
    CognitoCustomMessageUpdateUserAttributeEvent
    https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-custom-message.html

    Attributes:
    ----------
    triggerSource: Literal['CustomMessage_UpdateUserAttribute']
    """

    triggerSource: Literal["CustomMessage_UpdateUserAttribute"]


class CognitoCustomMessageVerifyUserAttributeEvent(
    CognitoCustomMessageCommon,
):
    """
    CognitoCustomMessageVerifyUserAttributeEvent
    https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-custom-message.html

    Attributes:
    ----------
    triggerSource: Literal['CustomMessage_VerifyUserAttribute']
    """

    triggerSource: Literal["CustomMessage_VerifyUserAttribute"]


class CognitoCustomMessageAuthenticationEvent(
    CognitoCustomMessageCommon,
):
    """
    CognitoCustomMessageAuthenticationEvent
    https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-custom-message.html

    Attributes:
    ----------
    triggerSource: Literal['CustomMessage_Authentication']
    """

    triggerSource: Literal["CustomMessage_Authentication"]


CognitoCustomMessageEvent = Union[
    CognitoCustomMessageSignUpEvent,
    CognitoCustomMessageAdminCreateUserEvent,
    CognitoCustomMessageResendCodeEvent,
    CognitoCustomMessageForgotPasswordEvent,
    CognitoCustomMessageUpdateUserAttributeEvent,
    CognitoCustomMessageVerifyUserAttributeEvent,
    CognitoCustomMessageAuthenticationEvent,
]
"""
CognitoCustomMessageEvent
https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-custom-message.html

Attributes:
----------
version: str

triggerSource: Literal[
    "CustomMessage_SignUp",
    "CustomMessage_AdminCreateUser",
    "CustomMessage_ResendCode",
    "CustomMessage_ForgotPassword",
    "CustomMessage_UpdateUserAttribute",
    "CustomMessage_VerifyUserAttribute",
    "CustomMessage_Authentication"
]

region: str

userPoolId: str

userName: str

callerContext: :py:class:`CallerContext`

request: :py:class:`Request`

response: :py:class:`Response`
"""
