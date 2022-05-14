#!/usr/bin/env python

import sys
from typing import Literal

if sys.version_info >= (3, 8):
    from typing import Dict, Optional, TypedDict
else:
    from typing import Dict, Optional

    from typing_extensions import TypedDict


class CognitoCustomMessageCallerContext(TypedDict):
    """
    CognitoCustomMessageCallerContext

    Attributes:
    ----------:
    awsSdk: str
    clientId: str
    """

    awsSdk: str
    clientId: str


class CognitoCustomMessageRequestUserAttributes(TypedDict):
    """
    CognitoCustomMessageRequestUserAttributes

    Attributes:
    ----------:
    phone_number_verified: bool
    email_verified: bool
    """

    phone_number_verified: bool
    email_verified: bool


class CognitoCustomMessageRequest(TypedDict):
    """
    CognitoCustomMessageRequest

    Attributes:
    ----------:
    userAttributes: CognitoCustomMessageRequestUserAttributes
    """


class CognitoCustomMessageResponse(TypedDict):
    """
    CognitoCustomMessageResponse

    Attributes:
    ----------:
    userAttributes: CognitoCustomMessageRequestUserAttributes
    """

    smsMessage: str
    emailMessage: str
    emailSubject: str


class CognitoCustomMessage(TypedDict):
    """
    CognitoCustomMessage
    https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-custom-message.html

    Attributes:
    ----------
    triggerSource: str
    """

    version: int
    triggerSource: Literal[
        "CustomMessage_SignUp",
        "CustomMessage_ResendCode",
        "CustomMessage_ForgotPassword",
        "CustomMessage_VerifyUserAttribute",
    ]
    region: str
    userPoolId: str
    userName: str
    callerContext: CognitoCustomMessageCallerContext
    request: CognitoCustomMessageRequest
    response: CognitoCustomMessageResponse
