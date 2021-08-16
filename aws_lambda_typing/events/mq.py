#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import List, Optional, Set, TypedDict
else:
    from typing import List, Optional, Set

    from typing_extensions import TypedDict


class MQMessageDestination(TypedDict):
    """
    MQMessageDestination

    Attributes:
    ----------
    physicalname: str
    """

    physicalname: str


class MQMessage(TypedDict, total=False):
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
    redelivered: Optional[bool]
    persistent: Optional[bool]
    destination: MQMessageDestination
    timestamp: int
    brokerInTime: int
    brokerOutTime: int


class MQEvent(TypedDict):
    """
    MQEvent https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html

    Attributes:
    ----------
    eventSource: str

    eventSourceArn: str

    messages: Set[List[MQMessage]]
    """

    eventSource: str
    eventSourceArn: str
    messages: Set[List[MQMessage]]
