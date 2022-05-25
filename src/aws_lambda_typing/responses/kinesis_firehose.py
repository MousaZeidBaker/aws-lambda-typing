#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import List, Literal, TypedDict
else:
    from typing import List

    from typing_extensions import Literal, TypedDict


KinesisFirehoseTransformationResponseResultCode = Literal[
    "Ok",
    "Dropped",
    "ProcessingFailed",
]


class KinesisFirehoseTransformationResponseResult(TypedDict):
    """
    KinesisFirehoseTransformationResponseResult

    Attributes:
    ----------
    recordId: str

    result: Literal["Ok", "Dropped", "ProcessingFailed"]

    data: str
    """

    recordId: str
    result: KinesisFirehoseTransformationResponseResultCode
    data: str


class KinesisFirehoseTransformationResponse(TypedDict):
    """
    KinesisFirehoseTransformationResponse
    https://docs.aws.amazon.com/firehose/latest/dev/data-transformation.html

    Attributes:
    ----------
    records: List[:py:class:`KinesisFirehoseTransformationResponseResult`]
    """

    records: List[KinesisFirehoseTransformationResponseResult]
