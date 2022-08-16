from aws_lambda_typing.events import WebSocketRouteEvent, WebSocketConnectEvent


def test_websocket_route_event() -> None:
    event: WebSocketRouteEvent = {
        "requestContext": {
            "routeKey": "route",
            "authorizer": {
                "authId": "ce2f5357-aa43-4b55-a835-b69f980d0ebf",
                "principalId": "28aeed70-50ce-4ce9-85b8-40293dfd9b64",
            },
            "messageId": "W9I-IeqhoAMCFvw=",
            "eventType": "MESSAGE",
            "extendedRequestId": "W9I-IGdiIAMFTIA=",
            "requestTime": "16/Aug/2022:12:06:50 +0000",
            "messageDirection": "IN",
            "stage": "dev",
            "connectedAt": 1660651467489,
            "requestTimeEpoch": 1660651610256,
            "identity": {"sourceIp": "62.90.14.41"},
            "requestId": "W9I-IGdiIAMFTIA=",
            "domainName": "ws.rocket.jitdev.io",
            "connectionId": "W9In0cvXIAMCFvw=",
            "apiId": "yldxgyfndc",
        },
        "body": '{"action": "route"}',
        "isBase64Encoded": False,
    }


def test_websocket_connect_event() -> None:
    event: WebSocketConnectEvent = {
        "headers": {
            "Host": "ws.domain.io",
            "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
            "Sec-WebSocket-Key": "NysmUTUM1SWo5oeJuKHZhw==",
            "Sec-WebSocket-Version": "13",
            "X-Amzn-Trace-Id": "Root=1-62fb87cb-4dbfce250f33864344a762b9",
            "X-Forwarded-For": "62.90.14.41",
            "X-Forwarded-Port": "443",
            "X-Forwarded-Proto": "https",
        },
        "multiValueHeaders": {
            "Host": ["ws.rocket.jitdev.io"],
            "Sec-WebSocket-Extensions": [
                "permessage-deflate; client_max_window_bits"
            ],
            "Sec-WebSocket-Key": ["NysmUTUM1SWo5oeJuKHZhw=="],
            "Sec-WebSocket-Version": ["13"],
            "X-Amzn-Trace-Id": ["Root=1-62fb87cb-4dbfce250f33864344a762b9"],
            "X-Forwarded-For": ["62.90.14.41"],
            "X-Forwarded-Port": ["443"],
            "X-Forwarded-Proto": ["https"],
        },
        "queryStringParameters": {
            "Authorization": "eyJhbGciOiJSUzI1NiIsInR5cCI6I",
            "AuthId": "ce2f5357-aa43-4b55-a835-b69f980d0ebf",
        },
        "multiValueQueryStringParameters": {
            "Authorization": ["eyJhbGciOiJSUzI1NiIsInR5cCI6I."],
            "AuthId": ["ce2f5357-aa43-4b55-a835-b69f980d0ebf"],
        },
        "requestContext": {
            "routeKey": "$connect",
            "authorizer": {
                "tenant_id": "ce2f5357-aa43-4b55-a835-b69f980d0ebf",
                "principalId": "28aeed70-50ce-4ce9-85b8-40293dfd9b64",
                "integrationLatency": 21,
            },
            "eventType": "CONNECT",
            "extendedRequestId": "W9In0EDVIAMFexQ=",
            "requestTime": "16/Aug/2022:12:04:27 +0000",
            "messageDirection": "IN",
            "stage": "dev",
            "connectedAt": 1660651467489,
            "requestTimeEpoch": 1660651467493,
            "identity": {"sourceIp": "62.90.14.41"},
            "requestId": "W9In0EDVIAMFexQ=",
            "domainName": "ws.domain.io",
            "connectionId": "W9In0cvXIAMCFvw=",
            "apiId": "yldxgyfndc",
        },
        "isBase64Encoded": False,
    }
