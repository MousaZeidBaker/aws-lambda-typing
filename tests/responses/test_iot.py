from aws_lambda_typing.responses import IoTPreProvisioningHookResponse


def test_iot_pre_provisioning_hook_response() -> None:
    response: IoTPreProvisioningHookResponse = {
        "allowProvisioning": True,
        "parameterOverrides": {
            "Key": "newCustomValue",
        },
    }
