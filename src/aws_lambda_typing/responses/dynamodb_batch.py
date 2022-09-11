#!/usr/bin/env python

import sys

if sys.version_info >= (3, 8):
    from typing import List, TypedDict
else:
    from typing import List

    from typing_extensions import TypedDict


class BatchItemFailure(TypedDict):
    """
    BatchItemFailure

    Attributes:
    ----------
    itemIdentifier: str
    """

    itemIdentifier: str


class DynamoDBBatchResponse(TypedDict):
    """
    DynamoDBBatchResponse
    https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-ddb-batchfailurereporting

    Attributes:
    ----------
    batchItemFailures: List[:py:class:`BatchItemFailure`]
    """

    batchItemFailures: List[BatchItemFailure]
