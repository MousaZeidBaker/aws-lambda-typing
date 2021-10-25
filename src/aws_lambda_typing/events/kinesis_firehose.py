#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import List, TypedDict
else:
    from typing import List

    from typing_extensions import TypedDict


class KinesisFirehoseKinesisRecordMetadata(TypedDict):
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


class KinesisFirehoseRecord(TypedDict):
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


class KinesisFirehoseEvent(TypedDict):
    """
    KinesisFirehoseEvent
    https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html

    Attributes:
    ----------
    invocationId: str

    deliveryStreamArn: str

    region: str

    records: List[:py:class:`KinesisFirehoseRecord`]
    """

    invocationId: str
    deliveryStreamArn: str
    region: str
    records: List[KinesisFirehoseRecord]
