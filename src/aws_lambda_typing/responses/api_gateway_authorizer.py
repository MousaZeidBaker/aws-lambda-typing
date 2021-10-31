#!/usr/bin/env python

import sys

from aws_lambda_typing.common import PolicyDocument

if sys.version_info >= (3, 8):
    from typing import Any, Dict, Optional, TypedDict
else:
    from typing import Any, Dict, Optional

    from typing_extensions import TypedDict


class APIGatewayAuthorizerResponse(TypedDict, total=False):
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
    context: Optional[Dict[str, Any]]
    usageIdentifierKey: Optional[str]
