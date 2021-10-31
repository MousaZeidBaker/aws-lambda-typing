#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import Dict, TypedDict
else:
    from typing import Dict

    from typing_extensions import TypedDict


class IoTPreProvisioningHookResponse(TypedDict):
    """
    IoTPreProvisioningHookEvent
    https://docs.aws.amazon.com/iot/latest/developerguide/pre-provisioning-hook.html

    Attributes:
    ----------
    allowProvisioning: bool

    parameterOverrides: Dict[str, str]
    """

    allowProvisioning: bool
    parameterOverrides: Dict[str, str]
