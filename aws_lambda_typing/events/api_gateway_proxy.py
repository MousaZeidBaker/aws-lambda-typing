#!/usr/bin/env python

import typing


"""
###############################################################################
###             HTTP API integration payload format version 1.0             ###
###############################################################################
"""


class RequestContextIdentity(typing.TypedDict, total=False):
    """
    RequestContextIdentity https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html

    Attributes:
    ----------
    accountId: typing.Optional[str]

    accessKey: typing.Optional[str]

    apiKey: typing.Optional[str]

    apiKeyId: typing.Optional[str]

    caller: typing.Optional[str]

    cognitoAuthenticationProvider: typing.Optional[str]

    cognitoAuthenticationType: typing.Optional[str]

    cognitoIdentityId: typing.Optional[str]

    cognitoIdentityPoolId: typing.Optional[str]

    principalOrgId: typing.Optional[str]

    sourceIp: str

    clientCert: typing.Optional[typing.Dict]

    user: typing.Optional[str]

    userAgent: typing.Optional[str]

    userArn: typing.Optional[str]
    """

    accountId: typing.Optional[str]
    accessKey: typing.Optional[str]
    apiKey: typing.Optional[str]
    apiKeyId: typing.Optional[str]
    caller: typing.Optional[str]
    cognitoAuthenticationProvider: typing.Optional[str]
    cognitoAuthenticationType: typing.Optional[str]
    cognitoIdentityId: typing.Optional[str]
    cognitoIdentityPoolId: typing.Optional[str]
    principalOrgId: typing.Optional[str]
    sourceIp: str
    clientCert: typing.Optional[typing.Dict]
    user: typing.Optional[str]
    userAgent: typing.Optional[str]
    userArn: typing.Optional[str]


class RequestContextV1(typing.TypedDict, total=False):
    """
    RequestContextV1 https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html

    Attributes:
    ----------
    accountId: str

    apiId: str

    authorizer: typing.Dict

    domainName: typing.Optional[str]

    domainPrefix: typing.Optional[str]

    extendedRequestId: typing.Optional[str]

    httpMethod: str

    identity: :py:class:`RequestContextIdentity`

    path: str

    protocol: str

    requestId: str

    requestTime: typing.Optional[str]

    requestTimeEpoch: int

    resourceId: str

    resourcePath: str

    stage: str
    """

    accountId: str
    apiId: str
    authorizer: typing.Dict
    domainName: typing.Optional[str]
    domainPrefix: typing.Optional[str]
    extendedRequestId: typing.Optional[str]
    httpMethod: str
    identity: RequestContextIdentity
    path: str
    protocol: str
    requestId: str
    requestTime: typing.Optional[str]
    requestTimeEpoch: int
    resourceId: str
    resourcePath: str
    stage: str


class APIGatewayProxyEventV1(typing.TypedDict):
    """
    APIGatewayProxyEventV1 https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html

    HTTP API integration payload format https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html

    Attributes:
    ----------
    resource: str

    path: str

    httpMethod: str

    requestContext: :py:class:`RequestContextV1`

    headers: typing.Dict[str, str]

    multiValueHeaders: typing.Dict[str, typing.List[str]]

    queryStringParameters: typing.Dict[str, str]

    multiValueQueryStringParameters: typing.Dict[str, typing.List[str]]

    pathParameters: typing.Dict[str, str]

    stageVariables: typing.Dict[str, str]

    body: str

    isBase64Encoded: bool
    """

    resource: str
    path: str
    httpMethod: str
    requestContext: RequestContextV1
    headers: typing.Dict[str, str]
    multiValueHeaders: typing.Dict[str, typing.List[str]]
    queryStringParameters: typing.Dict[str, str]
    multiValueQueryStringParameters: typing.Dict[str, typing.List[str]]
    pathParameters: typing.Dict[str, str]
    stageVariables: typing.Dict[str, str]
    body: str
    isBase64Encoded: bool


