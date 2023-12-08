#!/usr/bin/env python

import sys

from aws_lambda_typing.common import PolicyDocument

if sys.version_info >= (3, 8):
    from typing import Any, Generic, Mapping, Optional, TypedDict, TypeVar
else:
    from typing import Any, Generic, Mapping, Optional, TypeVar

    from typing_extensions import TypedDict


# related: https://github.com/python/mypy/issues/4976#issuecomment-384719025
AuthorizerType = TypeVar('AuthorizerType', bound=Optional[Mapping[str, Any]])


class APIGatewayAuthorizerResponse(Generic[AuthorizerType], TypedDict, total=False):
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
    context: Optional[AuthorizerType]
    usageIdentifierKey: Optional[str]


class APIGatewayAuthorizerResponseV2Simple(Generic[AuthorizerType], TypedDict, total=False):
    """
    https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html#http-api-lambda-authorizer.payload-format-response
    """
    isAuthorized: bool
    context: Optional[AuthorizerType]


class APIGatewayAuthorizerResponseV2IAM(Generic[AuthorizerType], TypedDict, total=False):
    """
    https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html#http-api-lambda-authorizer.payload-format-response
    """
    principalId: str
    policyDocument: PolicyDocument
    context: Optional[AuthorizerType]
