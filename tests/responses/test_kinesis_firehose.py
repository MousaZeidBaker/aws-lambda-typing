from aws_lambda_typing.responses import KinesisFirehoseTransformationResponse


def test_kinesis_firehose_transformation_responses() -> None:
    response: KinesisFirehoseTransformationResponse = {
        "records": [
            {
                "recordId": "record1",
                "result": "Ok",
                "data": "SGVsbG8sIHdvcmxkIQo=",  # base64-d 'Hello, world!'
            },
            {
                "recordId": "record2",
                "result": "Dropped",
                "data": "SGVsbG8sIHdvcmxkIQo=",  # base64-d 'Hello, world!'
            },
            {
                "recordId": "record3",
                "result": "ProcessingFailed",
                "data": "SGVsbG8sIHdvcmxkIQo=",  # base64-d 'Hello, world!'
            },
        ],
    }
