from aws_lambda_typing.responses import S3BatchResponse


def test_s3_batch_response() -> None:
    response: S3BatchResponse = {
        "invocationSchemaVersion": "1.0",
        "treatMissingKeysAs": "PermanentFailure",
        "invocationId": "YXNkbGZqYWRmaiBhc2RmdW9hZHNmZGpmaGFzbGtkaGZza2RmaAo",
        "results": [
            {
                "taskId": "dGFza2lkZ29lc2hlcmUK",
                "resultCode": "Succeeded",
                "resultString": "['Alice', 'Bob']"
            }
        ]
    }
