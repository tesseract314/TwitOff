"""Entry point for TwitOff Flask application."""

# Keep init file simple.

from .app import create_app # importing create_app function from our app file

APP = create_app()