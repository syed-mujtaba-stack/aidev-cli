"""Main entry point for AI-Dev-CLI."""

import typer
from rich.console import Console
from .cli import commands

# Initialize the main app
app = commands.app

if __name__ == "__main__":
    app()
