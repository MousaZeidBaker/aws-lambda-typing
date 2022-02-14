#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Dict, List, TypedDict
else:
    from typing import Dict, List

    from typing_extensions import TypedDict


EventBridgeEvent = TypedDict(
    "EventBridgeEvent",
    {
        "version": str,
        "id": str,
        "detail-type": str,
        "source": str,
        "account": str,
        "time": str,
        "region": str,
        "resources": List[str],
        "detail": Dict,
    },
)
"""
EventBridgeEvent
https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html

https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents.html

Attributes:
----------
version: str

id: str

detail-type: str

source: str

account: str

time: str

region: str

resources: List[str]

detail: Dict
"""
