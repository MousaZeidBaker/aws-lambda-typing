#!/usr/bin/env python

import typing


class S3BatchResponseResult(typing.TypedDict):
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


class S3BatchResponse(typing.TypedDict):
    """
    S3BatchResponse https://docs.aws.amazon.com/lambda/latest/dg/services-s3-batch.html

    Attributes:
    ----------
    invocationSchemaVersion: str

    treatMissingKeysAs: typing.Literal['Succeeded', 'TemporaryFailure', 'PermanentFailure']

    invocationId: str

    results: typing.List[:py:class:`S3BatchResponseResult`]
    """

    invocationSchemaVersion: str
    treatMissingKeysAs: typing.Literal['Succeeded', 'TemporaryFailure', 'PermanentFailure']
    invocationId: str
    results: typing.List[S3BatchResponseResult]
