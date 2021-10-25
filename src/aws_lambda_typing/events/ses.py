#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import (
        Any,
        Dict,
        Final,
        List,
        Literal,
        Optional,
        TypedDict,
        Union,
    )
else:
    from typing import Any, Dict, List, Optional, Union

    from typing_extensions import Final, Literal, TypedDict


class SESMailHeader(TypedDict):
    """
    SESReceiptStatus

    Attributes:
    ----------
    name: str

    value: str
    """

    name: str
    value: str


SESMailCommonHeaders: Final = TypedDict(
    "SESMailCommonHeaders",
    {
        "returnPath": str,
        "from": Optional[List[str]],
        "date": str,
        "to": Optional[List[str]],
        "cc": Optional[List[str]],
        "bcc": Optional[List[str]],
        "sender": Optional[List[str]],
        "replyTo": Optional[List[str]],
        "messageId": str,
        "subject": str,
    },
    total=False,
)
"""
SESMailCommonHeaders

Attributes:
----------
returnPath: str

from: Optional[List[str]]

date: str

to: Optional[List[str]]

cc: Optional[List[str]]

bcc: Optional[List[str]]

sender: Optional[List[str]]

replyTo: Optional[List[str]]

messageId: str

subject: str
"""


class SESMail(TypedDict):
    """
    SESReceiptStatus

    Attributes:
    ----------
    timestamp: str

    source: str

    messageId: str

    destination: List[str]

    headersTruncated: bool

    headers: List[:py:class:`SESMailHeader`]

    commonHeaders: :py:const:`SESMailCommonHeaders`
    """

    timestamp: str
    source: str
    messageId: str
    destination: List[str]
    headersTruncated: bool
    headers: List[SESMailHeader]
    commonHeaders: SESMailCommonHeaders


class SESReceiptStatus(TypedDict):
    """
    SESReceiptStatus

    Attributes:
    ----------
    status: :py:class:`SESReceiptStatusEnum` status: Literal['PASS', 'FAIL',
    'GRAY']
    """

    status: Literal[
        "PASS",
        "FAIL",
        "GRAY",
    ]


class SESReceiptS3Action(TypedDict, total=False):
    """
    SESReceiptS3Action

    Attributes:
    ----------
    type: Literal['S3']

    topicArn: Optional[str]

    bucketName: str

    objectKey: str
    """

    type: Literal["S3"]
    topicArn: Optional[str]
    bucketName: str
    objectKey: str


class SESReceiptSnsAction(TypedDict, total=False):
    """
    SESReceiptSnsAction

    Attributes:
    ----------
    type: Literal['SNS']

    topicArn: str
    """

    type: Literal["SNS"]
    topicArn: str


class SESReceiptBounceAction(TypedDict, total=False):
    """
    SESReceiptBounceAction

    Attributes:
    ----------
    type: Literal['Bounce']

    topicArn: Optional[str]

    smtpReplyCode: str

    statusCode: str

    message: str

    sender: str
    """

    type: Literal["Bounce"]
    topicArn: Optional[str]
    smtpReplyCode: str
    statusCode: str
    message: str
    sender: str


class SESReceiptLambdaAction(TypedDict, total=False):
    """
    SESReceiptLambdaAction

    Attributes:
    ----------
    type: Literal['Lambda']

    topicArn: Optional[str]

    functionArn: str

    invocationType: str
    """

    type: Literal["Lambda"]
    topicArn: Optional[str]
    functionArn: str
    invocationType: str


class SESReceiptStopAction(TypedDict, total=False):
    """
    SESReceiptStopAction

    Attributes:
    ----------
    type: Literal['Stop']

    topicArn: Optional[str]
    """

    type: Literal["Stop"]
    topicArn: Optional[str]


class SESReceiptWorkMailAction(TypedDict, total=False):
    """
    SESReceiptWorkMailAction

    Attributes:
    ----------
    type: Literal['WorkMail']

    topicArn: Optional[str]

    organizationArn: str
    """

    type: Literal["WorkMail"]
    topicArn: Optional[str]
    organizationArn: str


class SESReceipt(TypedDict, total=False):
    """
    SESReceipt

    Attributes:
    ----------
    receipt: :py:class:`SESReceipt`

    timestamp: str

    spamVerdict: :py:class:`SESReceiptStatus`

    dkimVerdict: :py:class:`SESReceiptStatus`

    processingTimeMillis: int

    action: Union[:py:class:`SESReceiptS3Action`,
                          :py:class:`SESReceiptSnsAction`,
                          :py:class:`SESReceiptBounceAction`,
                          :py:class:`SESReceiptLambdaAction`,
                          :py:class:`SESReceiptStopAction`,
                          :py:class:`SESReceiptWorkMailAction`]]

    spfVerdict: :py:class:`SESReceiptStatus`

    virusVerdict: :py:class:`SESReceiptStatus`

    dmarcVerdict: :py:class:`SESReceiptStatus`

    dmarcPolicy: Literal['none', 'quarantine', 'reject']
    """

    recipients: List[str]
    timestamp: str
    spamVerdict: SESReceiptStatus
    dkimVerdict: SESReceiptStatus
    processingTimeMillis: int
    action: Union[
        Union[
            Union[SESReceiptS3Action, SESReceiptSnsAction],
            Union[SESReceiptBounceAction, SESReceiptLambdaAction],
        ],
        Union[
            Union[SESReceiptStopAction, SESReceiptWorkMailAction],
            # Workaround for no type inference for dicts in union, see
            # https://github.com/python/mypy/issues/6463#issuecomment-467019931
            Dict[str, Any],
        ],
    ]
    spfVerdict: SESReceiptStatus
    virusVerdict: SESReceiptStatus
    dmarcVerdict: SESReceiptStatus
    dmarcPolicy: Literal[
        "none",
        "quarantine",
        "reject",
    ]


class SESMessage(TypedDict):
    """
    SESMessage
    https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-notifications-contents.html

    Attributes:
    ----------
    mail: :py:class:`SESMail`

    receipt: :py:class:`SESReceipt`
    """

    mail: SESMail
    receipt: SESReceipt


class SESEventRecord(TypedDict):
    """
    SESEventRecord

    Attributes:
    ----------
    eventVersion: str

    ses: :py:class:`SESMessage`

    eventSource: str
    """

    eventVersion: str
    ses: SESMessage
    eventSource: str


class SESEvent(TypedDict):
    """
    SESEvent https://docs.aws.amazon.com/lambda/latest/dg/services-ses.html

    Attributes:
    ----------
    Records: List[:py:class:`SESEventRecord`]
    """

    Records: List[SESEventRecord]