class APIGatewayProxyResponseV1(typing.TypedDict):
    """
    APIGatewayProxyResponseV1 https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html

    Lambda function response format https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html

    Attributes:
    ----------
    isBase64Encoded: bool

    statusCode: int

    headers: typing.Dict[str, str]

    multiValueHeaders: typing.Dict[str, typing.List[str]]

    body: str
    """

    isBase64Encoded: bool
    statusCode: int
    headers: typing.Dict[str, str]
    multiValueHeaders: typing.Dict[str, typing.List[str]]
    body: str


"""
###############################################################################
###             HTTP API integration payload format version 2.0             ###
###############################################################################
"""


class ClientCert(typing.TypedDict):
    """
    ClientCert

    Attributes:
    ----------
    clientCertPem: str

    subjectDN: str

    issuerDN: str

    serialNumber: str

    validity: typing.Dict
    """

    clientCertPem: str
    subjectDN: str
    issuerDN: str
    serialNumber: str
    validity: typing.Dict


class Authentication(typing.TypedDict):
    """
    Authentication

    Attributes:
    ----------

    clientCert: :py:class:`ClientCert`
    """

    clientCert: ClientCert


class JWT(typing.TypedDict):
    """
    JWT

    Attributes:
    ----------

    claims: typing.Dict[str, str]
    """

    claims: typing.Dict[str, str]


class Authorizer(typing.TypedDict):
    """
    Authorizer

    Attributes:
    ----------

    jwt: :py:class:`JWT`
    """

    jwt: JWT
    scopes: typing.List[str]


class HTTP(typing.TypedDict):
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


class RequestContextV2(typing.TypedDict, total=False):
    """
    RequestContextV2 https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html

    Attributes:
    ----------
    accountId: str

    apiId: str

    authentication: typing.Optional[:py:class:`Authentication`]

    authorizer: typing.Optional[:py:class:`Authorizer`]

    domainName: typing.Optional[str]

    domainPrefix: typing.Optional[str]

    http: :py:class:`HTTP`

    requestId: str

    routeKey: str

    stage: str

    time: str

    timeEpoch: int
    """

    accountId: str
    apiId: str
    authentication: typing.Optional[Authentication]
    authorizer: typing.Optional[Authorizer]
    domainName: typing.Optional[str]
    domainPrefix: typing.Optional[str]
    http: HTTP
    requestId: str
    routeKey: str
    stage: str
    time: str
    timeEpoch: int


class APIGatewayProxyEventV2(typing.TypedDict, total=False):
    """
    APIGatewayProxyEventV2 https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html

    HTTP API integration payload format https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html

    Attributes:
    ----------
    version: str

    routeKey: str

    rawPath: str

    rawQueryString: str

    cookies: typing.Optional[typing.List[str]]

    headers: typing.Dict[str, str]

    queryStringParameters: typing.Dict[str, str]

    requestContext: :py:class:`RequestContextV2`

    body: str

    pathParameters: typing.Dict[str, str]

    isBase64Encoded: bool

    stageVariables: typing.Dict[str, str]
    """

    version: str
    routeKey: str
    rawPath: str
    rawQueryString: str
    cookies: typing.Optional[typing.List[str]]
    headers: typing.Dict[str, str]
    queryStringParameters: typing.Dict[str, str]
    requestContext: RequestContextV2
    body: str
    pathParameters: typing.Dict[str, str]
    isBase64Encoded: bool
    stageVariables: typing.Dict[str, str]


class APIGatewayProxyResponseV2(typing.TypedDict):
    """
    APIGatewayProxyResponseV1 https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html

    Lambda function response format https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html

    Attributes:
    ----------
    cookies: typing.List[str]

    isBase64Encoded: bool

    statusCode: int

    headers: typing.Dict[str, str]

    body: str
    """

    cookies: typing.List[str]
    isBase64Encoded: bool
    statusCode: int
    headers: typing.Dict[str, str]
    body: str
