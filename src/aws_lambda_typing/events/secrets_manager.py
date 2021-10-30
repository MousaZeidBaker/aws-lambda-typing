#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Literal, TypedDict
else:
    from typing_extensions import Literal, TypedDict


class SecretsManagerRotationEvent(TypedDict):
    """
    SecretsManagerRotationEvent
    https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets-lambda-function-overview.html

    Attributes:
    ----------
    Step: Literal["createSecret", "setSecret", "testSecret", "finishSecret"]

    SecretId: str

    ClientRequestToken: str
    """

    Step: Literal[
        "createSecret",
        "setSecret",
        "testSecret",
        "finishSecret",
    ]
    SecretId: str
    ClientRequestToken: str
