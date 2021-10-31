#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Dict, TypedDict
else:
    from typing import Dict

    from typing_extensions import TypedDict


class IoTPreProvisioningHookEvent(TypedDict):
    """
    IoTPreProvisioningHookEvent
    https://docs.aws.amazon.com/iot/latest/developerguide/pre-provisioning-hook.html

    Attributes:
    ----------
    claimCertificateId: str

    certificateId: str

    certificatePem: str

    templateArn: str

    clientId: str

    parameters: Dict[str, str]
    """

    claimCertificateId: str
    certificateId: str
    certificatePem: str
    templateArn: str
    clientId: str
    parameters: Dict[str, str]
