#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Any, Dict, List, Literal, TypedDict
else:
    from typing import Any, Dict, List

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


class APIGatewayHTTPRequestInfo(TypedDict):
    method: str
    path: str
    protocol: str
    sourceIp: str
    userAgent: str


class APIGatewayHTTPRequestContext(TypedDict):
    accountId: str
    apiId: str
    authentication: Dict[str, Any]
    domainName: str
    domainPrefix: str
    http: APIGatewayHTTPRequestInfo
    requestId: str
    routeKey: str
    stage: str
    time: str
    timeEpoch: int


class APIGatewayHTTPAuthorizerEventV2(TypedDict):
    """
    APIGatewayHTTPAuthorizerEvent
    https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html#http-api-lambda-authorizer.payload-format
    """

    version: Literal["2.0"]
    type: Literal["REQUEST"]
    identitySource: List[str]
    routeArn: str
    routeKey: str
    rawPath: str
    rawQueryString: str
    cookies: List[str]
    headers: Dict[str, str]
    queryStringParameters: Dict[str, str]
    requestContext: APIGatewayHTTPRequestContext
    pathParameters: Dict[str, str]
    stageVariables: Dict[str, str]
