#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Any, Dict, Literal, TypedDict
else:
    from typing import Any, Dict

    from typing_extensions import Literal, TypedDict


class CloudFormationCustomResourceCommon(TypedDict):
    """
    CloudFormationCustomResourceCommon
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
    """

    RequestType: Literal[
        "Create",
        "Update",
        "Delete",
    ]
    RequestId: str
    ResponseURL: str
    ResourceType: str
    LogicalResourceId: str
    StackId: str
    ResourceProperties: Dict[str, Any]


class CloudFormationCustomResourceUpdate(
    CloudFormationCustomResourceCommon,
    total=False,
):
    """
    CloudFormationCustomResourceUpdate
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-requesttypes-update.html

    Attributes:
    ----------
    PhysicalResourceId: str

    OldResourceProperties: Dict[str, Any]
    """

    PhysicalResourceId: str
    OldResourceProperties: Dict[str, Any]


class CloudFormationCustomResourceDelete(
    CloudFormationCustomResourceCommon,
    total=False,
):
    """
    CloudFormationCustomResourceDelete
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-requesttypes-delete.html

    Attributes:
    ----------
    PhysicalResourceId: str
    """

    PhysicalResourceId: str


class CloudFormationCustomResourceEvent(
    CloudFormationCustomResourceUpdate,
    CloudFormationCustomResourceDelete,
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

    pass
