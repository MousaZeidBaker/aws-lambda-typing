#!/usr/bin/env python

import typing


class ConfigEvent(typing.TypedDict):
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
