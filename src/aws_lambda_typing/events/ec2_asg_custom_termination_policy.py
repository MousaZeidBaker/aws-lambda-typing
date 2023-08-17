#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import List, Literal, TypedDict
else:
    from typing import List

    from typing_extensions import Literal, TypedDict


class Capacity(TypedDict):
    """
    Capacity

    Attributes:
    ----------
    AvailabilityZone: str

    Capacity: int

    InstanceMarketOption: Literal['on-demand', 'spot']
    """

    AvailabilityZone: str
    Capacity: int
    InstanceMarketOption: Literal[
        "on-demand",
        "spot",
    ]


class Instance(TypedDict):
    """
    Instance

    Attributes:
    ----------
    AvailabilityZone: str

    InstanceId: str

    InstanceType: str

    InstanceMarketOption: Literal['on-demand', 'spot']
    """

    AvailabilityZone: str
    InstanceId: str
    InstanceType: str
    InstanceMarketOption: Literal[
        "on-demand",
        "spot",
    ]


class EC2ASGCustomTerminationPolicyEvent(TypedDict):
    """
    EC2ASGCustomTerminationPolicyEvent
    https://docs.aws.amazon.com/autoscaling/ec2/userguide/lambda-custom-termination-policy.html

    Attributes:
    ----------
    AutoScalingGroupARN: str

    AutoScalingGroupName: str

    CapacityToTerminate: List[:py:class:`CapacityToTerminate`]

    Instances: List[:py:class:`Instances`]

    Cause: Literal[
        'SCALE_IN',
        'INSTANCE_REFRESH',
        'MAX_INSTANCE_LIFETIME',
        'REBALANCE'
    ]
    """

    AutoScalingGroupARN: str
    AutoScalingGroupName: str
    CapacityToTerminate: List[Capacity]
    Instances: List[Instance]
    Cause: Literal[
        "SCALE_IN",
        "INSTANCE_REFRESH",
        "MAX_INSTANCE_LIFETIME",
        "REBALANCE",
    ]
