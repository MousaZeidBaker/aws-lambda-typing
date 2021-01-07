#!/usr/bin/env python

import typing


class SESMailHeader(typing.TypedDict):
    """
    SESReceiptStatus

    Attributes:
    ----------
    name: str

    value: str
    """

    name: str
    value: str


SESMailCommonHeaders: typing.Final = typing.TypedDict('SESMailCommonHeaders', {
    'returnPath': str,
    'from': typing.Optional[typing.List[str]],
    'date': str,
    'to': typing.Optional[typing.List[str]],
    'cc': typing.Optional[typing.List[str]],
    'bcc': typing.Optional[typing.List[str]],
    'sender': typing.Optional[typing.List[str]],
    'replyTo': typing.Optional[typing.List[str]],
    'messageId': str,
    'subject': str
}, total=False)


class SESMail(typing.TypedDict):
    """
    SESReceiptStatus

    Attributes:
    ----------
    timestamp: str

    source: str

    messageId: str

    destination: typing.List[str]

    headersTruncated: bool

    headers: typing.List[:py:class:`SESMailHeader`]

    commonHeaders: :py:const:`SESMailCommonHeaders`
    """
    timestamp: str
    source: str
    messageId: str
    destination: typing.List[str]
    headersTruncated: bool
    headers: typing.List[SESMailHeader]
    commonHeaders: SESMailCommonHeaders


class SESReceiptStatus(typing.TypedDict):
    """
    SESReceiptStatus

    Attributes:
    ----------
    status: :py:class:`SESReceiptStatusEnum`
    status: typing.Literal['PASS', 'FAIL', 'GRAY']
    """

    status: typing.Literal['PASS', 'FAIL', 'GRAY']


class SESReceiptS3Action(typing.TypedDict, total=False):
    """
    SESReceiptS3Action

    Attributes:
    ----------
    type: typing.Literal['S3']

    topicArn: typing.Optional[str]

    bucketName: str

    objectKey: str
    """

    type: typing.Literal['S3']
    topicArn: typing.Optional[str]
    bucketName: str
    objectKey: str


class SESReceiptSnsAction(typing.TypedDict, total=False):
    """
    SESReceiptSnsAction

    Attributes:
    ----------
    type: typing.Literal['SNS']

    topicArn: str
    """

    type: typing.Literal['SNS']
    topicArn: str


class SESReceiptBounceAction(typing.TypedDict, total=False):
    """
    SESReceiptBounceAction

    Attributes:
    ----------
    type: typing.Literal['Bounce']

    topicArn: typing.Optional[str]

    smtpReplyCode: str

    statusCode: str

    message: str

    sender: str
    """

    type: typing.Literal['Bounce']
    topicArn: typing.Optional[str]
    smtpReplyCode: str
    statusCode: str
    message: str
    sender: str


class SESReceiptLambdaAction(typing.TypedDict, total=False):
    """
    SESReceiptLambdaAction

    Attributes:
    ----------
    type: typing.Literal['Lambda']

    topicArn: typing.Optional[str]

    functionArn: str

    invocationType: str
    """

    type: typing.Literal['Lambda']
    topicArn: typing.Optional[str]
    functionArn: str
    invocationType: str


class SESReceiptStopAction(typing.TypedDict, total=False):
    """
    SESReceiptStopAction

    Attributes:
    ----------
    type: typing.Literal['Stop']

    topicArn: typing.Optional[str]
    """

    type: typing.Literal['Stop']
    topicArn: typing.Optional[str]


class SESReceiptWorkMailAction(typing.TypedDict, total=False):
    """
    SESReceiptWorkMailAction

    Attributes:
    ----------
    type: typing.Literal['WorkMail']

    topicArn: typing.Optional[str]

    organizationArn: str
    """

    type: typing.Literal['WorkMail']
    topicArn: typing.Optional[str]
    organizationArn: str


class SESReceipt(typing.TypedDict, total=False):
    """
    SESReceipt

    Attributes:
    ----------
    receipt: :py:class:`SESReceipt`

    timestamp: str

    spamVerdict: :py:class:`SESReceiptStatus`

    dkimVerdict: :py:class:`SESReceiptStatus`

    processingTimeMillis: int

    action: Union[:py:class:`SESReceiptS3Action`, :py:class:`SESReceiptSnsAction`,
                          :py:class:`SESReceiptBounceAction`, :py:class:`SESReceiptLambdaAction`,
                          :py:class:`SESReceiptStopAction`, :py:class:`SESReceiptWorkMailAction`]]

    spfVerdict: :py:class:`SESReceiptStatus`

    virusVerdict: :py:class:`SESReceiptStatus`

    dmarcVerdict: :py:class:`SESReceiptStatus`

    dmarcPolicy: typing.Literal['none', 'quarantine', 'reject']
    """
    recipients: typing.List[str]
    timestamp: str
    spamVerdict: SESReceiptStatus
    dkimVerdict: SESReceiptStatus
    processingTimeMillis: int
    action: typing.Union[
        typing.Union[
            typing.Union[SESReceiptS3Action, SESReceiptSnsAction],
            typing.Union[SESReceiptBounceAction, SESReceiptLambdaAction],
        ],
        typing.Union[
            typing.Union[SESReceiptStopAction, SESReceiptWorkMailAction],
            # Workaround for no type inference for dicts in union,
            # see https://github.com/python/mypy/issues/6463#issuecomment-467019931
            typing.Dict[str, typing.Any]
        ]
    ]
    spfVerdict: SESReceiptStatus
    virusVerdict: SESReceiptStatus
    dmarcVerdict: SESReceiptStatus
    dmarcPolicy: typing.Literal['none', 'quarantine', 'reject']


class SESMessage(typing.TypedDict):
    """
    SESMessage https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-notifications-contents.html

    Attributes:
    ----------
    mail: :py:class:`SESMail`

    receipt: :py:class:`SESReceipt`
    """

    mail: SESMail
    receipt: SESReceipt


class SESEventRecord(typing.TypedDict):
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


class SESEvent(typing.TypedDict):
    """
    SESEvent https://docs.aws.amazon.com/lambda/latest/dg/services-ses.html

    Attributes:
    ----------
    Records: typing.List[:py:class:`SESEventRecord`]
    """

    Records: typing.List[SESEventRecord]
