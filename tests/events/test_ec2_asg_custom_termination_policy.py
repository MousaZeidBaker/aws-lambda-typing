from aws_lambda_typing.events import EC2ASGCustomTerminationPolicyEvent


def test_ec2_asg_custom_termination_policy_event_pattern1() -> None:
    # Event from AWS documentation
    # https://docs.aws.amazon.com/autoscaling/ec2/userguide/lambda-custom-termination-policy.html
    event: EC2ASGCustomTerminationPolicyEvent = {
        "AutoScalingGroupARN": "arn:aws:autoscaling:us-east-1:<account-id>:autoScalingGroup:d4738357-2d40-4038-ae7e-b00ae0227003:autoScalingGroupName/my-asg",  # noqa: E501
        "AutoScalingGroupName": "my-asg",
        "CapacityToTerminate": [
            {
                "AvailabilityZone": "us-east-1b",
                "Capacity": 2,
                "InstanceMarketOption": "on-demand",
            },
            {
                "AvailabilityZone": "us-east-1b",
                "Capacity": 1,
                "InstanceMarketOption": "spot",
            },
            {
                "AvailabilityZone": "us-east-1c",
                "Capacity": 3,
                "InstanceMarketOption": "on-demand",
            },
        ],
        "Instances": [
            {
                "AvailabilityZone": "us-east-1b",
                "InstanceId": "i-0056faf8da3e1f75d",
                "InstanceType": "t2.nano",
                "InstanceMarketOption": "on-demand",
            },
            {
                "AvailabilityZone": "us-east-1c",
                "InstanceId": "i-02e1c69383a3ed501",
                "InstanceType": "t2.nano",
                "InstanceMarketOption": "on-demand",
            },
            {
                "AvailabilityZone": "us-east-1c",
                "InstanceId": "i-036bc44b6092c01c7",
                "InstanceType": "t2.nano",
                "InstanceMarketOption": "on-demand",
            },
        ],
        "Cause": "SCALE_IN",
    }


def test_ec2_asg_custom_termination_policy_event_pattern2() -> None:
    # Real event observed on 2023/08/17
    event: EC2ASGCustomTerminationPolicyEvent = {
        "AutoScalingGroupARN": "arn:aws:autoscaling:ap-northeast-1:480046787332:autoScalingGroup:77727a8f-46ed-4afd-beb6-043e14f8fb40:autoScalingGroupName/test",  # noqa: E501
        "AutoScalingGroupName": "test",
        "CapacityToTerminate": [
            {
                "AvailabilityZone": "ap-northeast-1a",
                "Capacity": 1,
                "InstanceMarketOption": "on-demand",
            },
            {
                "AvailabilityZone": "ap-northeast-1c",
                "Capacity": 1,
                "InstanceMarketOption": "on-demand",
            },
        ],
        "Instances": [
            {
                "AvailabilityZone": "ap-northeast-1c",
                "InstanceId": "i-06f811125f96a0d92",
                "InstanceType": "t4g.small",
                "InstanceMarketOption": "on-demand",
            },
            {
                "AvailabilityZone": "ap-northeast-1a",
                "InstanceId": "i-0cb2107f121e6b3ed",
                "InstanceType": "t4g.small",
                "InstanceMarketOption": "on-demand",
            },
        ],
        "Cause": "SCALE_IN",
    }
