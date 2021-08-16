#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import List, TypedDict
else:
    from typing import List

    from typing_extensions import TypedDict


class KinesisStreamKinesis(TypedDict):
    """
    KinesisStreamKinesis

    Attributes:
    ----------
    kinesisSchemaVersion: str

    partitionKey: str

    sequenceNumber: str

    data: str

    approximateArrivalTimestamp: float
    """

    kinesisSchemaVersion: str
    partitionKey: str
    sequenceNumber: str
    data: str
    approximateArrivalTimestamp: float


class KinesisStreamRecord(TypedDict):
    """
    KinesisStreamRecord

    Attributes:
    ----------
    kinesis: :py:class:`KinesisStreamKinesis`

    eventSource: str

    eventVersion: str

    eventID: str

    eventName: str

    invokeIdentityArn: str

    awsRegion: str

    eventSourceARN: str
    """

    kinesis: KinesisStreamKinesis
    eventSource: str
    eventVersion: str
    eventID: str
    eventName: str
    invokeIdentityArn: str
    awsRegion: str
    eventSourceARN: str


class KinesisStreamEvent(TypedDict):
    """
    KinesisStreamEvent https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html

    Attributes:
    ----------
    records: List[:py:class:`KinesisStreamRecord`]
    """

    records: List[KinesisStreamRecord]
