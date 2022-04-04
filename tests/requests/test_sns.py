from aws_lambda_typing.requests import SNSPublish
from aws_lambda_typing.requests import SNSPublishBatch


def test_sns_publish() -> None:
    request: SNSPublish = {
        "Message": "Hello World",
        "MessageAttributes": {
            "string": {
                "DataType": "string",
                "StringValue": "string",
                "BinaryValue": b"bytes"
            }
        },
        "MessageDeduplicationId": "string",
        "MessageGroupId": "string",
        "MessageStructure": "json",
        "PhoneNumber": "string",
        "Subject": "string",
        "TargetArn": "string",
        "TopicArn": "string",
    }

def test_sns_publish_batch() -> None:
    request: SNSPublishBatch = {
        "TopicArn": "string",
        "PublishBatchRequestEntries": [
            {
                "Id": "string",
                "Message": "Hello World",
                "MessageAttributes": {
                    "string": {
                        "DataType": "string",
                        "StringValue": "string",
                        "BinaryValue": b"bytes"
                    }
                },
                "MessageDeduplicationId": "string",
                "MessageGroupId": "string",
                "MessageStructure": "json",
                "Subject": "string",
            }
        ]
    }
