from config import PDF_PATH, VECTORSTORE_PATH
from app.loaders import load_pdf
from app.splitters import split_documents
from app.embeddings import build_vectorstore
from pathlib import Path
import os


if __name__ == "__main__":
    # Always ingest and overwrite vectorstore if documents change
    print("📄 Starting ingestion pipeline...")

    # Step 1: Load All pdf from the datasource folder
    
    documents = []
    PDF_PATH = Path(PDF_PATH)
    
    print("no of contents -:", len(os.listdir(PDF_PATH)))
    
    if len(os.listdir(PDF_PATH)) == 0:
        raise FileExistsError("Please Add Pdf files ....")
        
    for file in os.listdir(PDF_PATH):
        if file.endswith(".pdf"):
            file_name = PDF_PATH/file
            docs = load_pdf(file_name)
            documents.extend(docs)
            
    # Step 2: Split into chunks
    chunks = split_documents(documents)

    # Step 3: Build and persist vectorstore
    print("⚙️ Building vectorstore for the first time...")
    vectorstore = build_vectorstore(chunks)

    # Step 4: Save vectorstore to disk
    if hasattr(vectorstore, "persist"):
        vectorstore.persist()
        print(f"✅ Embeddings stored in DB at  {VECTORSTORE_PATH}")
    else:
        print(f"⚠️ Warning: vectorstore persistence not implemented in build_vectorstore")