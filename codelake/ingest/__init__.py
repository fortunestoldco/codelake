"""
Documentation ingestion module for codelake.
"""

from codelake.ingest.documentation_ingest import ingest_sdk_documentation
from codelake.ingest.updater import DocumentationUpdater, get_updater

# Export the alias at module level
__all__ = ['ingest_sdk_documentation', 'DocumentationUpdater', 'get_updater']