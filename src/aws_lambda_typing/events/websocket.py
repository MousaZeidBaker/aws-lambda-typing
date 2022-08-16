#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Any, Dict, List, Literal, TypedDict
else:
    from typing import Any, Dict, List

    from typing_extensions import Literal, TypedDict


class Identity(TypedDict, total=False):
    """
    Identity

    Attributes:
    ----------
    accountId: str

    apiKey: str

    apiKeyId: str

    caller: str

    cognitoAuthenticationProvider: str

    cognitoAuthenticationType: str

    cognitoIdentityId: str

    cognitoIdentityPoolId: str

    sourceIp: str

    user: str

    userAgent: str

    userArn: str
    """

    accountId: str
    apiKey: str
    apiKeyId: str
    caller: str
    cognitoAuthenticationProvider: str
    cognitoAuthenticationType: str
    cognitoIdentityId: str
    cognitoIdentityPoolId: str
    sourceIp: str
    user: str
    userAgent: str
    userArn: str


class Error(TypedDict, total=False):
    """
    Error

    Attributes:
    ----------
    message: str

    messageString: str

    validationErrorString: str
    """

    message: str
    messageString: str
    validationErrorString: str


class RequestContextRequiredAttributes(TypedDict):
    """
    RequestContextRequiredAttributes required attributes only
    https://peps.python.org/pep-0589/#totality

    Attributes:
    ----------
    connectionId: str

    connectedAt: int

    domainName: str

    eventType: Literal['CONNECT', 'DISCONNECT', 'MESSAGE']

    routeKey: str

    requestId: str

    extendedRequestId: str

    apiId: str

    authorizer: Dict[str, Any]

    requestTime: str

    requestTimeEpoch: int

    messageDirection: Literal['IN', 'OUT']

    stage: str

    identity: :py:class:`Identity`
    """

    connectionId: str
    connectedAt: int
    domainName: str
    eventType: Literal["CONNECT", "DISCONNECT", "MESSAGE"]
    routeKey: str
    requestId: str
    extendedRequestId: str
    apiId: str
    authorizer: Dict[str, Any]
    requestTime: str
    requestTimeEpoch: int
    messageDirection: Literal["IN", "OUT"]
    stage: str
    identity: Identity


class RequestContext(RequestContextRequiredAttributes, total=False):
    """
    Attributes:
    ----------
    messageId: str - exists when eventType == 'MESSAGE'
    error: :py:class:`Error`
    status: int
    """

    messageId: str
    error: Error
    status: int


class WebSocketEventCommonAttributes(TypedDict):
    """
    Attributes:
    ----------
    requestContext: :py:class:`RequestContext`

    isBase64Encoded: bool
    """

    requestContext: RequestContext
    isBase64Encoded: bool


class WebSocketConnectEvent(WebSocketEventCommonAttributes):
    """
    WebSocketEvent https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-mapping-template-reference.html
    as sent to the $connect and $disconnect routes.

    Attributes:
    ----------
    headers: Dict[str, str]

    multiValueHeaders: Dict[str, List[str]]

    queryStringParameters: Dict[str, str]

    multiValueQueryStringParameters: Dict[str, List[str]]
    """

    headers: Dict[str, str]
    multiValueHeaders: Dict[str, List[str]]
    queryStringParameters: Dict[str, str]
    multiValueQueryStringParameters: Dict[str, List[str]]


class WebSocketRouteEvent(WebSocketEventCommonAttributes):
    """
    WebSocketEvent https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-mapping-template-reference.html
    as send to custom routes and the $default route.

    Attributes:
    ----------
    body: str
    """

    body: str
