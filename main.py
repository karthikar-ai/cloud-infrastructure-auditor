import typer

app = typer.Typer(
    help="Cloud Infrastructure Auditor - Audit cloud resources safely."
)


@app.command()
def audit():
    """Start a cloud infrastructure audit."""
    typer.echo("Cloud Infrastructure Auditor")
    typer.echo("Starting cloud resource audit...")


if __name__ == "__main__":
    app()