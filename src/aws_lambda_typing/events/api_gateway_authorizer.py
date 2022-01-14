#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Any, Dict, Literal, TypedDict
else:
    from typing import Any, Dict

    from typing_extensions import Literal, TypedDict


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
