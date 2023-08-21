from aws_lambda_typing.common import PolicyDocument


def iam_policy_document() -> None:
    document: PolicyDocument = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Deny",
                "Action": "*",
                "Resource": "*",
            },
            {
                "Effect": "Allow",
                "Action": ["s3:ListAllMyBuckets", "s3:GetBucketLocation"],
                "Resource": "arn:aws:s3:::*",
            },
            {
                "Effect": "Allow",
                "Action": "s3:ListBucket",
                "Resource": "arn:aws:s3:::BUCKET-NAME",
                "Condition": {
                    "StringLike": {
                        "s3:prefix": ["", "home/", "home/${aws:username}/"]
                    }
                },
            },
            {
                "Effect": "Allow",
                "Action": "s3:*",
                "Resource": [
                    "arn:aws:s3:::BUCKET-NAME/home/${aws:username}",
                    "arn:aws:s3:::BUCKET-NAME/home/${aws:username}/*",
                ],
            },
        ],
    }
