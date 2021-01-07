#!/usr/bin/env python

import typing


class SNSMessageAttribute(typing.TypedDict):
    """
    SNSMessageAttribute https://docs.aws.amazon.com/sns/latest/api/API_MessageAttributeValue.html

    Attributes:
    ----------
    Type: str

    Value: str
    """
    Type: str
    Value: str


class SNSMessage(typing.TypedDict):
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

    MessageAttributes: typing.Dict[str, :py:class:`SNSMessageAttribute`]

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
    MessageAttributes: typing.Dict[str, SNSMessageAttribute]
    Type: str
    UnsubscribeUrl: str
    TopicArn: str
    Subject: str


class SNSEventRecord(typing.TypedDict):
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


class SNSEvent(typing.TypedDict):
    """
    SNSEvent https://docs.aws.amazon.com/lambda/latest/dg/with-sns.html

    Attributes:
    ----------
    Records: typing.List[:py:class:`SNSEventRecord`]
    """

    Records: typing.List[SNSEventRecord]
