from aws_lambda_typing.events import CloudWatchLogsEvent


def test_cloud_watch_logs_event() -> None:
    event: CloudWatchLogsEvent = {
        "awslogs": {
            "data": "ewogICAgIm1lc3NhZ2VUeXBlIjogIkRBVEFfTUVTU0FHRSIsCiAgICAib3duZXIiOiAiMTIzNDU2Nzg5MDEyIiwKICAgICJsb2dHcm91cCI6I..."
        }
    }
