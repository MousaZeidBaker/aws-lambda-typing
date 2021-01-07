#!/usr/bin/env python

import typing


class AttributeValue(typing.TypedDict, total=False):
    """
    AttributeValue https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_AttributeValue.html

    Attributes:
    ----------
    B: str

    BS: typing.List[str]

    BOOL: bool

    L: typing.List

    M: typing.Dict

    N: str

    NS: typing.List[str]

    NULL: bool

    S: str

    SS: typing.List[str]
    """

    B: str
    BS: typing.List[str]
    BOOL: bool
    L: typing.List
    M: typing.Dict
    N: str
    NS: typing.List[str]
    NULL: bool
    S: str
    SS: typing.List[str]


class StreamRecord(typing.TypedDict, total=False):
    """
    StreamRecord https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_StreamRecord.html

    Attributes:
    ----------
    ApproximateCreationDateTime: typing.Optional[int]

    Keys: typing.Dict[str, :py:class:`AttributeValue`]

    NewImage: typing.Dict[str, :py:class:`AttributeValue`]

    OldImage: typing.Optional[typing.Dict[str, AttributeValue]]

    SequenceNumber: str

    SizeBytes: int

    StreamViewType: typing.Literal['KEYS_ONLY', 'NEW_IMAGE', 'OLD_IMAGE', 'NEW_AND_OLD_IMAGES']
    """

    ApproximateCreationDateTime: typing.Optional[int]
    Keys: typing.Dict[str, AttributeValue]
    NewImage: typing.Dict[str, AttributeValue]
    OldImage: typing.Optional[typing.Dict[str, AttributeValue]]
    SequenceNumber: str
    SizeBytes: int
    StreamViewType: typing.Literal['KEYS_ONLY', 'NEW_IMAGE', 'OLD_IMAGE', 'NEW_AND_OLD_IMAGES']


class DynamodbRecord(typing.TypedDict, total=False):
    """
    DynamodbRecord https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_Record.html

    Attributes:
    ----------
    awsRegion: str

    dynamodb: :py:class:`StreamRecord`

    eventID: str

    eventName: typing.Literal['INSERT', 'MODIFY', 'REMOVE']

    eventSource: str

    eventSourceARN: str

    eventVersion: str

    userIdentity: typing.Optional[typing.Any]
    """

    awsRegion: str
    dynamodb: StreamRecord
    eventID: str
    eventName: typing.Literal['INSERT', 'MODIFY', 'REMOVE']
    eventSource: str
    eventSourceARN: str
    eventVersion: str
    userIdentity: typing.Optional[typing.Any]


class DynamoDBStreamEvent(typing.TypedDict):
    """
    DynamoDBStreamEvent https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html

    Attributes:
    ----------
    Records: typing.List[:py:class:`DynamodbRecord`]
    """

    Records: typing.List[DynamodbRecord]
