import typer

app = typer.Typer(
    help="Cloud Infrastructure Auditor - Audit cloud resources safely."
)


def get_mock_resources():
    """Return sample AWS resources for testing."""
    return [
        {
            "type": "EBS Volume",
            "id": "vol-001",
            "status": "Unattached",
            "estimated_monthly_cost": 8.00,
        },
        {
            "type": "Elastic IP",
            "id": "eip-001",
            "status": "Unused",
            "estimated_monthly_cost": 3.65,
        },
        {
            "type": "EC2 Instance",
            "id": "i-001",
            "status": "Underutilized",
            "estimated_monthly_cost": 25.00,
        },
    ]


import json

import typer

app = typer.Typer(
    help="Cloud Infrastructure Auditor - Audit cloud resources safely."
)


def get_mock_resources():
    """Return sample AWS resources for testing."""
    return [
        {
            "type": "EBS Volume",
            "id": "vol-001",
            "status": "Unattached",
            "estimated_monthly_cost": 8.00,
        },
        {
            "type": "Elastic IP",
            "id": "eip-001",
            "status": "Unused",
            "estimated_monthly_cost": 3.65,
        },
        {
            "type": "EC2 Instance",
            "id": "i-001",
            "status": "Underutilized",
            "estimated_monthly_cost": 25.00,
        },
    ]


def save_json_report(resources, total_savings):
    """Save audit results as a JSON report."""
    report = {
        "resources": resources,
        "estimated_monthly_savings": total_savings,
    }

    with open("audit_report.json", "w") as file:
        json.dump(report, file, indent=4)


@app.command()
def audit():
    """Scan AWS resources and identify potential cost savings."""
    typer.echo("Cloud Infrastructure Auditor")
    typer.echo("=" * 40)

    resources = get_mock_resources()
    total_savings = 0.0

    typer.echo("\nPotential Cost Optimization Findings:\n")

    for resource in resources:
        typer.echo(
            f"{resource['type']} | "
            f"{resource['id']} | "
            f"{resource['status']} | "
            f"${resource['estimated_monthly_cost']:.2f}/month"
        )

        total_savings += resource["estimated_monthly_cost"]

    typer.echo(f"\nEstimated Monthly Savings: ${total_savings:.2f}")

    save_json_report(resources, total_savings)
    typer.echo("\nJSON report saved: audit_report.json")


if __name__ == "__main__":
    app()