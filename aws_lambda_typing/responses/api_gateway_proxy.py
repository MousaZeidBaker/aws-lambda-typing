#!/usr/bin/env python

import typing


"""
###############################################################################
###             Lambda function response format version 1.0             ###
###############################################################################
"""


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
###             Lambda function response format version 2.0             ###
###############################################################################
"""


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
