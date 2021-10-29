#!/usr/bin/env python

import sys
from typing import Any

if sys.version_info >= (3, 8):
    from typing import Dict, Literal, TypedDict
else:
    from typing import Dict, Literal

    from typing_extensions import TypedDict


class APIGatewayTokenAuthorizerEvent(TypedDict):
    """
    APIGatewayTokenAuthorizerEvent
    https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-lambda-authorizer-input.html

    Attributes:
    ----------
    type: str

    authorizationToken: str

    methodArn: str
    """

    type: str
    authorizationToken: str
    methodArn: str


class APIGatewayRequestAuthorizerEvent(TypedDict):
    """
    APIGatewayRequestAuthorizerEvent
    https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-lambda-authorizer-input.html

    Attributes:
    ----------
    type: Literal['REQUEST']

    methodArn: str

    resource: str

    path: str

    httpMethod: str

    headers: Dict[str, str]

    queryStringParameters: Dict[str, str]

    pathParameters: Dict[str, str]

    stageVariables: Dict[str, str]

    requestContext: Dict[str, Any]
    """

    type: Literal["REQUEST"]
    methodArn: str
    resource: str
    path: str
    httpMethod: str
    headers: Dict[str, str]
    queryStringParameters: Dict[str, str]
    pathParameters: Dict[str, str]
    stageVariables: Dict[str, str]
    requestContext: Dict[str, Any]
