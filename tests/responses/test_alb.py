from aws_lambda_typing.responses import ALBResponse


def test_app_sync_resolver_event() -> None:
    event: ALBResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "statusDescription": "200 OK",
        "headers": {
            "Set-cookie": "cookies",
            "Content-Type": "application/json",
        },
        "body": "Hello from Lambda (optional)",
    }
