#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import List, Optional, TypedDict
else:
    from typing import List, Optional

    from typing_extensions import TypedDict


class S3UserIdentity(TypedDict):
    """
    S3UserIdentity

    Attributes:
    ----------
    principalId: str
    """

    principalId: str


class S3RequestParameters(TypedDict):
    """
    S3RequestParameters

    Attributes:
    ----------
    sourceIPAddress: str
    """

    sourceIPAddress: str


S3ResponseElements = TypedDict('S3ResponseElements', {
    'x-amz-request-id': str,
    'x-amz-id-2': str
}, total=False)
"""
S3ResponseElements

Attributes:
----------
x-amz-request-id: str

x-amz-id-2: str
"""


class S3OwnerIdentity(TypedDict):
    """
    S3OwnerIdentity

    Attributes:
    ----------
    principalId: str
    """

    principalId: str


class S3Bucket(TypedDict):
    """
    S3Bucket

    Attributes:
    ----------
    name: str

    ownerIdentity: :py:class:`S3OwnerIdentity`

    arn: str
    """

    name: str
    ownerIdentity: S3OwnerIdentity
    arn: str


class S3Object(TypedDict, total=False):
    """
    S3OwnerIdentity

    Attributes:
    ----------
    key: str

    size: int

    eTag: str

    versionId: Optional[str]

    sequencer: str
    """

    key: str
    size: int
    eTag: str
    versionId: Optional[str]
    sequencer: str


class S3(TypedDict):
    """
    S3

    Attributes:
    ----------
    s3SchemaVersion: str

    configurationId: str

    bucket: :py:class:`S3Bucket`

    object: :py:class:`S3Object`
    """

    s3SchemaVersion: str
    configurationId: str
    bucket: S3Bucket
    object: S3Object


class S3GlacierEventDataRestoreEventData(TypedDict):
    """
    S3GlacierEventData

    Attributes:
    ----------
    lifecycleRestorationExpiryTime: str

    lifecycleRestoreStorageClass: str
    """

    lifecycleRestorationExpiryTime: str
    lifecycleRestoreStorageClass: str


class S3GlacierEventData(TypedDict):
    """
    S3GlacierEventData

    Attributes:
    ----------
    restoreEventData: :py:class:`S3GlacierEventDataRestoreEventData`
    """

    restoreEventData: S3GlacierEventDataRestoreEventData


class S3EventRecord(TypedDict, total=False):
    """
    S3EventRecord https://docs.aws.amazon.com/AmazonS3/latest/dev/notification-content-structure.html

    Attributes:
    ----------
    eventVersion: str

    eventSource: str

    awsRegion: str

    eventTime: str

    eventName: str

    userIdentity: :py:class:`S3UserIdentity`

    requestParameters: :py:class:`S3RequestParameters`

    responseElements: :py:const:`S3ResponseElements`

    s3: :py:class:`S3`

    glacierEventData: Optional[:py:class:`S3GlacierEventData`]
    """

    eventVersion: str
    eventSource: str
    awsRegion: str
    eventTime: str
    eventName: str
    userIdentity: S3UserIdentity
    requestParameters: S3RequestParameters
    responseElements: S3ResponseElements
    s3: S3
    glacierEventData: Optional[S3GlacierEventData]


class S3Event(TypedDict):
    """
    S3Event https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html

    Attributes:
    ----------
    Records: List[:py:class:`S3EventRecord`]
    """

    Records: List[S3EventRecord]
