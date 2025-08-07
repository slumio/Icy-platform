import os
from dotenv import load_dotenv
from pydantic import BaseSettings
import logging

# Construct the path to the .env file, which is in the parent 'backend' directory
# This makes the script work correctly regardless of where it's run from.
env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env')
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    Pydantic automatically reads the variables from the .env file and validates them.
    """
    # Database Configuration
    MONGODB_URI: str

    # Service API Keys
    OPENAI_API_KEY: str
    SENDGRID_API_KEY: str
    SENDER_EMAIL: str

    # JWT Authentication
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        # This tells Pydantic where to look for the .env file if the path isn't specified.
        # While we load it manually above for robustness, this is good practice.
        env_file = ".env"
        env_file_encoding = "utf-8"

# Create a single, importable instance of the settings
try:
    settings = Settings()
    logging.info("Configuration loaded successfully.")
except Exception as e:
    logging.error(f"FATAL: Could not load configuration. Missing environment variables? Error: {e}")
    # In a real app, you might exit here if the config fails to load.
    settings = None