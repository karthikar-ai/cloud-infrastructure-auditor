from main import get_mock_resources


def test_mock_resources():
    resources = get_mock_resources()

    assert len(resources) == 3
    assert resources[0]["type"] == "EBS Volume"
    assert resources[1]["type"] == "Elastic IP"
    assert resources[2]["type"] == "EC2 Instance"


def test_monthly_costs():
    resources = get_mock_resources()

    total = sum(resource["estimated_monthly_cost"] for resource in resources)

    assert total == 36.65