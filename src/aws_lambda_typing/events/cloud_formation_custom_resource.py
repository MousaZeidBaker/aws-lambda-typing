#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Any, Dict, Literal, TypedDict, Union
else:
    from typing import Any, Dict, Union

    from typing_extensions import Literal, TypedDict


class CloudFormationCustomResourceCommon(TypedDict):
    """
    CloudFormationCustomResourceCommon
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


class CloudFormationCustomResourceCreate(
    CloudFormationCustomResourceCommon,
):
    """
    CloudFormationCustomResourceCreate
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-requesttypes-create.html

    Attributes:
    ----------
    RequestType: Literal['Create']
    """

    RequestType: Literal["Create"]


class CloudFormationCustomResourceUpdate(
    CloudFormationCustomResourceCommon,
):
    """
    CloudFormationCustomResourceUpdate
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-requesttypes-update.html

    Attributes:
    ----------
    RequestType: Literal['Update']

    PhysicalResourceId: str

    OldResourceProperties: Dict[str, Any]
    """

    RequestType: Literal["Update"]
    PhysicalResourceId: str
    OldResourceProperties: Dict[str, Any]


class CloudFormationCustomResourceDelete(
    CloudFormationCustomResourceCommon,
):
    """
    CloudFormationCustomResourceDelete
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-requesttypes-delete.html

    Attributes:
    ----------
    RequestType: Literal['Delete']

    PhysicalResourceId: str
    """

    RequestType: Literal["Delete"]
    PhysicalResourceId: str


CloudFormationCustomResourceEvent = Union[
    CloudFormationCustomResourceCreate,
    CloudFormationCustomResourceUpdate,
    CloudFormationCustomResourceDelete,
]
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

PhysicalResourceId: str (only in "Update" and "Delete" events)

OldResourceProperties: Dict[str, Any] (only in "Update" events)
"""
