import aws_lambda_typing as lambda_typing


def test_cloud_watch_logs_event() -> None:
    dummy: lambda_typing.CloudWatchLogsEvent = {
        "awslogs": {
            "data": "ewogICAgIm1lc3NhZ2VUeXBlIjogIkRBVEFfTUVTU0FHRSIsCiAgICAib3duZXIiOiAiMTIzNDU2Nzg5MDEyIiwKICAgICJsb2dHcm91cCI6I..."
        }
    }
