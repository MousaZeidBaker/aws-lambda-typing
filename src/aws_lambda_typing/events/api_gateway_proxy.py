#!/usr/bin/env python

import sys
from typing import Dict, Generic, List, Optional

# TypedDict generic support added in 3.11
if sys.version_info >= (3, 11):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

from aws_lambda_typing.responses.api_gateway_authorizer import AuthorizerType


"""
###############################################################################
###             HTTP API integration payload format version 1.0             ###
###############################################################################
"""


class RequestContextIdentity(TypedDict, total=False):
    """
    RequestContextIdentity
    https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html

    Attributes:
    ----------
    accountId: Optional[str]

    accessKey: Optional[str]

    apiKey: Optional[str]

    apiKeyId: Optional[str]

    caller: Optional[str]

    cognitoAuthenticationProvider: Optional[str]

    cognitoAuthenticationType: Optional[str]

    cognitoIdentityId: Optional[str]

    cognitoIdentityPoolId: Optional[str]

    principalOrgId: Optional[str]

    sourceIp: str

    clientCert: Optional[Dict]

    user: Optional[str]

    userAgent: Optional[str]

    userArn: Optional[str]
    """

    accountId: Optional[str]
    accessKey: Optional[str]
    apiKey: Optional[str]
    apiKeyId: Optional[str]
    caller: Optional[str]
    cognitoAuthenticationProvider: Optional[str]
    cognitoAuthenticationType: Optional[str]
    cognitoIdentityId: Optional[str]
    cognitoIdentityPoolId: Optional[str]
    principalOrgId: Optional[str]
    sourceIp: str
    clientCert: Optional[Dict]
    user: Optional[str]
    userAgent: Optional[str]
    userArn: Optional[str]


class RequestContextV1(TypedDict, total=False):
    """
    RequestContextV1
    https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html

    Attributes:
    ----------
    accountId: str

    apiId: str

    authorizer: Dict

    domainName: Optional[str]

    domainPrefix: Optional[str]

    extendedRequestId: Optional[str]

    httpMethod: str

    identity: :py:class:`RequestContextIdentity`

    operationName: str

    path: str

    protocol: str

    requestId: str

    requestTime: Optional[str]

    requestTimeEpoch: int

    resourceId: str

    resourcePath: str

    stage: str
    """

    accountId: str
    apiId: str
    authorizer: Dict
    domainName: Optional[str]
    domainPrefix: Optional[str]
    extendedRequestId: Optional[str]
    httpMethod: str
    identity: RequestContextIdentity
    operationName: Optional[str]
    path: str
    protocol: str
    requestId: str
    requestTime: Optional[str]
    requestTimeEpoch: int
    resourceId: str
    resourcePath: str
    stage: str


class APIGatewayProxyEventV1(TypedDict):
    """
    APIGatewayProxyEventV1
    https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html

    HTTP API integration payload format
    https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html

    Attributes:
    ----------
    resource: str

    path: str

    httpMethod: str

    requestContext: :py:class:`RequestContextV1`

    headers: Dict[str, str]

    multiValueHeaders: Dict[str, List[str]]

    queryStringParameters: Dict[str, str]

    multiValueQueryStringParameters: Dict[str, List[str]]

    pathParameters: Dict[str, str]

    stageVariables: Dict[str, str]

    body: str

    isBase64Encoded: bool
    """

    resource: str
    path: str
    httpMethod: str
    requestContext: RequestContextV1
    headers: Dict[str, str]
    multiValueHeaders: Dict[str, List[str]]
    queryStringParameters: Optional[Dict[str, str]]
    multiValueQueryStringParameters: Optional[Dict[str, List[str]]]
    pathParameters: Optional[Dict[str, str]]
    stageVariables: Optional[Dict[str, str]]
    body: Optional[str]
    isBase64Encoded: bool


"""
###############################################################################
###             HTTP API integration payload format version 2.0             ###
###############################################################################
"""


class ClientCert(TypedDict):
    """
    ClientCert

    Attributes:
    ----------
    clientCertPem: str

    subjectDN: str

    issuerDN: str

    serialNumber: str

    validity: Dict
    """

    clientCertPem: str
    subjectDN: str
    issuerDN: str
    serialNumber: str
    validity: Dict


class Authentication(TypedDict):
    """
    Authentication

    Attributes:
    ----------

    clientCert: :py:class:`ClientCert`
    """

    clientCert: ClientCert


class JWT(TypedDict):
    """
    JWT

    Attributes:
    ----------

    claims: Dict[str, str]
    scopes: List[str]
    """

    claims: Dict[str, str]
    scopes: List[str]


class JWTAuthorizer(TypedDict):
    """
    Authorizer

    Attributes:
    ----------

    jwt: :py:class:`JWT`
    """

    jwt: JWT


class Authorizer(JWTAuthorizer):
    """Deprecated. Prefer JWTAuthorizer or custom TypedDict instead."""
    pass


class HTTP(TypedDict):
    """
    HTPP

    Attributes:
    ----------

    method: str

    path: str

    protocol: str

    sourceIp: str

    userAgent: str
    """

    method: str
    path: str
    protocol: str
    sourceIp: str
    userAgent: str


class RequestContextV2(Generic[AuthorizerType], TypedDict, total=False):
    """
    RequestContextV2
    https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html

    Attributes:
    ----------
    accountId: str

    apiId: str

    authentication: Optional[:py:class:`Authentication`]

    authorizer: Optional[:py:class:`Authorizer`]

    domainName: Optional[str]

    domainPrefix: Optional[str]

    http: :py:class:`HTTP`

    requestId: str

    routeKey: str

    stage: str

    time: str

    timeEpoch: int
    """

    accountId: str
    apiId: str
    authentication: Optional[Authentication]
    authorizer: AuthorizerType
    domainName: Optional[str]
    domainPrefix: Optional[str]
    http: HTTP
    requestId: str
    routeKey: str
    stage: str
    time: str
    timeEpoch: int


class APIGatewayProxyEventV2(Generic[AuthorizerType], TypedDict, total=False):
    """
    APIGatewayProxyEventV2
    https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html

    HTTP API integration payload format
    https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html

    Attributes:
    ----------
    version: str

    routeKey: str

    rawPath: str

    rawQueryString: str

    cookies: Optional[List[str]]

    headers: Dict[str, str]

    queryStringParameters: Dict[str, str]

    requestContext: :py:class:`RequestContextV2`

    body: str

    pathParameters: Dict[str, str]

    isBase64Encoded: bool

    stageVariables: Dict[str, str]
    """

    version: str
    routeKey: str
    rawPath: str
    rawQueryString: str
    cookies: Optional[List[str]]
    headers: Dict[str, str]
    queryStringParameters: Dict[str, str]
    requestContext: RequestContextV2[AuthorizerType]
    body: str
    pathParameters: Dict[str, str]
    isBase64Encoded: bool
    stageVariables: Dict[str, str]
