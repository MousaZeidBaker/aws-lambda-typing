from aws_lambda_typing.events import CloudFormationEvent


def test_cloudformation_event() -> None:
    event: CloudFormationEvent = {
        "RequestType" : "Update",
        "RequestId" : "unique id for this update request",
        "ResponseURL" : "pre-signed-url-for-update-response",
        "ResourceType" : "Custom::MyCustomResourceType",
        "LogicalResourceId" : "name of resource in template",
        "StackId" : "arn:aws:cloudformation:us-east-2:123456789012:stack/mystack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0136786",
        "PhysicalResourceId" :"custom resource provider-defined physical id",
        "ResourceProperties" : {
            "key1" : "new-string",
            "key2" : [ "new-list" ],
            "key3" : { "key4" : "new-map" }
        },
        "OldResourceProperties" : {
            "key1" : "string",
            "key2" : [ "list" ],
            "key3" : { "key4" : "map" }
        }
    }
