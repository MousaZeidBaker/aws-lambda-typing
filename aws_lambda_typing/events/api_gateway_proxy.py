#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Dict, List, Optional, TypedDict
else:
    from typing import Dict, List, Optional

    from typing_extensions import TypedDict


"""
###############################################################################
###             HTTP API integration payload format version 1.0             ###
###############################################################################
"""


class RequestContextIdentity(TypedDict, total=False):
    """
    RequestContextIdentity https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html

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
    RequestContextV1 https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html

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
    APIGatewayProxyEventV1 https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html

    HTTP API integration payload format https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html

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
    queryStringParameters: Dict[str, str]
    multiValueQueryStringParameters: Dict[str, List[str]]
    pathParameters: Dict[str, str]
    stageVariables: Dict[str, str]
    body: str
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
    """

    claims: Dict[str, str]


class Authorizer(TypedDict):
    """
    Authorizer

    Attributes:
    ----------

    jwt: :py:class:`JWT`
    """

    jwt: JWT
    scopes: List[str]


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


class RequestContextV2(TypedDict, total=False):
    """
    RequestContextV2 https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html

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
    authorizer: Optional[Authorizer]
    domainName: Optional[str]
    domainPrefix: Optional[str]
    http: HTTP
    requestId: str
    routeKey: str
    stage: str
    time: str
    timeEpoch: int


class APIGatewayProxyEventV2(TypedDict, total=False):
    """
    APIGatewayProxyEventV2 https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html

    HTTP API integration payload format https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html

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
    requestContext: RequestContextV2
    body: str
    pathParameters: Dict[str, str]
    isBase64Encoded: bool
    stageVariables: Dict[str, str]
