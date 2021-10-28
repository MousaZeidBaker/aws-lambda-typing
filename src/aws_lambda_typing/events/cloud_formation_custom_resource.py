#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Any, Dict, Literal, Optional, TypedDict
else:
    from typing import Any, Dict, Optional

    from typing_extensions import Literal, TypedDict


class CloudFormationCustomResourceEventCommon(TypedDict):
    """
    CloudFormationCustomResourceEventCommon
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-requesttypes.html

    Attributes:
    ----------
    RequestId: str
    ResponseURL: str
    ResourceType: str
    LogicalResourceId: str
    StackId: str
    ResourceProperties: Dict[str, Any]
    """

    RequestId: str
    ResponseURL: str
    ResourceType: str
    LogicalResourceId: str
    StackId: str
    ResourceProperties: Dict[str, Any]


class CloudFormationCustomResourceCreateEvent(
    CloudFormationCustomResourceEventCommon
):
    """
    CloudFormationCustomResourceCreateEvent
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-requesttypes-create.html

    Attributes:
    ----------
    RequestType: Literal["Create"]
    RequestId: str
    ResponseURL: str
    ResourceType: str
    LogicalResourceId: str
    StackId: str
    ResourceProperties: Dict[str, Any]
    """

    RequestType: Literal["Create"]


class CloudFormationCustomResourceUpdateEvent(
    CloudFormationCustomResourceEventCommon
):
    """
    CloudFormationCustomResourceUpdateEvent
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-requesttypes-update.html

    Attributes:
    ----------
    RequestType: Literal["Update"]
    RequestId: str
    ResponseURL: str
    ResourceType: str
    LogicalResourceId: str
    StackId: str
    ResourceProperties: Dict[str, Any]
    PhysicalResourceId: str
    OldResourceProperties: Dict[str, Any]
    """

    RequestType: Literal["Update"]
    PhysicalResourceId: str
    OldResourceProperties: Dict[str, Any]


class CloudFormationCustomResourceDeleteEvent(
    CloudFormationCustomResourceEventCommon
):
    """
    CloudFormationCustomResourceDeleteEvent
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-requesttypes-delete.html

    Attributes:
    ----------
    RequestType: Literal["Delete"]
    RequestId: str
    ResponseURL: str
    ResourceType: str
    LogicalResourceId: str
    StackId: str
    ResourceProperties: Dict[str, Any]
    PhysicalResourceId: str
    """

    RequestType: Literal["Delete"]
    PhysicalResourceId: str


class CloudFormationCustomResourceEvent(
    CloudFormationCustomResourceEventCommon, total=False
):
    """
    CloudFormationCustomResourceEvent
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-requesttypes.html

    Attributes:
    ----------
    RequestType: Literal["Create", "Update", "Delete"]
    RequestId: str
    ResponseURL: str
    ResourceType: str
    LogicalResourceId: str
    StackId: str
    ResourceProperties: Dict[str, Any]
    PhysicalResourceId: Optional[str] Only in Update/Delete events
    OldResourceProperties: Optional[Dict[str, Any]] Only in Update events
    """

    RequestType: Literal["Create", "Update", "Delete"]
    PhysicalResourceId: Optional[str]
    OldResourceProperties: Optional[Dict[str, Any]]
