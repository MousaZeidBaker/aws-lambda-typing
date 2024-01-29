from aws_lambda_typing.events import (
    CognitoPostConfirmationForgotPasswordEvent,
    CognitoPostConfirmationSignUpEvent,
)


def test_cognito_post_confirmation_forgot_password_event() -> None:
    event: CognitoPostConfirmationForgotPasswordEvent = {
        "version": "1",
        "triggerSource": "PostConfirmation_ConfirmForgotPassword",
        "region": "us-west-2",
        "userPoolId": "poolid",
        "userName": "userName",
        "callerContext": {
            "awsSdkVersion": "1",
            "clientId": "jkSDFasdfnsq",
        },
        "request": {
            "userAttributes": {
                "sub": "cc0a8a56-9b57-4cd1-a92e-e020bf6d3ab0",
                "given_name": "John",
                "family_name": "Doe",
            },
            "clientMetadata": {
                "environment": "development",
            },
        },
        "response": {},
    }


def test_cognito_post_confirmation_sign_up_event() -> None:
    event: CognitoPostConfirmationSignUpEvent = {
        "version": "1",
        "triggerSource": "PostConfirmation_ConfirmSignUp",
        "region": "us-west-2",
        "userPoolId": "poolid",
        "userName": "userName",
        "callerContext": {
            "awsSdkVersion": "1",
            "clientId": "jkSDFasdfnsq",
        },
        "request": {
            "userAttributes": {
                "sub": "cc0a8a56-9b57-4cd1-a92e-e020bf6d3ab0",
                "given_name": "John",
                "family_name": "Doe",
            },
            "clientMetadata": {
                "environment": "development",
            },
        },
        "response": {},
    }
