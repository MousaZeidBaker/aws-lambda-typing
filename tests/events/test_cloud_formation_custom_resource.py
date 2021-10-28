from aws_lambda_typing.events import (
    CloudFormationCustomResourceCreateEvent,
    CloudFormationCustomResourceDeleteEvent,
    CloudFormationCustomResourceEvent,
    CloudFormationCustomResourceUpdateEvent,
)


def test_cloud_formation_custom_resource_event() -> None:
    event: CloudFormationCustomResourceEvent = {
        "RequestType": "Create",
        "RequestId": "unique id for this create request",
        "ResponseURL": "pre-signed-url-for-create-response",
        "ResourceType": "Custom::MyCustomResourceType",
        "LogicalResourceId": "name of resource in template",
        "StackId": "arn:aws:cloudformation:us-east-2:123456789012:stack/mystack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0136786",  # noqa: E501
        "ResourceProperties": {
            "key1": "new-string",
            "key2": ["new-list"],
            "key3": {"key4": "new-map"},
        },
    }


def test_cloud_formation_custom_resource_create_event() -> None:
    event: CloudFormationCustomResourceCreateEvent = {
        "RequestType": "Create",
        "RequestId": "unique id for this create request",
        "ResponseURL": "pre-signed-url-for-create-response",
        "ResourceType": "Custom::MyCustomResourceType",
        "LogicalResourceId": "name of resource in template",
        "StackId": "arn:aws:cloudformation:us-east-2:123456789012:stack/mystack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0136786",  # noqa: E501
        "ResourceProperties": {
            "key1": "new-string",
            "key2": ["new-list"],
            "key3": {"key4": "new-map"},
        },
    }


def test_cloud_formation_custom_resource_update_event() -> None:
    event: CloudFormationCustomResourceUpdateEvent = {
        "RequestType": "Update",
        "RequestId": "unique id for this update request",
        "ResponseURL": "pre-signed-url-for-update-response",
        "ResourceType": "Custom::MyCustomResourceType",
        "LogicalResourceId": "name of resource in template",
        "StackId": "arn:aws:cloudformation:us-east-2:123456789012:stack/mystack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0136786",  # noqa: E501
        "PhysicalResourceId": "custom resource provider-defined physical id",
        "ResourceProperties": {
            "key1": "new-string",
            "key2": ["new-list"],
            "key3": {"key4": "new-map"},
        },
        "OldResourceProperties": {
            "key1": "string",
            "key2": ["list"],
            "key3": {"key4": "map"},
        },
    }


def test_cloud_formation_custom_resource_delete_event() -> None:
    event: CloudFormationCustomResourceDeleteEvent = {
        "RequestType": "Delete",
        "RequestId": "unique id for this delete request",
        "ResponseURL": "pre-signed-url-for-delete-response",
        "ResourceType": "Custom::MyCustomResourceType",
        "LogicalResourceId": "name of resource in template",
        "StackId": "arn:aws:cloudformation:us-east-2:123456789012:stack/mystack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0136786",  # noqa: E501
        "PhysicalResourceId": "custom resource provider-defined physical id",
        "ResourceProperties": {
            "key1": "new-string",
            "key2": ["new-list"],
            "key3": {"key4": "new-map"},
        },
    }