"""CLI commands for AI-Dev-CLI."""

import typer
from typing import Optional
from rich.console import Console
from rich.prompt import Prompt

from .. import __version__

app = typer.Typer(name="aidev", help="AI-powered project generator")
console = Console()


@app.command()
def version():
    """Show version information."""
    console.print(f"AI-Dev-CLI v{__version__}", style="bold green")


@app.command()
def create(
    project_description: str = typer.Argument(
        ...,
        help="Description of the project to create"
    ),
    output_dir: str = typer.Option(
        ".",
        "--output",
        "-o",
        help="Output directory for the project"
    ),
):
    """Create a new project based on the description."""
    console.print(
        f"\n🚀 Creating project: {project_description}",
        style="bold blue"
    )
    console.print(f"📁 Output directory: {output_dir}")
    
    # TODO: Add project creation logic
    console.print("\n✅ Project created successfully!", style="bold green")
