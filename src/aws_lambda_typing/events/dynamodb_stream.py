#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Any, Dict, List, Literal, Optional, TypedDict
else:
    from typing import Any, Dict, List, Optional

    from typing_extensions import Literal, TypedDict


class AttributeValue(TypedDict, total=False):
    """
    AttributeValue
    https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_AttributeValue.html

    Attributes:
    ----------
    B: str

    BS: List[str]

    BOOL: bool

    L: List

    M: Dict

    N: str

    NS: List[str]

    NULL: bool

    S: str

    SS: List[str]
    """

    B: str
    BS: List[str]
    BOOL: bool
    L: List
    M: Dict
    N: str
    NS: List[str]
    NULL: bool
    S: str
    SS: List[str]


class StreamRecord(TypedDict, total=False):
    """
    StreamRecord
    https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_StreamRecord.html

    Attributes:
    ----------
    ApproximateCreationDateTime: Optional[int]

    Keys: Dict[str, :py:class:`AttributeValue`]

    NewImage: Dict[str, :py:class:`AttributeValue`]

    OldImage: Optional[Dict[str, AttributeValue]]

    SequenceNumber: str

    SizeBytes: int

    StreamViewType: Literal['KEYS_ONLY', 'NEW_IMAGE', 'OLD_IMAGE',
    'NEW_AND_OLD_IMAGES']
    """

    ApproximateCreationDateTime: Optional[int]
    Keys: Dict[str, AttributeValue]
    NewImage: Dict[str, AttributeValue]
    OldImage: Optional[Dict[str, AttributeValue]]
    SequenceNumber: str
    SizeBytes: int
    StreamViewType: Literal[
        "KEYS_ONLY",
        "NEW_IMAGE",
        "OLD_IMAGE",
        "NEW_AND_OLD_IMAGES",
    ]


class DynamodbRecord(TypedDict, total=False):
    """
    DynamodbRecord
    https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_Record.html

    Attributes:
    ----------
    awsRegion: str

    dynamodb: :py:class:`StreamRecord`

    eventID: str

    eventName: Literal['INSERT', 'MODIFY', 'REMOVE']

    eventSource: str

    eventSourceARN: str

    eventVersion: str

    userIdentity: Optional[Any]
    """

    awsRegion: str
    dynamodb: StreamRecord
    eventID: str
    eventName: Literal["INSERT", "MODIFY", "REMOVE"]
    eventSource: str
    eventSourceARN: str
    eventVersion: str
    userIdentity: Optional[Any]


class DynamoDBStreamEvent(TypedDict):
    """
    DynamoDBStreamEvent
    https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html

    Attributes:
    ----------
    Records: List[:py:class:`DynamodbRecord`]
    """

    Records: List[DynamodbRecord]
