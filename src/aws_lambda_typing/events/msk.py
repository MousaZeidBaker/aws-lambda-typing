#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Dict, List, Literal, TypedDict
else:
    from typing import Dict, List

    from typing_extensions import Literal, TypedDict


class MSKRecord(TypedDict):
    """
    MSKRecord

    Attributes:
    ----------
    topic: str

    partition: str

    offset: int

    timestamp: int

    timestampType: Literal["CREATE_TIME", "LOG_APPEND_TIME"]

    value: str

    headers: List[Dict]
    """

    topic: str
    partition: str
    offset: int
    timestamp: int
    timestampType: Literal[
        "CREATE_TIME",
        "LOG_APPEND_TIME",
    ]
    value: str
    headers: List[Dict]


class MSKEvent(TypedDict):
    """
    MSKEvent
    https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html

    Attributes:
    ----------
    eventSource: Literal["aws:kafka"]

    eventSourceArn: str

    records: Dict[str, List[:py:class:`MSKRecord`]]
    """

    eventSource: Literal["aws:kafka"]
    eventSourceArn: str
    records: Dict[str, List[MSKRecord]]
