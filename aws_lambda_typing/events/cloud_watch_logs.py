#!/usr/bin/env python

import typing


class LogEvent(typing.TypedDict):
    """
    LogEvent

    Attributes:
    ----------
    id: str

    timestamp: int

    message: str
    """

    id: str
    timestamp: int
    message: str


class CloudWatchLogsDecodedData(typing.TypedDict):
    """
    CloudWatchLogsDecodedData https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SubscriptionFilters.html

    Attributes:
    ----------
    messageType: str
        Data messages will use the "DATA_MESSAGE" type. Sometimes CloudWatch Logs may emit Lambda records with a
        "CONTROL_MESSAGE" type, mainly for checking if the destination is reachable.

    owner: str

    logGroup: str

    logStream: str

    subscriptionFilters: typing.List[str]

    logEvents: typing.List[LogEvent]
    """

    messageType: str
    owner: str
    logGroup: str
    logStream: str
    subscriptionFilters: typing.List[str]
    logEvents: typing.List[LogEvent]


class AWSLogs(typing.TypedDict):
    """
    AWSLogs

    Attributes:
    ----------
    data: str
        Base64 encoded and compressed with the gzip format.
    """

    data: str


class CloudWatchLogsEvent(typing.TypedDict):
    """
    CloudWatchLogsEvent https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchlogs.html

    Attributes:
    ----------
    awslogs: str
    """

    awslogs: AWSLogs
