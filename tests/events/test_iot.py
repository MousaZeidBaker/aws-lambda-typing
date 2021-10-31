from aws_lambda_typing.events import IoTPreProvisioningHookEvent


def test_iot_pre_provisioning_hook_event() -> None:
    event: IoTPreProvisioningHookEvent = {
        "claimCertificateId": "string",
        "certificateId": "string",
        "certificatePem": "string",
        "templateArn": "arn:aws:iot:us-east-1:1234567890:provisioningtemplate/MyTemplate",  # noqa: E501
        "clientId": "221a6d10-9c7f-42f1-9153-e52e6fc869c1",
        "parameters": {
            "string": "string",
        },
    }
