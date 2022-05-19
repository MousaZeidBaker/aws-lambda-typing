from aws_lambda_typing.events import (
    CognitoCustomMessageAdminCreateUserEvent,
    CognitoCustomMessageAuthenticationEvent,
    CognitoCustomMessageForgotPasswordEvent,
    CognitoCustomMessageResendCodeEvent,
    CognitoCustomMessageSignUpEvent,
    CognitoCustomMessageUpdateUserAttributeEvent,
    CognitoCustomMessageVerifyUserAttributeEvent,
)


def test_cognito_custom_message_sign_up_event() -> None:
    event: CognitoCustomMessageSignUpEvent = {
        "version": "1",
        "triggerSource": "CustomMessage_SignUp",
        "region": "us-west-2",
        "userPoolId": "poolid",
        "userName": "userName",
        "callerContext": {
            "awsSdkVersion": "1",
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
            "smsMessage": "<custom message to be sent in the message with code parameter>",  # noqa: E501
            "emailMessage": "<custom message to be sent in the message with code parameter>",  # noqa: E501
            "emailSubject": "<custom email subject>",
        },
    }


def test_cognito_custom_message_admin_create_user_event() -> None:
    event: CognitoCustomMessageAdminCreateUserEvent = {
        "version": "1",
        "triggerSource": "CustomMessage_AdminCreateUser",
        "region": "us-west-2",
        "userPoolId": "poolid",
        "userName": "userName",
        "callerContext": {
            "awsSdkVersion": "1",
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
            "smsMessage": "<custom message to be sent in the message with code parameter>",  # noqa: E501
            "emailMessage": "<custom message to be sent in the message with code parameter>",  # noqa: E501
            "emailSubject": "<custom email subject>",
        },
    }


def test_cognito_custom_message_resend_code_event() -> None:
    event: CognitoCustomMessageResendCodeEvent = {
        "version": "1",
        "triggerSource": "CustomMessage_ResendCode",
        "region": "us-west-2",
        "userPoolId": "poolid",
        "userName": "userName",
        "callerContext": {
            "awsSdkVersion": "1",
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
            "smsMessage": "<custom message to be sent in the message with code parameter>",  # noqa: E501
            "emailMessage": "<custom message to be sent in the message with code parameter>",  # noqa: E501
            "emailSubject": "<custom email subject>",
        },
    }


def test_cognito_custom_message_forgot_password_event() -> None:
    event: CognitoCustomMessageForgotPasswordEvent = {
        "version": "1",
        "triggerSource": "CustomMessage_ForgotPassword",
        "region": "us-west-2",
        "userPoolId": "poolid",
        "userName": "userName",
        "callerContext": {
            "awsSdkVersion": "1",
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
            "smsMessage": "<custom message to be sent in the message with code parameter>",  # noqa: E501
            "emailMessage": "<custom message to be sent in the message with code parameter>",  # noqa: E501
            "emailSubject": "<custom email subject>",
        },
    }


def test_cognito_custom_message_update_user_attribute_event() -> None:
    event: CognitoCustomMessageUpdateUserAttributeEvent = {
        "version": "1",
        "triggerSource": "CustomMessage_UpdateUserAttribute",
        "region": "us-west-2",
        "userPoolId": "poolid",
        "userName": "userName",
        "callerContext": {
            "awsSdkVersion": "1",
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
            "smsMessage": "<custom message to be sent in the message with code parameter>",  # noqa: E501
            "emailMessage": "<custom message to be sent in the message with code parameter>",  # noqa: E501
            "emailSubject": "<custom email subject>",
        },
    }


def test_cognito_custom_message_verify_user_attribute_event() -> None:
    event: CognitoCustomMessageVerifyUserAttributeEvent = {
        "version": "1",
        "triggerSource": "CustomMessage_VerifyUserAttribute",
        "region": "us-west-2",
        "userPoolId": "poolid",
        "userName": "userName",
        "callerContext": {
            "awsSdkVersion": "1",
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
            "smsMessage": "<custom message to be sent in the message with code parameter>",  # noqa: E501
            "emailMessage": "<custom message to be sent in the message with code parameter>",  # noqa: E501
            "emailSubject": "<custom email subject>",
        },
    }


def test_cognito_custom_message_authentication_event() -> None:
    event: CognitoCustomMessageAuthenticationEvent = {
        "version": "1",
        "triggerSource": "CustomMessage_Authentication",
        "region": "us-west-2",
        "userPoolId": "poolid",
        "userName": "userName",
        "callerContext": {
            "awsSdkVersion": "1",
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
            "smsMessage": "<custom message to be sent in the message with code parameter>",  # noqa: E501
            "emailMessage": "<custom message to be sent in the message with code parameter>",  # noqa: E501
            "emailSubject": "<custom email subject>",
        },
    }
