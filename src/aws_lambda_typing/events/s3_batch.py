#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import List, Literal, Optional, TypedDict
else:
    from typing import List, Optional

    from typing_extensions import Literal, TypedDict

S3BatchResponseResultCode = Literal[
    "Succeeded",
    "TemporaryFailure",
    "PermanentFailure",
]


class S3BatchRequestJob(TypedDict):
    """
    S3BatchRequestJob

    Attributes:
    ----------
    id: str
    """

    id: str


class S3BatchRequestTask(TypedDict):
    """
    S3BatchRequestTask

    Attributes:
    ----------
    taskId: str

    s3Key: str

    s3VersionId: Optional[str]

    s3BucketArn: str
    """

    taskId: str
    s3Key: str
    s3VersionId: Optional[str]
    s3BucketArn: str


class S3BatchEvent(TypedDict):
    """
    S3BatchEvent
    https://docs.aws.amazon.com/lambda/latest/dg/services-s3-batch.html

    Attributes:
    ----------
    invocationSchemaVersion: str

    invocationId: str

    job: :py:class:`S3BatchRequestJob`

    tasks: List[:py:class:`S3BatchRequestTask`]
    """

    invocationSchemaVersion: str
    invocationId: str
    job: S3BatchRequestJob
    tasks: List[S3BatchRequestTask]


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
