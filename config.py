import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# Base directory = project root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

VECTORSTORE_PATH = os.path.join(BASE_DIR, "vectorstore")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_ENDPOINT = os.getenv("LANGSMITH_ENDPOINT")
LANGSMITH_PROJECT= os.getenv("LANGSMITH_PROJECT")


# Point to the folder instead of a single file
PDF_PATH = os.path.join(BASE_DIR, "datasource")


# print(type(PDF_PATH), "TYPE OF FILE")



