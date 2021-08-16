#!/usr/bin/env python

from typing import Dict, List, TypedDict


class SNSMessageAttribute(TypedDict):
    """
    SNSMessageAttribute https://docs.aws.amazon.com/sns/latest/api/API_MessageAttributeValue.html

    Attributes:
    ----------
    Type: str

    Value: str
    """
    Type: str
    Value: str


class SNSMessage(TypedDict):
    """
    SNSMessage

    Attributes:
    ----------
    SignatureVersion: str

    Timestamp: str

    Signature: str

    SigningCertUrl: str

    MessageId: str

    Message: str

    MessageAttributes: Dict[str, :py:class:`SNSMessageAttribute`]

    Type: str

    UnsubscribeUrl: str

    TopicArn: str

    Subject: str
    """

    SignatureVersion: str
    Timestamp: str
    Signature: str
    SigningCertUrl: str
    MessageId: str
    Message: str
    MessageAttributes: Dict[str, SNSMessageAttribute]
    Type: str
    UnsubscribeUrl: str
    TopicArn: str
    Subject: str


class SNSEventRecord(TypedDict):
    """
    SNSEventRecord

    Attributes:
    ----------
    EventVersion: str

    EventSubscriptionArn: str

    EventSource: str

    Sns: :py:class:`SNSMessage`
    """

    EventVersion: str
    EventSubscriptionArn: str
    EventSource: str
    Sns: SNSMessage


class SNSEvent(TypedDict):
    """
    SNSEvent https://docs.aws.amazon.com/lambda/latest/dg/with-sns.html

    Attributes:
    ----------
    Records: List[:py:class:`SNSEventRecord`]
    """

    Records: List[SNSEventRecord]
