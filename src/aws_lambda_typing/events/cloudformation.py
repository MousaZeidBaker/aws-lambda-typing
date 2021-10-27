#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Any, Dict, Optional, TypedDict
else:
    from typing import Any, Dict, Optional

    from typing_extensions import TypedDict


class CloudFormationEvent(TypedDict):
    """
    CloudFormationEvent https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-requesttypes.html   # noqa: E501
    Attributes:
    ----------
    RequestType: str
    RequestId: str
    ResponseURL: str
    ResourceType: bool
    LogicalResourceId: str
    StackId: str
    ResourceProperties: Dict[str, Any]
    PhysicalResourceId: Optional[str] Only in Update/Delete events
    OldResourceProperties: Optional[Dict[str, Any]] Only in Update events
    """

    RequestType: str
    RequestId: str
    ResponseURL: str
    ResourceType: str
    LogicalResourceId: str
    StackId: str
    ResourceProperties: Dict[str, Any]
    PhysicalResourceId: Optional[str]
    OldResourceProperties: Optional[Dict[str, Any]]
