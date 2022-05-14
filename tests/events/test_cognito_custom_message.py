from aws_lambda_typing.events import CognitoCustomMessage


def test_cognito_custom_message_event() -> None:
    event: CognitoCustomMessage = {
        "version": 1,
        "triggerSource": "CustomMessage_SignUp",
        "region": "us-west-2",
        "userPoolId": "poolid",
        "userName": "userName",
        "callerContext": {
            "awsSdk": "1",
            "clientId": "jkSDFasdfnsq",
        },
        "request": {
            "userAttributes": {
                "phone_number_verified": False,
                "email_verified": True,
            },
            "codeParameter": "####",
        },
        "response": {
            "smsMessage": "<custom message to be sent in the message with code parameter>",
            "emailMessage": "<custom message to be sent in the message with code parameter>",
            "emailSubject": "<custom email subject>",
        },
    }
