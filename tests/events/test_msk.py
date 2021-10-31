from aws_lambda_typing.events import MSKEvent


def test_msk_event() -> None:
    event: MSKEvent = {
        "eventSource": "aws:kafka",
        "eventSourceArn": "arn:aws:kafka:sa-east-1:123456789012:cluster/vpc-2priv-2pub/751d2973-a626-431c-9d4e-d7975eb44dd7-2",  # noqa: E501
        "records": {
            "mytopic-0": [
                {
                    "topic": "mytopic",
                    "partition": "0",
                    "offset": 15,
                    "timestamp": 1545084650987,
                    "timestampType": "CREATE_TIME",
                    "value": "SGVsbG8sIHRoaXMgaXMgYSB0ZXN0Lg==",
                    "headers": [
                        {
                            "headerKey": [
                                104,
                                101,
                                97,
                                100,
                                101,
                                114,
                                86,
                                97,
                                108,
                                117,
                                101,
                            ]
                        }
                    ],
                }
            ]
        },
    }
