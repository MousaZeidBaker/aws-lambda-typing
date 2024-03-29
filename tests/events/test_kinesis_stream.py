from aws_lambda_typing.events import KinesisStreamEvent


def test_kinesis_stream_event() -> None:
    event: KinesisStreamEvent = {
        "Records": [
            {
                "kinesis": {
                    "kinesisSchemaVersion": "1.0",
                    "partitionKey": "1",
                    "sequenceNumber": "49590338271490256608559692538361571095921575989136588898",  # noqa: E501
                    "data": "SGVsbG8sIHRoaXMgaXMgYSB0ZXN0Lg==",
                    "approximateArrivalTimestamp": 1545084650.987,
                },
                "eventSource": "aws:kinesis",
                "eventVersion": "1.0",
                "eventID": "shardId-000000000006:49590338271490256608559692538361571095921575989136588898",  # noqa: E501
                "eventName": "aws:kinesis:record",
                "invokeIdentityArn": "arn:aws:iam::123456789012:role/lambda-role",  # noqa: E501
                "awsRegion": "us-east-2",
                "eventSourceARN": "arn:aws:kinesis:us-east-2:123456789012:stream/lambda-stream",  # noqa: E501
            },
            {
                "kinesis": {
                    "kinesisSchemaVersion": "1.0",
                    "partitionKey": "1",
                    "sequenceNumber": "49590338271490256608559692540925702759324208523137515618",  # noqa: E501
                    "data": "VGhpcyBpcyBvbmx5IGEgdGVzdC4=",
                    "approximateArrivalTimestamp": 1545084711.166,
                },
                "eventSource": "aws:kinesis",
                "eventVersion": "1.0",
                "eventID": "shardId-000000000006:49590338271490256608559692540925702759324208523137515618",  # noqa: E501
                "eventName": "aws:kinesis:record",
                "invokeIdentityArn": "arn:aws:iam::123456789012:role/lambda-role",  # noqa: E501
                "awsRegion": "us-east-2",
                "eventSourceARN": "arn:aws:kinesis:us-east-2:123456789012:stream/lambda-stream",  # noqa: E501
            },
        ]
    }
