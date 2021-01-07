#!/usr/bin/env python

import typing


class Configuration(typing.TypedDict):
    """
    Configuration

    Attributes:
    ----------
    FunctionName: str

    UserParameters: str
    """
    FunctionName: str
    UserParameters: str


class ActionConfiguration(typing.TypedDict):
    """
    ActionConfiguration

    Attributes:
    ----------
    configuration: :py:class:`Configuration`
    """
    configuration: Configuration


class S3Location(typing.TypedDict):
    """
    S3Location

    Attributes:
    ----------
    bucketName: str

    objectKey: str
    """
    bucketName: str
    objectKey: str


class ArtifactLocation(typing.TypedDict):
    """
    ArtifactLocation

    Attributes:
    ----------
    type: str
        S3 locations will use the "S3" type.

    s3Location: :py:class:`S3Location`
    """

    type: str
    s3Location: S3Location


class Artifact(typing.TypedDict):
    """
    Artifact

    Attributes:
    ----------
    name: str

    revision: typing.Optional[str]

    location: :py:class:`ArtifactLocation`
    """

    name: str
    revision: typing.Optional[str]
    location: ArtifactLocation


class ArtifactCredentials(typing.TypedDict):
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


class EncryptionKey(typing.TypedDict):
    """
    EncryptionKey

    Attributes:
    ----------
    id: str

    type: str
    """

    id: str
    type: str


class Data(typing.TypedDict, total=False):
    """
    Data

    Attributes:
    ----------
    actionConfiguration: :py:class:`ActionConfiguration`

    inputArtifacts: typing.List[:py:class:`Artifact`]

    outputArtifacts: typing.List[:py:class:`Artifact`]

    artifactCredentials: :py:class:`ArtifactCredentials`

    encryptionKey: typing.Optional[:py:class:`EncryptionKey`]

    continuationToken: typing.Optional[str]
    """
    actionConfiguration: ActionConfiguration
    inputArtifacts: typing.List[Artifact]
    outputArtifacts: typing.List[Artifact]
    artifactCredentials: ArtifactCredentials
    encryptionKey: typing.Optional[EncryptionKey]
    continuationToken: typing.Optional[str]


class CodePipelineJob(typing.TypedDict):
    """
    CodePipelineJob https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-invoke-lambda-function.html

    Attributes:
    ----------
    id: str

    accountId: str

    data: :py:class:`Data`
    """

    id: str
    accountId: str
    data: Data


"""
CodePipelineEvent https://docs.aws.amazon.com/lambda/latest/dg/services-codepipeline.html
"""
CodePipelineEvent = typing.TypedDict('CodePipelineEvent', {
    'CodePipeline.job': CodePipelineJob
})
