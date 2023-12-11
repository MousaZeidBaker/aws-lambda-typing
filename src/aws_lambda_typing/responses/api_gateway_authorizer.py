#!/usr/bin/env python

import sys
from typing import Any, Generic, Mapping, Optional, TypeVar

# TypedDict generic support added in 3.11
if sys.version_info >= (3, 11):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

from aws_lambda_typing.common import PolicyDocument


# related: https://github.com/python/mypy/issues/4976#issuecomment-384719025
LambdaAuthorizerType = TypeVar('LambdaAuthorizerType', bound=Optional[Mapping[str, Any]])


class APIGatewayAuthorizerResponse(Generic[LambdaAuthorizerType], TypedDict, total=False):
    """
    APIGatewayAuthorizerResponse
    https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-lambda-authorizer-output.html

    Attributes:
    ----------
    principalId: str

    policyDocument: :py:class:`PolicyDocument`

    context: Optional[Dict[str, Any]]

    usageIdentifierKey: Optional[str]
    """

    principalId: str
    policyDocument: PolicyDocument
    context: Optional[LambdaAuthorizerType]
    usageIdentifierKey: Optional[str]


class APIGatewayAuthorizerResponseV2Simple(Generic[LambdaAuthorizerType], TypedDict, total=False):
    """
    https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html#http-api-lambda-authorizer.payload-format-response
    """
    isAuthorized: bool
    context: Optional[LambdaAuthorizerType]


class APIGatewayAuthorizerResponseV2IAM(Generic[LambdaAuthorizerType], TypedDict, total=False):
    """
    https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html#http-api-lambda-authorizer.payload-format-response
    """
    principalId: str
    policyDocument: PolicyDocument
    context: Optional[LambdaAuthorizerType]
