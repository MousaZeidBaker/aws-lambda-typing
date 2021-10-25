#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Dict, List, TypedDict
else:
    from typing import Dict, List

    from typing_extensions import TypedDict


"""
###############################################################################
###             Lambda function response format version 1.0                 ###
###############################################################################
"""


class APIGatewayProxyResponseV1(TypedDict):
    """
    APIGatewayProxyResponseV1
    https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html

    Lambda function response format
    https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html

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
###             Lambda function response format version 2.0                 ###
###############################################################################
"""


class APIGatewayProxyResponseV2(TypedDict, total=False):
    """
    APIGatewayProxyResponseV2
    https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html

    Lambda function response format
    https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html

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
