from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langsmith import traceable
from config import VECTORSTORE_PATH
from langsmith.run_helpers import get_current_run_tree


@traceable(run_type="embedding", name="Initialize Embeddings")
def _init_embeddings():
    """Initialize HuggingFace embeddings model"""
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

# Define embeddings globally so they can be reused
embeddings = _init_embeddings()

@traceable(
    run_type="embedding",
    name="Build Vector Store",
    metadata={"vector_db": "chroma", "model": "all-MiniLM-L6-v2"}
)
def build_vectorstore(chunks):
    print("⏳ Building vectorstore...")
    
    # Log what’s being embedded
    run_tree = get_current_run_tree()
    if run_tree:
        run_tree.metadata.update({
            "num_chunks": len(chunks),
            "sample_chunk": chunks[0].page_content if chunks else None
        })
    
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTORSTORE_PATH,
    )
    
    print("✅ Vectorstore built!")
    
    return vectorstore