#!/usr/bin/env python

import typing

"""
CloudWatchEventsMessageEvent https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents.html

Other CloudWatch Events Event Examples: https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/EventTypes.html

"""
CloudWatchEventsMessageEvent = typing.TypedDict('CloudWatchEventsMessageEvent', {
    'version': str,
    'id': str,
    'detail-type': str,
    'source': str,
    'account': str,
    'time': str,
    'region': str,
    'resources': typing.List[str],
    'detail': typing.Dict,
})
