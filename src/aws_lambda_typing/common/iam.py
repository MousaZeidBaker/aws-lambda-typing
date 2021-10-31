#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Dict, List, Literal, Optional, TypedDict, Union
else:
    from typing import Dict, List, Optional, Union

    from typing_extensions import Literal, TypedDict


class Statement(TypedDict, total=False):
    """
    Statement
    https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_statement.html

    Attributes:
    ----------
    Principal: Optional[Union[str, List[str], Dict[str, Union[str, List[str]]]]]

    NotPrincipal: Optional[
        Union[str, List[str], Dict[str, Union[str, List[str]]]]
    ]

    Action: Optional[Union[str, List[str]]]

    NotAction: Optional[Union[str, List[str]]]

    Resource: Optional[Union[str, List[str]]]

    NotResource: Optional[Union[str, List[str]]]

    Condition: Optional[Dict[str, Dict[str, Union[str, List[str]]]]]
    """

    Sid: Optional[str]
    Effect: Literal[
        "Allow",
        "Deny",
    ]
    Principal: Optional[Union[str, List[str], Dict[str, Union[str, List[str]]]]]
    NotPrincipal: Optional[
        Union[str, List[str], Dict[str, Union[str, List[str]]]]
    ]
    Action: Optional[Union[str, List[str]]]
    NotAction: Optional[Union[str, List[str]]]
    Resource: Optional[Union[str, List[str]]]
    NotResource: Optional[Union[str, List[str]]]
    Condition: Optional[Dict[str, Dict[str, Union[str, List[str]]]]]


class PolicyDocument(TypedDict, total=False):
    """
    PolicyDocument
    https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html

    Attributes:
    ----------
    Version: str

    Id: Optional[str]

    Statement: List[:py:class:`Statement`]
    """

    Version: str
    Id: Optional[str]
    Statement: List[Statement]
