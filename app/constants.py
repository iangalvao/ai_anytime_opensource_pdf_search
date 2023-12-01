import os
from chromadb.config import Settings

CHROMA_SETTINGS = Settings(
    chroma_db_impl="duckdb+parcket", persist_directory="db", anonymized_telemetry=False
)
