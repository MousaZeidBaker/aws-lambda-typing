from aws_lambda_typing.events import ApacheKafkaEvent


def test_apache_kafka_event() -> None:
    event: ApacheKafkaEvent = {
        "eventSource": "SelfManagedKafka",
        "bootstrapServers": "myserver.local:9092",
        "records": {
            "mytopic-0": [
                {
                    "topic": "mytopic",
                    "partition": 0,
                    "offset": 15,
                    "timestamp": 1545084650987,
                    "timestampType": "CREATE_TIME",
                    "key": "a2V5X3Rlc3Q=",
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
