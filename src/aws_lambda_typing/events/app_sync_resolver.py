#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Any, Dict, List, TypedDict, Union
else:
    from typing import Any, Dict, List, Union

    from typing_extensions import TypedDict


class AppSyncInfo(TypedDict):
    """
    AppSyncInfo

    Attributes:
    ----------
    selectionSetList: List[str]

    selectionSetGraphQL: str

    parentTypeName: str

    fieldName: str

    variables: Dict[str, Any]
    """

    selectionSetList: List[str]
    selectionSetGraphQL: str
    parentTypeName: str
    fieldName: str
    variables: Dict[str, Any]


class AppSyncPrev(TypedDict):
    """
    AppSyncPrev

    Attributes:
    ----------
    result: Dict[str, Any]
    """

    result: Dict[str, Any]


class AppSyncRequest(TypedDict):
    """
    AppSyncRequest

    Attributes:
    ----------
    headers: Dict[str, str]
    """

    headers: Dict[str, str]


class AppSyncIdentityIAM(TypedDict):
    """
    AppSyncIdentityIAM

    Attributes:
    ----------
    accountId: str

    cognitoIdentityPoolId: str

    cognitoIdentityId: str

    sourceIp: List[str]

    username: str

    userArn: str

    cognitoIdentityAuthType: str

    cognitoIdentityAuthProvider: str
    """

    accountId: str
    cognitoIdentityPoolId: str
    cognitoIdentityId: str
    sourceIp: List[str]
    username: str
    userArn: str
    cognitoIdentityAuthType: str
    cognitoIdentityAuthProvider: str


class AppSyncIdentityCognito(TypedDict):
    """
    AppSyncIdentityCognito

    Attributes:
    ----------
    sub: str

    issuer: str

    username: str

    claims: Any

    sourceIp: List[str]

    defaultAuthStrategy: str

    groups: Union[List[str], None]
    """

    sub: str
    issuer: str
    username: str
    claims: Any
    sourceIp: List[str]
    defaultAuthStrategy: str
    groups: Union[List[str], None]


class AppSyncIdentityOIDC(TypedDict):
    """
    AppSyncIdentityOIDC

    Attributes:
    ----------
    claims: Any

    issuer: str

    sub: str
    """

    claims: Any
    issuer: str
    sub: str


class AppSyncIdentityLambda(TypedDict):
    """
    AppSyncIdentityLambda

    Attributes:
    ----------
    resolverContext: Any
    """

    resolverContext: Any


class AppSyncResolverEvent(TypedDict):
    """
    AppSyncResolverEvent
    https://docs.aws.amazon.com/appsync/latest/devguide/resolver-context-reference.html

    Attributes:
    ----------
    arguments: Dict

    identity: Union[
        :py:class:`AppSyncIdentityIAM`,
        :py:class:`AppSyncIdentityCognito`,
        :py:class:`AppSyncIdentityOIDC`,
        :py:class:`AppSyncIdentityLambda`
    ]

    source: Union[Dict, None]

    stash: Dict[str, Any]

    request: :py:class:`AppSyncRequest`

    prev: Union[:py:class:`AppSyncPrev`, None]

    info: :py:class:`AppSyncInfo`
    """

    arguments: Dict
    identity: Union[
        AppSyncIdentityIAM,
        AppSyncIdentityCognito,
        AppSyncIdentityOIDC,
        AppSyncIdentityLambda,
    ]
    source: Union[Dict, None]
    stash: Dict[str, Any]
    request: AppSyncRequest
    prev: Union[AppSyncPrev, None]
    info: AppSyncInfo
