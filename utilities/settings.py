from dotenv import load_dotenv
import os


"""
Utility functions to handle environment variables.
"""
def load_env(env_file):
    load_dotenv(env_file)
    required_vars = ["SPOTIFY_CLIENT_ID", "SPOTIFY_CLIENT_SECRET", "OPENAI_API_KEY"]
    missing_vars = [var for var in required_vars if var not in os.environ]
    if missing_vars:
        raise ValueError(f"Error: missing environment variables: {', '.join(missing_vars)}")