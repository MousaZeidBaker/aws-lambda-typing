#!/usr/bin/env python

import typing


class MQMessageDestination(typing.TypedDict):
    """
    MQMessageDestination

    Attributes:
    ----------
    physicalname: str
    """

    physicalname: str


class MQMessage(typing.TypedDict, total=False):
    """
    MQMessage

    Attributes:
    ----------
    messageID: str

    messageType: str

    data: str

    connectionId: str

    redelivered: bool

    persistent: bool

    destination: :py:class:`MQMessageDestination`

    timestamp: int

    brokerInTime: int

    brokerOutTime: int
    """

    messageID: str
    messageType: str
    data: str
    connectionId: str
    redelivered: typing.Optional[bool]
    persistent: typing.Optional[bool]
    destination: MQMessageDestination
    timestamp: int
    brokerInTime: int
    brokerOutTime: int


class MQEvent(typing.TypedDict):
    """
    MQEvent https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html

    Attributes:
    ----------
    eventSource: str

    eventSourceArn: str

    messages: typing.Set[typing.List[MQMessage]]
    """

    eventSource: str
    eventSourceArn: str
    messages: typing.Set[typing.List[MQMessage]]
