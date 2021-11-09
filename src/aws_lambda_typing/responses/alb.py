#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Dict, Optional, TypedDict
else:
    from typing import Dict, Optional

    from typing_extensions import TypedDict


class ALBResponse(TypedDict, total=False):
    """
    ALBResponse
    https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html

    Attributes:
    ----------
    isBase64Encoded: Optional[bool]

    statusCode: int

    statusDescription: str

    headers: Optional[Dict[str, str]]

    body: Optional[str]
    """

    isBase64Encoded: Optional[bool]
    statusCode: int
    statusDescription: str
    headers: Optional[Dict[str, str]]
    body: Optional[str]
