#!/usr/bin/env python

import typing


class KinesisStreamKinesis(typing.TypedDict):
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


class KinesisStreamRecord(typing.TypedDict):
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


class KinesisStreamEvent(typing.TypedDict):
    """
    KinesisStreamEvent https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html

    Attributes:
    ----------
    records: typing.List[:py:class:`KinesisStreamRecord`]
    """

    records: typing.List[KinesisStreamRecord]
