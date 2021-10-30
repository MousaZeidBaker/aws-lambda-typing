from aws_lambda_typing.events import SecretsManagerRotationEvent


def test_secrets_manager_create_secret_event() -> None:
    event: SecretsManagerRotationEvent = {
        "Step": "createSecret",
        "SecretId": "MyTestDatabaseSecret",
        "ClientRequestToken": "3749bce8-dc74-49fb-9272-c2c736211350",
    }


def test_secrets_manager_set_secret_event() -> None:
    event: SecretsManagerRotationEvent = {
        "Step": "setSecret",
        "SecretId": "MyTestDatabaseSecret",
        "ClientRequestToken": "3749bce8-dc74-49fb-9272-c2c736211350",
    }


def test_secrets_manager_test_secret_event() -> None:
    event: SecretsManagerRotationEvent = {
        "Step": "setSecret",
        "SecretId": "MyTestDatabaseSecret",
        "ClientRequestToken": "3749bce8-dc74-49fb-9272-c2c736211350",
    }


def test_secrets_manager_finish_secret_event() -> None:
    event: SecretsManagerRotationEvent = {
        "Step": "finishSecret",
        "SecretId": "MyTestDatabaseSecret",
        "ClientRequestToken": "3749bce8-dc74-49fb-9272-c2c736211350",
    }
