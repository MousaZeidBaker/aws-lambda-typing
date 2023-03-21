#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Dict, List, Literal, TypedDict
else:
    from typing import Dict, List

    from typing_extensions import Literal, TypedDict


class ApacheKafkaRecord(TypedDict):
    """
    ApacheKafkaRecord

    Attributes:
    ----------
    topic: str

    partition: int

    offset: int

    timestamp: int

    timestampType: Literal["CREATE_TIME", "LOG_APPEND_TIME"]

    key: str

    value: str

    headers: List[Dict]
    """

    topic: str
    partition: int
    offset: int
    timestamp: int
    timestampType: Literal[
        "CREATE_TIME",
        "LOG_APPEND_TIME",
    ]
    key: str
    value: str
    headers: List[Dict]


class ApacheKafkaEvent(TypedDict):
    """
    ApacheKafkaEvent
    https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html

    Attributes:
    ----------
    eventSource: Literal["SelfManagedKafka"]

    bootstrapServers: str

    records: Dict[str, List[:py:class:`ApacheKafkaRecord`]]
    """

    eventSource: Literal["SelfManagedKafka"]
    bootstrapServers: str
    records: Dict[str, List[ApacheKafkaRecord]]
