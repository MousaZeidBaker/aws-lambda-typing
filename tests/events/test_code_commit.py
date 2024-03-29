from aws_lambda_typing.events import CodeCommitMessageEvent


def test_code_commit_event() -> None:
    event: CodeCommitMessageEvent = {
        "Records": [
            {
                "awsRegion": "us-east-2",
                "codecommit": {
                    "references": [
                        {
                            "commit": "5e493c6f3067653f3d04eca608b4901eb227078",
                            "ref": "refs/heads/master",
                        }
                    ]
                },
                "eventId": "31ade2c7-f889-47c5-a937-1cf99e2790e9",
                "eventName": "ReferenceChanges",
                "eventPartNumber": 1,
                "eventSource": "aws:codecommit",
                "eventSourceARN": "arn:aws:codecommit:us-east-2:123456789012:lambda-pipeline-repo",  # noqa: E501
                "eventTime": "2019-03-12T20:58:25.400+0000",
                "eventTotalParts": 1,
                "eventTriggerConfigId": "0d17d6a4-efeb-46f3-b3ab-a63741badeb8",
                "eventTriggerName": "index.handler",
                "eventVersion": "1.0",
                "userIdentityARN": "arn:aws:iam::123456789012:user/intern",
            }
        ]
    }
