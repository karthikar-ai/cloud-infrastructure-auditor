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


@app.command()
def audit():
    """Scan AWS resources and identify potential cost savings."""
    typer.echo("Cloud Infrastructure Auditor")
    typer.echo("=" * 40)

    resources = get_mock_resources()

    typer.echo("\nPotential Cost Optimization Findings:\n")

    total_savings = 0.0

    for resource in resources:
        typer.echo(
            f"{resource['type']} | "
            f"{resource['id']} | "
            f"{resource['status']} | "
            f"${resource['estimated_monthly_cost']:.2f}/month"
        )
        total_savings += resource["estimated_monthly_cost"]

    typer.echo(f"\nEstimated Monthly Savings: ${total_savings:.2f}")


if __name__ == "__main__":
    app()