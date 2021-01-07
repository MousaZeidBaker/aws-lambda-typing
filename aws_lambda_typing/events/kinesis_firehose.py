#!/usr/bin/env python

import typing


class KinesisFirehoseKinesisRecordMetadata(typing.TypedDict):
    """
    KinesisFirehoseKinesisRecordMetadata

    Attributes:
    ----------
    shardId: str

    partitionKey: str

    approximateArrivalTimestamp: str

    sequenceNumber: str

    subsequenceNumber: str
    """

    shardId: str
    partitionKey: str
    approximateArrivalTimestamp: str
    sequenceNumber: str
    subsequenceNumber: str


class KinesisFirehoseRecord(typing.TypedDict):
    """
    KinesisFirehoseRecord

    Attributes:
    ----------
    data: str

    recordId: str

    approximateArrivalTimestamp: int

    kinesisRecordMetadata: :py:class:`KinesisFirehoseKinesisRecordMetadata`
    """

    data: str
    recordId: str
    approximateArrivalTimestamp: int
    kinesisRecordMetadata: KinesisFirehoseKinesisRecordMetadata


class KinesisFirehoseEvent(typing.TypedDict):
    """
    KinesisFirehoseEvent https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html

    Attributes:
    ----------
    invocationId: str

    deliveryStreamArn: str

    region: str

    records: typing.List[:py:class:`KinesisFirehoseRecord`]
    """

    invocationId: str
    deliveryStreamArn: str
    region: str
    records: typing.List[KinesisFirehoseRecord]
