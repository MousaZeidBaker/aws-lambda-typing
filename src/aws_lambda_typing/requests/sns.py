#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Any, Dict, List, Literal, Optional, TypedDict, Union
else:
    from typing import Any, Dict, List, Optional, Union

    from typing_extensions import Literal, TypedDict


class MessageAttributesString(TypedDict):
    """
    MessageAttributesString

    Attributes:
    ----------
    DataType: str

    StringValue: str

    BinaryValue: Any
    """

    DataType: str
    StringValue: Optional[str]
    BinaryValue: Optional[Any]


class MessageAttributes(TypedDict):
    """
    MessageAttributes

    Attributes:
    ----------
    string: py:class:`MessageAttributesString`
    """

    string: MessageAttributesString


class PublishBatchRequestEntry(TypedDict, total=False):
    """
    PublishBatchRequestEntry
    https://docs.aws.amazon.com/sns/latest/api/API_PublishBatchRequestEntry.html

    Attributes:
    ----------
    Id: str

    Message: str

    MessageAttributes: Optional[:py:class:`MessageAttributes`]

    MessageDeduplicationId: Optional[str]

    MessageGroupId: Optional[str]

    MessageStructure: Optional[str]

    Subject: Optional[str]
    """

    Id: str
    Message: str
    MessageAttributes: Optional[MessageAttributes]
    MessageDeduplicationId: Optional[str]
    MessageGroupId: Optional[str]
    MessageStructure: Optional[str]
    Subject: Optional[str]


class SNSPublish(TypedDict, total=False):
    """
    SNSPublish
    https://docs.aws.amazon.com/sns/latest/api/API_Publish.html

    Attributes:
    ----------
    Message: Union[str, Dict[str, str]]

    MessageAttributes: Optional[:py:class:`MessageAttributes`]

    MessageDeduplicationId: Optional[str]

    MessageGroupId: Optional[str]

    MessageStructure: Optional[Literal["json"]]

    PhoneNumber: Optional[str]

    Subject: Optional[str]

    TargetArn: Optional[str]

    TopicArn: Optional[str]
    """

    Message: Union[str, Dict[str, str]]
    MessageAttributes: Optional[MessageAttributes]
    MessageDeduplicationId: Optional[str]
    MessageGroupId: Optional[str]
    MessageStructure: Optional[Literal["json"]]
    PhoneNumber: Optional[str]
    Subject: Optional[str]
    TargetArn: Optional[str]
    TopicArn: Optional[str]


class SNSPublishBatch(TypedDict, total=False):
    """
    SNSPublishBatch
    https://docs.aws.amazon.com/sns/latest/api/API_PublishBatch.html

    Attributes:
    ----------
    TopicArn: str

    PublishBatchRequestEntries: List[:py:class:`PublishBatchRequestEntry`]
    """

    TopicArn: str
    PublishBatchRequestEntries: List[PublishBatchRequestEntry]
