#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Dict, Optional, TypedDict
else:
    from typing import Dict, Optional

    from typing_extensions import TypedDict


class ELB(TypedDict):
    """
    ELB

    Attributes:
    ----------
    targetGroupArn: str
    """

    targetGroupArn: str


class ALBRequestContext(TypedDict):
    """
    ALBRequestContext

    Attributes:
    ----------
    elb: :py:class:`ELB`
    """

    elb: ELB


class ALBEvent(TypedDict, total=False):
    """
    ALBEvent
    https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html

    Attributes:
    ----------
    requestContext: :py:class:`ALBRequestContext`

    httpMethod: str

    path: str

    queryStringParameters: Dict[str, str]

    headers: Dict[str, str]

    isBase64Encoded: bool

    body: Optional[str]
    """

    requestContext: ALBRequestContext
    httpMethod: str
    path: str
    queryStringParameters: Optional[Dict[str, str]]
    headers: Optional[Dict[str, str]]
    isBase64Encoded: bool
    body: Optional[str]
