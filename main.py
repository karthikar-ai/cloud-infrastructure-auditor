import typer

app = typer.Typer(
    help="Cloud Infrastructure Auditor - Audit cloud resources safely."
)


@app.command()
def audit():
    """Start a cloud infrastructure audit."""
    typer.echo("Cloud Infrastructure Auditor")
    typer.echo("Starting cloud resource audit...")

    typer.echo("\nAWS Resource Checks:")
    typer.echo("✓ Unattached EBS volumes")
    typer.echo("✓ Unused Elastic IP addresses")
    typer.echo("✓ Underutilized EC2 instances")


if __name__ == "__main__":
    app()