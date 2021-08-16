#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


class ConfigEvent(TypedDict):
    """
    MQEvent https://docs.aws.amazon.com/lambda/latest/dg/services-config.html

    Attributes:
    ----------
    invokingEvent: str

    ruleParameters: str

    resultToken: str

    eventLeftScope: bool

    executionRoleArn: str

    configRuleArn: str

    configRuleName: str

    configRuleId: str

    accountId: str

    version: str
    """

    invokingEvent: str
    ruleParameters: str
    resultToken: str
    eventLeftScope: bool
    executionRoleArn: str
    configRuleArn: str
    configRuleName: str
    configRuleId: str
    accountId: str
    version: str
