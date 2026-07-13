# server.py
from fastapi import FastAPI
from pydantic import BaseModel
from config import VECTORSTORE_PATH, LANGSMITH_API_KEY, LANGSMITH_ENDPOINT,LANGSMITH_PROJECT

from app.embeddings import embeddings
from app.llm_chain import build_chain
from langchain_chroma import Chroma
from langchain_core.tracers.langchain import LangChainTracer
from langsmith import Client
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Initialize LangSmith client and tracer
langsmith_client = Client(
    api_key=LANGSMITH_API_KEY,
    api_url=LANGSMITH_ENDPOINT,
)

tracer = LangChainTracer(
    client=langsmith_client,
    project_name=LANGSMITH_PROJECT,
)

@app.get("/")
def welcome():
    return {"message": "Welcome to PDF Chat Bot.."}

class Query(BaseModel):
    question: str

if os.path.exists(VECTORSTORE_PATH):
    vectorstore = Chroma(
        persist_directory=VECTORSTORE_PATH,
        embedding_function=embeddings
    )
    chain = build_chain(vectorstore)
else:
    raise FileNotFoundError("Run ingest.py first")

@app.post("/chat")
def chat(query: Query):
    # Pass tracer as a list in callbacks config
    res = chain(query.question)
    #     query.question,
    #     config={
    #         "callbacks": [tracer],
    #         "metadata": {
    #             "user_input": query.question,
    #             "endpoint": "/chat"
    #         },
    #         "tags": ["production", "customer-support"]
    #     }
    # )
    return {
        "answer": res["response"],
        "documents": res["documents"]
        }