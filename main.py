import csv
import json
import os
import boto3

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

app = typer.Typer(
    help="Cloud Infrastructure Auditor - Audit cloud resources safely."
)
VERSION = "1.0.0"
def get_aws_profile():
    """Return the configured AWS profile name, if available."""
    session = boto3.Session()
    return session.profile_name or "default"
@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: bool = typer.Option(
        False,
        "--version",
        help="Show the application version."
    )
):
    if version:
        typer.echo(f"Cloud Infrastructure Auditor v{VERSION}")
        raise typer.Exit()

    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())

console = Console()


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
    console.print("\n[bold cyan]Dry-Run Cleanup Plan[/bold cyan]")

    for resource in resources:
        console.print(
            f"[yellow][DRY-RUN][/yellow] Would review "
            f"{resource['type']} {resource['id']} "
            f"({resource['status']})"
        )

    console.print("\n[bold green]✓ No resources were deleted.[/bold green]")


@app.command()
def audit():
    """Scan AWS resources and identify potential cost savings."""
    console.print(
        Panel.fit(
            "[bold cyan]Cloud Infrastructure Auditor[/bold cyan]\n"
            "Cloud cost optimization and resource audit",
            border_style="cyan",
        )
    )

    resources = get_mock_resources()
    total_savings = 0.0

    table = Table(title="Potential Cost Optimization Findings")

    table.add_column("Resource", style="cyan")
    table.add_column("Resource ID", style="magenta")
    table.add_column("Status", style="yellow")
    table.add_column("Monthly Cost", justify="right", style="green")

    for resource in resources:
        table.add_row(
            resource["type"],
            resource["id"],
            resource["status"],
            f"${resource['estimated_monthly_cost']:.2f}/month",
        )

        total_savings += resource["estimated_monthly_cost"]

    console.print(table)

    console.print(
        Panel(
            f"[bold green]Estimated Monthly Savings: "
            f"${total_savings:.2f}[/bold green]",
            border_style="green",
        )
    )

    save_json_report(resources, total_savings)
    save_csv_report(resources)

    console.print("\n[green]✓ JSON report saved:[/green] audit_report.json")
    console.print("[green]✓ CSV report saved:[/green] audit_report.csv")

    show_dry_run(resources)


if __name__ == "__main__":
    app()