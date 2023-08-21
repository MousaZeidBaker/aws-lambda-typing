from aws_lambda_typing.responses import DynamoDBBatchResponse


def test_dynamodb_batch_response() -> None:
    response: DynamoDBBatchResponse = {
        "batchItemFailures": [
            {
                "itemIdentifier": "f3ed1a77c",
            }
        ],
    }
