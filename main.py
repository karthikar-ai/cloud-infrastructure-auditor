import csv
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


def save_csv_report(resources):
    """Save audit results as a CSV report."""
    with open("audit_report.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "type",
                "id",
                "status",
                "estimated_monthly_cost",
            ],
        )

        writer.writeheader()
        writer.writerows(resources)


def show_dry_run(resources):
    """Show proposed cleanup actions without deleting anything."""
    typer.echo("\nDry-Run Cleanup Plan:")
    typer.echo("-" * 40)

    for resource in resources:
        typer.echo(
            f"[DRY-RUN] Would review {resource['type']} "
            f"{resource['id']} ({resource['status']})"
        )

    typer.echo("\nNo resources were deleted.")


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
    save_csv_report(resources)

    typer.echo("\nJSON report saved: audit_report.json")
    typer.echo("CSV report saved: audit_report.csv")

    show_dry_run(resources)


if __name__ == "__main__":
    app()