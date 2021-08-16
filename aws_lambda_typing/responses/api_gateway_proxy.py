#!/usr/bin/env python

from typing import Dict, List, TypedDict

"""
###############################################################################
###             Lambda function response format version 1.0             ###
###############################################################################
"""


class APIGatewayProxyResponseV1(TypedDict):
    """
    APIGatewayProxyResponseV1 https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html

    Lambda function response format https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html

    Attributes:
    ----------
    isBase64Encoded: bool

    statusCode: int

    headers: Dict[str, str]

    multiValueHeaders: Dict[str, List[str]]

    body: str
    """

    isBase64Encoded: bool
    statusCode: int
    headers: Dict[str, str]
    multiValueHeaders: Dict[str, List[str]]
    body: str


"""
###############################################################################
###             Lambda function response format version 2.0             ###
###############################################################################
"""


class APIGatewayProxyResponseV2(TypedDict):
    """
    APIGatewayProxyResponseV1 https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html

    Lambda function response format https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html

    Attributes:
    ----------
    cookies: List[str]

    isBase64Encoded: bool

    statusCode: int

    headers: Dict[str, str]

    body: str
    """

    cookies: List[str]
    isBase64Encoded: bool
    statusCode: int
    headers: Dict[str, str]
    body: str
