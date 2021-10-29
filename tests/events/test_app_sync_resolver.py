from aws_lambda_typing.events import AppSyncResolverEvent


def test_app_sync_resolver_event() -> None:
    event: AppSyncResolverEvent = {
        "arguments": {"id": "my identifier"},
        "identity": {
            "claims": {
                "sub": "192879fc-a240-4bf1-ab5a-d6a00f3063f9",
                "email_verified": True,
                "iss": "https://cognito-idp.us-west-2.amazonaws.com/us-west-xxxxxxxxxxx",  # noqa: E501
                "phone_number_verified": False,
                "cognito:username": "jdoe",
                "aud": "7471s60os7h0uu77i1tk27sp9n",
                "event_id": "bc334ed8-a938-4474-b644-9547e304e606",
                "token_use": "id",
                "auth_time": 1599154213,
                "phone_number": "+19999999999",
                "exp": 1599157813,
                "iat": 1599154213,
                "email": "jdoe@email.com",
            },
            "defaultAuthStrategy": "ALLOW",
            "groups": None,
            "issuer": "https://cognito-idp.us-west-2.amazonaws.com/us-west-xxxxxxxxxxx",  # noqa: E501
            "sourceIp": ["1.1.1.1"],
            "sub": "192879fc-a240-4bf1-ab5a-d6a00f3063f9",
            "username": "jdoe",
        },
        "source": None,
        "request": {
            "headers": {
                "x-forwarded-for": "1.1.1.1, 2.2.2.2",
                "cloudfront-viewer-country": "US",
                "cloudfront-is-tablet-viewer": "False",
                "via": "2.0 xxxxxxxxxxxxxxxx.cloudfront.net (CloudFront)",
                "cloudfront-forwarded-proto": "https",
                "origin": "https://us-west-1.console.aws.amazon.com",
                "content-length": "217",
                "accept-language": "en-US,en;q=0.9",
                "host": "xxxxxxxxxxxxxxxx.appsync-api.us-west-1.amazonaws.com",
                "x-forwarded-proto": "https",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",  # noqa: E501
                "accept": "*/*",
                "cloudfront-is-mobile-viewer": "False",
                "cloudfront-is-smarttv-viewer": "False",
                "accept-encoding": "gzip, deflate, br",
                "referer": "https://us-west-1.console.aws.amazon.com/appsync/home?region=us-west-1",  # noqa: E501
                "content-type": "application/json",
                "sec-fetch-mode": "cors",
                "x-amz-cf-id": "3aykhqlUwQeANU-HGY7E_guV5EkNeMMtwyOgiA==",
                "x-amzn-trace-id": "Root=1-5f512f51-fac632066c5e848ae714",
                "authorization": "eyJraWQiOiJScWFCSlJqYVJlM0hrSnBTUFpIcVRXazNOW...",  # noqa: E501
                "sec-fetch-dest": "empty",
                "x-amz-user-agent": "AWS-Console-AppSync/",
                "cloudfront-is-desktop-viewer": "True",
                "sec-fetch-site": "cross-site",
                "x-forwarded-port": "443",
            }
        },
        "prev": None,
        "info": {
            "selectionSetList": ["id", "field1", "field2"],
            "selectionSetGraphQL": "{\n  id\n  field1\n  field2\n}",
            "parentTypeName": "Mutation",
            "fieldName": "createSomething",
            "variables": {},
        },
        "stash": {},
    }
