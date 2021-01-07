#!/usr/bin/env python

import typing


class S3BatchRequestJob(typing.TypedDict):
    """
    S3BatchRequestJob

    Attributes:
    ----------
    id: str
    """

    id: str


class S3BatchRequestTask(typing.TypedDict):
    """
    S3BatchRequestTask

    Attributes:
    ----------
    taskId: str

    s3Key: str

    s3VersionId: typing.Optional[str]

    s3BucketArn: str
    """

    taskId: str
    s3Key: str
    s3VersionId: typing.Optional[str]
    s3BucketArn: str


class S3BatchEvent(typing.TypedDict):
    """
    S3BatchEvent https://docs.aws.amazon.com/lambda/latest/dg/services-s3-batch.html

    Attributes:
    ----------
    invocationSchemaVersion: str

    invocationId: str

    job: :py:class:`S3BatchRequestJob`

    tasks: typing.List[:py:class:`S3BatchRequestTask`]
    """

    invocationSchemaVersion: str
    invocationId: str
    job: S3BatchRequestJob
    tasks: typing.List[S3BatchRequestTask]


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
