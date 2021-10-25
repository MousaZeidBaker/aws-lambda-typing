#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import List, TypedDict
else:
    from typing import List

    from typing_extensions import TypedDict


class Reference(TypedDict):
    """
    Reference

    Attributes:
    ----------
    commit: str

    ref: str
    """

    commit: str
    ref: str


class CodeCommit(TypedDict):
    """
    CodeCommit

    Attributes:
    ----------
    references: List[:py:class:`Reference`]
    """

    references: List[Reference]


class CodeCommitMessage(TypedDict):
    """
    CodeCommitMessage

    Attributes:
    ----------
    awsRegion: str

    codecommit: :py:class:`CodeCommit`

    eventId: str

    eventName: str

    eventPartNumber: int

    eventSource: str

    eventSourceARN: str

    eventTime: str

    eventTotalParts: int

    eventTriggerConfigId: str

    eventTriggerName: str

    eventVersion: str

    userIdentityARN: str
    """

    awsRegion: str
    codecommit: CodeCommit
    eventId: str
    eventName: str
    eventPartNumber: int
    eventSource: str
    eventSourceARN: str
    eventTime: str
    eventTotalParts: int
    eventTriggerConfigId: str
    eventTriggerName: str
    eventVersion: str
    userIdentityARN: str


class CodeCommitMessageEvent(TypedDict):
    """
    CodeCommitMessageEvent
    https://docs.aws.amazon.com/lambda/latest/dg/services-codecommit.html

    Attributes:
    ----------
    Records: List[:py:class:`CodeCommitMessage`]
    """

    Records: List[CodeCommitMessage]
