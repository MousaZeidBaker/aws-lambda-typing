from aws_lambda_typing.responses import APIGatewayAuthorizerResponse


def test_iot_pre_provisioning_hook_response() -> None:
    response: APIGatewayAuthorizerResponse = {
        "principalId": "user",
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": "Deny",
                    "Resource": "arn:aws:execute-api:us-west-2:123456789012:ymy8tbxw7b/dev/GET/",  # noqa: E501
                }
            ],
        },
    }
