import boto3
from moto import mock_aws


@mock_aws
def test_aws_connection():
    ec2 = boto3.client("ec2", region_name="us-east-1")

    response = ec2.describe_regions()

    assert "Regions" in response


@mock_aws
def test_create_and_list_ec2_instances():
    ec2 = boto3.resource("ec2", region_name="us-east-1")

    instances = ec2.create_instances(
        ImageId="ami-12345678",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
    )

    assert len(instances) == 1
    assert instances[0].instance_type == "t2.micro"