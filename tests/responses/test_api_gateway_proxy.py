from aws_lambda_typing.responses import (
    APIGatewayProxyResponseV1,
    APIGatewayProxyResponseV2,
)


def test_api_gateway_proxy_event_v1() -> None:
    response: APIGatewayProxyResponseV1 = {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "isBase64Encoded": False,
        "multiValueHeaders": {
            "X-Custom-Header": ["My value", "My other value"],
        },
        "body": '{\n  "TotalCodeSize": 104330022,\n  "FunctionCount": 26\n}',
    }


def test_api_gateway_proxy_event_v2() -> None:
    response: APIGatewayProxyResponseV2 = {
        "cookies": [],
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": '{\n  "TotalCodeSize": 104330022,\n  "FunctionCount": 26\n}',
    }
