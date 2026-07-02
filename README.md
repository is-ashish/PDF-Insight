# 📄 PDF-Insight

Chat with your PDF documents. PDF-Insight is a Retrieval-Augmented Generation (RAG) app that ingests PDFs into a vector store and lets you ask natural-language questions about them through a simple chat UI.

## How it works

```
PDFs (datasource/)
        │  ingest.py
        ▼
  Load → Split → Embed → Store
        │
        ▼
   Chroma vector store
        │
        ▼
 FastAPI backend (server.py)  ── /chat ──►  Groq LLM (Llama 3.3 70B)
        ▲
        │  HTTP request
Streamlit UI (streamlit_app.py)
```

1. **Ingestion** (`ingest.py`) — loads every PDF in the `datasource/` folder, splits it into chunks, embeds the chunks, and persists them to a local Chroma vector store.
2. **Retrieval + generation** (`server.py`) — a FastAPI service exposes a `/chat` endpoint. On each query it does a similarity search against the vector store, filters results by a score threshold, and passes the matched context to a Groq-hosted LLM to generate an answer.
3. **UI** (`streamlit_app.py`) — a lightweight Streamlit chat interface that calls the FastAPI `/chat` endpoint and keeps conversation history in the session.

The app is also wired up to **LangSmith** for tracing/observability of embedding, retrieval, and chain runs.

## Features

- 📥 Bulk PDF ingestion from a single folder
- ✂️ Configurable chunking (`chunk_size` / `chunk_overlap`)
- 🔍 Similarity search with a relevance-score cutoff (falls back to "I don't know" when nothing relevant is found)
- ⚡ Fast inference via [Groq](https://groq.com/) (`llama-3.3-70b-versatile`)
- 🧠 Local embeddings via `sentence-transformers/all-MiniLM-L6-v2`
- 🩻 Built-in tracing to LangSmith for embeddings, retrieval, and chain runs
- 💬 Streamlit chat UI with persistent session history
- 🖥️ REST API (FastAPI) that can be used independently of the UI

## Project structure

```
.
├── app/
│   ├── loaders.py      # PDF loading (PyPDFLoader)
│   ├── splitters.py    # Text chunking
│   ├── embeddings.py   # HuggingFace embeddings + Chroma vectorstore builder
│   ├── llm_chain.py    # Retrieval + Groq LLM chain
│   └── chat.py         # CLI chat loop helper
├── evals/
│   └── evaluation.ipynb  # Evaluation notebook (RAG metrics)
├── config.py            # Env vars, paths (VECTORSTORE_PATH, PDF_PATH, etc.)
├── ingest.py             # Entry point: build the vector store from datasource/
├── server.py              # FastAPI app exposing POST /chat
├── streamlit_app.py        # Streamlit chat UI (calls the FastAPI backend)
├── requirement.txt          # pip dependencies
├── pyproject.toml            # Project metadata / uv dependencies
└── deployment-steps.md        # Notes on deploying this app to Azure
```

## Prerequisites

- Python 3.12
- A [Groq API key](https://console.groq.com/)
- (Optional) A [LangSmith](https://smith.langchain.com/) API key for tracing

## Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/is-ashish/PDF-Insight.git
   cd PDF-Insight
   ```

2. **Install dependencies**

   Using `pip`:
   ```bash
   pip install -r requirement.txt
   ```
   or using [`uv`](https://docs.astral.sh/uv/) (a `uv.lock` is included):
   ```bash
   uv sync
   ```

   > **Note:** the code uses `langchain_chroma` (Chroma) as the vector store, but `chromadb`/`langchain-chroma` isn't currently pinned in `requirement.txt` or `pyproject.toml` — install it separately if you hit an import error:
   > ```bash
   > pip install langchain-chroma chromadb
   > ```

3. **Configure environment variables**

   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key

   # Optional — for LangSmith tracing
   LANGSMITH_API_KEY=your_langsmith_api_key
   LANGSMITH_ENDPOINT=https://api.smith.langchain.com
   LANGSMITH_PROJECT=pdf-insight
   ```

4. **Add your PDFs**

   Create a `datasource/` folder in the project root and drop your PDF files inside:
   ```bash
   mkdir datasource
   # copy your .pdf files into datasource/
   ```

## Usage

1. **Ingest your documents** (run this whenever your PDFs change):
   ```bash
   python ingest.py
   ```
   This builds/overwrites the Chroma vector store under `vectorstore/`.

2. **Start the API backend:**
   ```bash
   uvicorn server:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`, with a chat endpoint at `POST /chat`:
   ```bash
   curl -X POST http://127.0.0.1:8000/chat \
     -H "Content-Type: application/json" \
     -d '{"question": "What is this document about?"}'
   ```

3. **Launch the chat UI** (in a separate terminal, with the backend already running):
   ```bash
   streamlit run streamlit_app.py
   ```
   Open the URL Streamlit prints (typically `http://localhost:8501`) and start chatting with your documents.

## Evaluation

`evals/evaluation.ipynb` contains a notebook for evaluating RAG quality (e.g. faithfulness, answer relevancy, context precision/recall).

## Deployment

See [`deployment-steps.md`](./deployment-steps.md) for a walkthrough of deploying this app to Azure (Docker, Azure App Service/AKS, Blob Storage for the vector store, Key Vault for secrets, and a re-ingestion pipeline via Azure Functions).

## Roadmap / known gaps

- [ ] Pin `langchain-chroma` / `chromadb` in dependency files (currently required by code but not listed)
- [ ] Reconcile `requirement.txt` vs `pyproject.toml` (they currently list different dependency sets)
- [ ] Add automated tests (`test.py` is currently a placeholder)

## License

No license file is currently included in this repository.