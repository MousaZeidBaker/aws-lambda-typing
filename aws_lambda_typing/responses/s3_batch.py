#!/usr/bin/env python

from typing import List, Literal, TypedDict


class S3BatchResponseResult(TypedDict):
    """
    S3BatchRequestTask

    Attributes:
    ----------
    taskId: str

    resultCode: str

    resultString: str
    """

    taskId: str
    resultCode: str
    resultString: str


class S3BatchResponse(TypedDict):
    """
    S3BatchResponse https://docs.aws.amazon.com/lambda/latest/dg/services-s3-batch.html

    Attributes:
    ----------
    invocationSchemaVersion: str

    treatMissingKeysAs: Literal['Succeeded', 'TemporaryFailure', 'PermanentFailure']

    invocationId: str

    results: List[:py:class:`S3BatchResponseResult`]
    """

    invocationSchemaVersion: str
    treatMissingKeysAs: Literal['Succeeded', 'TemporaryFailure', 'PermanentFailure']
    invocationId: str
    results: List[S3BatchResponseResult]
