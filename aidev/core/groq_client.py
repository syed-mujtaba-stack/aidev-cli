"""Groq API client for AI-Dev-CLI."""

import os
import json
from typing import Dict, Any, Optional
import requests
from rich.console import Console

from ..config.settings import GROQ_API_KEY, DEFAULT_MODEL

console = Console()

class GroqClient:
    """Client for interacting with the Groq API."""
    
    BASE_URL = "https://api.groq.com/openai/v1"
    
    def __init__(self, api_key: str = None, model: str = None):
        """Initialize the Groq client.
        
        Args:
            api_key: Groq API key. If not provided, will use from environment.
            model: Model to use for completions.
        """
        self.api_key = api_key or GROQ_API_KEY
        self.model = model or DEFAULT_MODEL
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def generate_text(
        self,
        prompt: str,
        max_tokens: int = 2000,
        temperature: float = 0.7,
        **kwargs
    ) -> str:
        """Generate text using the Groq API.
        
        Args:
            prompt: The prompt to send to the API.
            max_tokens: Maximum number of tokens to generate.
            temperature: Controls randomness in the response.
            **kwargs: Additional arguments to pass to the API.
            
        Returns:
            The generated text.
        """
        url = f"{self.BASE_URL}/chat/completions"
        
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": temperature,
            "max_tokens": max_tokens,
            **kwargs
        }
        
        try:
            response = requests.post(
                url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
            
        except requests.exceptions.RequestException as e:
            console.print(f"\n❌ Error calling Groq API: {str(e)}", style="bold red")
            if hasattr(e, 'response') and e.response is not None:
                console.print(f"Response: {e.response.text}")
            raise

def get_groq_client() -> GroqClient:
    """Get a configured instance of the Groq client."""
    return GroqClient()
