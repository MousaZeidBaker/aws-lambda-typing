#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Dict, List, TypedDict
else:
    from typing import Dict, List

    from typing_extensions import TypedDict


CloudWatchEventsMessageEvent = TypedDict(
    "CloudWatchEventsMessageEvent",
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
CloudWatchEventsMessageEvent
https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents.html

Other CloudWatch Events Event Examples:
https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/EventTypes.html

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
