"""Configuration settings for AI-Dev-CLI."""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Application settings
APP_NAME = "AI-Dev-CLI"
VERSION = "0.1.0"

# API Settings
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
DEFAULT_MODEL = "mixtral-8x7b-32768"

# Project defaults
DEFAULT_OUTPUT_DIR = "./projects"
TEMPLATES_DIR = Path(__file__).parent.parent / "templates"

# Ensure templates directory exists
TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)
