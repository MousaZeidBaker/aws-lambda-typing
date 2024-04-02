from aws_lambda_typing.events import SQSEvent


def test_sqs_event_standard_queue() -> None:
    event: SQSEvent = {
        "Records": [
            {
                "messageId": "059f36b4-87a3-44ab-83d2-661975830a7d",
                "receiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a...",
                "body": "Test message.",
                "attributes": {
                    "ApproximateReceiveCount": "1",
                    "SentTimestamp": "1545082649183",
                    "SenderId": "AIDAIENQZJOLO23YVJ4VO",
                    "ApproximateFirstReceiveTimestamp": "1545082649185",
                },
                "messageAttributes": {},
                "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
                "eventSource": "aws:sqs",
                "eventSourceARN": "arn:aws:sqs:us-east-2:123456789012:my-queue",
                "awsRegion": "us-east-2",
            },
            {
                "messageId": "2e1424d4-f796-459a-8184-9c92662be6da",
                "receiptHandle": "AQEBzWwaftRI0KuVm4tP+/7q1rGgNqicHq...",
                "body": "Test message.",
                "attributes": {
                    "ApproximateReceiveCount": "1",
                    "SentTimestamp": "1545082650636",
                    "SenderId": "AIDAIENQZJOLO23YVJ4VO",
                    "ApproximateFirstReceiveTimestamp": "1545082650649",
                },
                "messageAttributes": {},
                "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
                "eventSource": "aws:sqs",
                "eventSourceARN": "arn:aws:sqs:us-east-2:123456789012:my-queue",
                "awsRegion": "us-east-2",
            },
        ]
    }


def test_sqs_event_fifo_queue() -> None:
    event: SQSEvent = {
        "Records": [
            {
                "messageId": "11d6ee51-4cc7-4302-9e22-7cd8afdaadf5",
                "receiptHandle": "AQEBBX8nesZEXmkhsmZeyIE8iQAMig7qw...",
                "body": "Test message.",
                "attributes": {
                    "ApproximateReceiveCount": "1",
                    "SentTimestamp": "1573251510774",
                    "SequenceNumber": "18849496460467696128",
                    "MessageGroupId": "1",
                    "SenderId": "AIDAIO23YVJENQZJOL4VO",
                    "MessageDeduplicationId": "1",
                    "ApproximateFirstReceiveTimestamp": "1573251510774",
                },
                "messageAttributes": {},
                "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
                "eventSource": "aws:sqs",
                "eventSourceARN": "arn:aws:sqs:us-east-2:123456789012:fifo",
                "awsRegion": "us-east-2",
            }
        ]
    }


def test_sqs_event_message_attributes() -> None:
    event: SQSEvent = {
        "Records": [
            {
                "messageId": "b9d7aba9-30ea-4e72-8f44-585b8045fe2c",
                "receiptHandle": "AQEB7+aJcKwp6VVxs0A7M8o7TMgB/QQb+...",
                "body": "Test message.",
                "attributes": {
                    "DeadLetterQueueSourceArn": "arn:aws:sqs:us-east-1:123...",
                    "ApproximateReceiveCount": "2",
                    "AWSTraceHeader": "Root=1-afa8dcdd-00db74c9;Parent=6df...",
                    "SentTimestamp": "1711115795107",
                    "SenderId": "AIDAIO23YVJENQZJOL4VO:my-lambda",
                    "ApproximateFirstReceiveTimestamp": "1711115795116",
                },
                "messageAttributes": {
                    "attribute_1": {
                        "stringValue": "value_1",
                        "binaryValue": None,
                        "stringListValues": [],
                        "binaryListValues": [],
                        "dataType": "String",
                    }
                },
                "md5OfMessageAttributes": "d326d59e52374ec1d1ff87040b56c09d",
                "md5OfBody": "e6c926f2b6defe3812e91283a68e5f43",
                "eventSource": "aws:sqs",
                "eventSourceARN": "arn:aws:sqs:us-east-1:123456789012:queue",
                "awsRegion": "us-east-1",
            }
        ]
    }
