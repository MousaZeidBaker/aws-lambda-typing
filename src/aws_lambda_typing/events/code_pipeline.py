#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import List, Optional, TypedDict
else:
    from typing import List, Optional

    from typing_extensions import TypedDict


class Configuration(TypedDict):
    """
    Configuration

    Attributes:
    ----------
    FunctionName: str

    UserParameters: str
    """

    FunctionName: str
    UserParameters: str


class ActionConfiguration(TypedDict):
    """
    ActionConfiguration

    Attributes:
    ----------
    configuration: :py:class:`Configuration`
    """

    configuration: Configuration


class S3Location(TypedDict):
    """
    S3Location

    Attributes:
    ----------
    bucketName: str

    objectKey: str
    """

    bucketName: str
    objectKey: str


class ArtifactLocation(TypedDict):
    """
    ArtifactLocation

    Attributes:
    ----------
    type: str S3 locations will use the "S3" type.

    s3Location: :py:class:`S3Location`
    """

    type: str
    s3Location: S3Location


class Artifact(TypedDict):
    """
    Artifact

    Attributes:
    ----------
    name: str

    revision: Optional[str]

    location: :py:class:`ArtifactLocation`
    """

    name: str
    revision: Optional[str]
    location: ArtifactLocation


class ArtifactCredentials(TypedDict):
    """
    ArtifactCredentials

    Attributes:
    ----------
    accessKeyId: str

    secretAccessKey: str

    sessionToken: str

    expirationTime: int
    """

    accessKeyId: str
    secretAccessKey: str
    sessionToken: str
    expirationTime: int


class EncryptionKey(TypedDict):
    """
    EncryptionKey

    Attributes:
    ----------
    id: str

    type: str
    """

    id: str
    type: str


class Data(TypedDict, total=False):
    """
    Data

    Attributes:
    ----------
    actionConfiguration: :py:class:`ActionConfiguration`

    inputArtifacts: List[:py:class:`Artifact`]

    outputArtifacts: List[:py:class:`Artifact`]

    artifactCredentials: :py:class:`ArtifactCredentials`

    encryptionKey: Optional[:py:class:`EncryptionKey`]

    continuationToken: Optional[str]
    """

    actionConfiguration: ActionConfiguration
    inputArtifacts: List[Artifact]
    outputArtifacts: List[Artifact]
    artifactCredentials: ArtifactCredentials
    encryptionKey: Optional[EncryptionKey]
    continuationToken: Optional[str]


class CodePipelineJob(TypedDict):
    """
    CodePipelineJob
    https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-invoke-lambda-function.html

    Attributes:
    ----------
    id: str

    accountId: str

    data: :py:class:`Data`
    """

    id: str
    accountId: str
    data: Data


CodePipelineEvent = TypedDict(
    "CodePipelineEvent", {"CodePipeline.job": CodePipelineJob}
)
"""
CodePipelineEvent
https://docs.aws.amazon.com/lambda/latest/dg/services-codepipeline.html

Attributes:
----------
CodePipeline.job: :py:class:`CodePipelineJob`
"""
