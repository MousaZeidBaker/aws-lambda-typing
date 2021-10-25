from aws_lambda_typing.events import MQEvent


def test_mq_event() -> None:
    event: MQEvent = {
        "eventSource": "aws:amq",
        "eventSourceArn": "arn:aws:mq:us-west-2:112556298976:broker:test:b-9bcfa592-423a-4942-879d-eb284b418fc8",  # noqa: E501
        "messages": {
            [
                {
                    "messageID": "ID:b-9bcfa592-423a-4942-879d-eb284b418fc8-1.mq.us-west-2.amazonaws.com-37557-1234520418293-4:1:1:1:1",  # noqa: E501
                    "messageType": "jms/text-message",
                    "data": "QUJDOkFBQUE=",
                    "connectionId": "myJMSCoID",
                    "redelivered": False,
                    "destination": {"physicalname": "testQueue"},
                    "timestamp": 1598827811958,
                    "brokerInTime": 1598827811958,
                    "brokerOutTime": 1598827811959,
                },
                {
                    "messageID": "ID:b-9bcfa592-423a-4942-879d-eb284b418fc8-1.mq.us-west-2.amazonaws.com-37557-1234520418293-4:1:1:1:1",  # noqa: E501
                    "messageType": "jms/bytes-message",
                    "data": "3DTOOW7crj51prgVLQaGQ82S48k=",
                    "connectionId": "myJMSCoID1",
                    "persistent": False,
                    "destination": {"physicalname": "testQueue"},
                    "timestamp": 1598827811958,
                    "brokerInTime": 1598827811958,
                    "brokerOutTime": 1598827811959,
                },
            ]
        },
    }
