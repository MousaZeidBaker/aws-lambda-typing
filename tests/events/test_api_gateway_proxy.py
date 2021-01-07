import aws_lambda_typing as lambda_typing


def test_api_gateway_proxy_event_v1() -> None:
    dummy: lambda_typing.APIGatewayProxyEventV1 = {
        "resource": "/",
        "path": "/",
        "httpMethod": "GET",
        "headers": {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "cookie": "s_fid=7AAB6XMPLAFD9BBF-0643XMPL09956DE2; regStatus=pre-register",
            "Host": "70ixmpl4fl.execute-api.us-east-2.amazonaws.com",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "upgrade-insecure-requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
            "X-Amzn-Trace-Id": "Root=1-5e66d96f-7491f09xmpl79d18acf3d050",
            "X-Forwarded-For": "52.255.255.12",
            "X-Forwarded-Port": "443",
            "X-Forwarded-Proto": "https"
        },
        "multiValueHeaders": {
            "accept": [
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
            ],
            "accept-encoding": [
                "gzip, deflate, br"
            ],
            "accept-language": [
                "en-US,en;q=0.9"
            ],
            "cookie": [
                "s_fid=7AABXMPL1AFD9BBF-0643XMPL09956DE2; regStatus=pre-register;"
            ],
            "Host": [
                "70ixmpl4fl.execute-api.ca-central-1.amazonaws.com"
            ],
            "sec-fetch-dest": [
                "document"
            ],
            "sec-fetch-mode": [
                "navigate"
            ],
            "sec-fetch-site": [
                "none"
            ],
            "upgrade-insecure-requests": [
                "1"
            ],
            "User-Agent": [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
            ],
            "X-Amzn-Trace-Id": [
                "Root=1-5e66d96f-7491f09xmpl79d18acf3d050"
            ],
            "X-Forwarded-For": [
                "52.255.255.12"
            ],
            "X-Forwarded-Port": [
                "443"
            ],
            "X-Forwarded-Proto": [
                "https"
            ]
        },
        "queryStringParameters": {},
        "multiValueQueryStringParameters": {},
        "pathParameters": {},
        "stageVariables": {},
        "requestContext": {
            "resourceId": "2gxmpl",
            "resourcePath": "/",
            "httpMethod": "GET",
            "extendedRequestId": "JJbxmplHYosFVYQ=",
            "requestTime": "10/Mar/2020:00:03:59 +0000",
            "path": "/Prod/",
            "accountId": "123456789012",
            "protocol": "HTTP/1.1",
            "stage": "Prod",
            "domainPrefix": "70ixmpl4fl",
            "requestTimeEpoch": 1583798639428,
            "requestId": "77375676-xmpl-4b79-853a-f982474efe18",
            "identity": {
                "cognitoIdentityPoolId": None,
                "accountId": None,
                "cognitoIdentityId": None,
                "caller": None,
                "sourceIp": "52.255.255.12",
                "principalOrgId": None,
                "accessKey": None,
                "cognitoAuthenticationType": None,
                "cognitoAuthenticationProvider": None,
                "userArn": None,
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
                "user": None
            },
            "domainName": "70ixmpl4fl.execute-api.us-east-2.amazonaws.com",
            "apiId": "70ixmpl4fl"
        },
        "body": "",
        "isBase64Encoded": False
    }


def test_api_gateway_proxy_event_v2() -> None:
    dummy: lambda_typing.APIGatewayProxyEventV2 = {
        "version": "2.0",
        "routeKey": "ANY /nodejs-apig-function-1G3XMPLZXVXYI",
        "rawPath": "/default/nodejs-apig-function-1G3XMPLZXVXYI",
        "rawQueryString": "",
        "cookies": [
            "s_fid=7AABXMPL1AFD9BBF-0643XMPL09956DE2",
            "regStatus=pre-register"
        ],
        "headers": {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "content-length": "0",
            "host": "r3pmxmplak.execute-api.us-east-2.amazonaws.com",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "cross-site",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
            "x-amzn-trace-id": "Root=1-5e6722a7-cc56xmpl46db7ae02d4da47e",
            "x-forwarded-for": "205.255.255.176",
            "x-forwarded-port": "443",
            "x-forwarded-proto": "https"
        },
        "requestContext": {
            "accountId": "123456789012",
            "apiId": "r3pmxmplak",
            "domainName": "r3pmxmplak.execute-api.us-east-2.amazonaws.com",
            "domainPrefix": "r3pmxmplak",
            "http": {
                "method": "GET",
                "path": "/default/nodejs-apig-function-1G3XMPLZXVXYI",
                "protocol": "HTTP/1.1",
                "sourceIp": "205.255.255.176",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
            },
            "requestId": "JKJaXmPLvHcESHA=",
            "routeKey": "ANY /nodejs-apig-function-1G3XMPLZXVXYI",
            "stage": "default",
            "time": "10/Mar/2020:05:16:23 +0000",
            "timeEpoch": 1583817383220
        },
        "isBase64Encoded": True
    }
