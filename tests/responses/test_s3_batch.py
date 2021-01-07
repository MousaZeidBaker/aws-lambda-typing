import aws_lambda_typing as lambda_typing


def test_s3_batch_response() -> None:
    dummy: lambda_typing.S3BatchResponse = {
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
