#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Dict, List, Literal, Optional, TypedDict
else:
    from typing import Dict, List, Optional

    from typing_extensions import Literal, TypedDict


class SQSAttributes(TypedDict, total=False):
    """
    SQSAttributes

    Attributes:
    ----------
    ApproximateReceiveCount: str

    SentTimestamp: str

    SenderId: str

    ApproximateFirstReceiveTimestamp: str

    SequenceNumber: Optional[str] Only in FIFO queues

    MessageGroupId: Optional[str] Only in FIFO queues

    MessageDeduplicationId: Optional[str] Only in FIFO queues

    DeadLetterQueueSourceArn: str

    AWSTraceHeader: str
    """

    ApproximateReceiveCount: str
    SentTimestamp: str
    SenderId: str
    ApproximateFirstReceiveTimestamp: str
    SequenceNumber: Optional[str]
    MessageGroupId: Optional[str]
    MessageDeduplicationId: Optional[str]
    DeadLetterQueueSourceArn: str
    AWSTraceHeader: str


class SQSMessageAttribute(TypedDict):
    """
    SQSMessageAttribute
    https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_MessageAttributeValue.html

    Attributes:
    ----------
    binaryValue: str

    dataType: Literal['String', 'Number', 'Binary']

    stringValue: str

    stringListValues: List[str]

    binaryListValues: List[str]
    """

    binaryValue: Optional[str]
    dataType: Literal[
        "String",
        "Number",
        "Binary",
    ]
    stringValue: str
    stringListValues: List[str]
    binaryListValues: List[str]


class SQSMessage(TypedDict, total=False):
    """
    SQSMessage
    https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_Message.html

    Attributes:
    ----------
    messageId: str

    receiptHandle: str

    body: str

    attributes: :py:class:`SQSAttributes`

    messageAttributes: Dict[str, :py:class:`SQSMessageAttribute`]

    md5OfBody: str

    md5OfMessageAttributes: str

    eventSource: str

    eventSourceARN: str

    awsRegion: str
    """

    messageId: str
    receiptHandle: str
    body: str
    attributes: SQSAttributes
    messageAttributes: Dict[str, SQSMessageAttribute]
    md5OfBody: str
    md5OfMessageAttributes: str
    eventSource: str
    eventSourceARN: str
    awsRegion: str


class SQSEvent(TypedDict):
    """
    SQSEvent https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html

    Attributes:
    ----------
    Records: List[:py:class:`SQSMessage`]
    """

    Records: List[SQSMessage]
