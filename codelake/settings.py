import os
from typing import List
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # API Keys
    openai_api_key: str = os.environ.get("OPENAI_API_KEY", "")
    activeloop_token: str = os.environ.get("ACTIVELOOP_TOKEN", "")

    # API Configuration  
    api_host: str = os.environ.get("API_HOST", "0.0.0.0")
    api_port: int = int(os.environ.get("API_PORT", "8000"))

    # Deep Lake Configuration
    deeplake_dataset_path: str = os.environ.get("DEEPLAKE_DATASET_PATH", "")
    repo_url: str = os.environ.get("REPO_URL", "")

    # Web Search Configuration
    google_api_key: str = os.environ.get("GOOGLE_API_KEY", "")
    google_cse_id: str = os.environ.get("GOOGLE_CSE_ID", "")
    use_web_search: bool = os.environ.get("USE_WEB_SEARCH", "true").lower() == "true"

    # Search Configuration  
    search_confidence_threshold: float = float(os.environ.get("SEARCH_CONFIDENCE_THRESHOLD", "0.85"))
    distance_metric: str = os.environ.get("DISTANCE_METRIC", "cos")
    fetch_k: int = int(os.environ.get("FETCH_K", "5"))

    # Model Configuration
    model_name: str = os.environ.get("MODEL_NAME", "gpt-4-turbo")
    temperature: float = float(os.environ.get("TEMPERATURE", "0.2"))

    # Update Configuration
    enable_auto_updates: bool = os.environ.get("ENABLE_AUTO_UPDATES", "false").lower() == "true"
    update_schedule: str = os.environ.get("UPDATE_SCHEDULE", "0 2 * * *")

    # Document Processing
    chunk_size: int = int(os.environ.get("CHUNK_SIZE", "1000"))
    chunk_overlap: int = int(os.environ.get("CHUNK_OVERLAP", "100"))

    # Security Configuration
    allowed_sdk_sources: List[str] = os.environ.get("ALLOWED_SDK_SOURCES", 
                                                   "github.com,gitlab.com,bitbucket.org").split(",")

# Create a singleton instance
settings = Settings()

# Also export individual settings for backward compatibility
openai_api_key: str = settings.openai_api_key
activeloop_token: str = settings.activeloop_token
api_host: str = settings.api_host
api_port: int = settings.api_port
deeplake_dataset_path: str = settings.deeplake_dataset_path
repo_url: str = settings.repo_url
google_api_key: str = settings.google_api_key
google_cse_id: str = settings.google_cse_id
use_web_search: bool = settings.use_web_search
search_confidence_threshold: float = settings.search_confidence_threshold
distance_metric: str = settings.distance_metric
fetch_k: int = settings.fetch_k
model_name: str = settings.model_name
temperature: float = settings.temperature
enable_auto_updates: bool = settings.enable_auto_updates
update_schedule: str = settings.update_schedule
chunk_size: int = settings.chunk_size
chunk_overlap: int = settings.chunk_overlap
allowed_sdk_sources: List[str] = settings.allowed_sdk_sources

# Export everything
__all__ = [
    'settings',
    'openai_api_key',
    'activeloop_token',
    'api_host',
    'api_port',
    'deeplake_dataset_path',
    'repo_url',
    'google_api_key',
    'google_cse_id',
    'use_web_search',
    'search_confidence_threshold',
    'distance_metric',
    'fetch_k',
    'model_name',
    'temperature',
    'enable_auto_updates',
    'update_schedule',
    'chunk_size',
    'chunk_overlap',
    'allowed_sdk_sources'
]