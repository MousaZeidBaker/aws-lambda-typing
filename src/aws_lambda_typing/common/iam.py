#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Dict, List, Literal, TypedDict, Union
else:
    from typing import Dict, List, Union

    from typing_extensions import Literal, TypedDict


class Principal(TypedDict, total=False):
    """
    Principal
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html

    Attributes:
    ----------
    AWS: Union[str, List[str]]

    CanonicalUser: Union[str, List[str]]

    Federated: Union[str, List[str]]

    Service: Union[str, List[str]]

    """

    AWS: Union[str, List[str]]
    CanonicalUser: Union[str, List[str]]
    Federated: Union[str, List[str]]
    Service: Union[str, List[str]]


class _Statement(TypedDict):
    """
    Base class used to define required attributes
    - https://peps.python.org/pep-0589/#totality

    Attributes:
    ----------
    Effect: Literal["Allow", "Deny"]
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_effect.html
    """

    Effect: Literal[
        "Allow",
        "Deny",
    ]


class Statement(_Statement, total=False):
    """
    Statement
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_statement.html

    Attributes:
    ----------
    Sid: str
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_sid.html

    Principal: Union[Literal["*"], :py:class:`Principal`]
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html

    NotPrincipal: :py:class:`Principal`
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_notprincipal.html

    Action: Union[str, List[str]]
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_action.html
    - At least one of Action/NotAction must be specified

    NotAction: Union[str, List[str]]
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_notaction.html
    - At least one of Action/NotAction must be specified

    Resource: Union[str, List[str]]
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html
    - At least one of Resource/NotResource must be specified

    NotResource: Union[str, List[str]]
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_notresource.html
    - At least one of Resource/NotResource must be specified

    Condition: Dict[str, Dict[str, Union[str, List[str]]]]
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html
    """

    Sid: str
    Principal: Union[Literal["*"], Principal]
    NotPrincipal: Principal
    Action: Union[str, List[str]]
    NotAction: Union[str, List[str]]
    Resource: Union[str, List[str]]
    NotResource: Union[str, List[str]]
    Condition: Dict[str, Dict[str, Union[str, List[str]]]]


class _PolicyDocument(TypedDict):
    """
    Base class used to define required attributes
    - https://peps.python.org/pep-0589/#totality

    Attributes:
    ----------
    Version: str
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_version.html

    Statement: Union[:py:class:`Statement`, List[:py:class:`Statement`]]
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_statement.html
    """

    Version: Literal["2012-10-17", "2008-10-17"]
    Statement: Union[Statement, List[Statement]]


class PolicyDocument(_PolicyDocument, total=False):
    """
    PolicyDocument
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html

    Attributes:
    ----------
    Id: str
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_id.html
    """

    Id: str
