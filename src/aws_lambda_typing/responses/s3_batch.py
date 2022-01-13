#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import List, Literal, TypedDict
else:
    from typing import List

    from typing_extensions import Literal, TypedDict

S3BatchResponseResultCode = Literal[
    "Succeeded",
    "TemporaryFailure",
    "PermanentFailure",
]


class S3BatchResponseResult(TypedDict):
    """
    S3BatchRequestTask

    Attributes:
    ----------
    taskId: str

    resultCode: Literal['Succeeded', 'TemporaryFailure', 'PermanentFailure']

    resultString: str
    """

    taskId: str
    resultCode: S3BatchResponseResultCode
    resultString: str


class S3BatchResponse(TypedDict):
    """
    S3BatchResponse
    https://docs.aws.amazon.com/lambda/latest/dg/services-s3-batch.html

    Attributes:
    ----------
    invocationSchemaVersion: str

    treatMissingKeysAs: Literal['Succeeded', 'TemporaryFailure',
    'PermanentFailure']

    invocationId: str

    results: List[:py:class:`S3BatchResponseResult`]
    """

    invocationSchemaVersion: str
    treatMissingKeysAs: S3BatchResponseResultCode
    invocationId: str
    results: List[S3BatchResponseResult]
