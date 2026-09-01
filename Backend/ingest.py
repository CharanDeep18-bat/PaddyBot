from pathlib import Path

from embeddings import get_embedding_model
from vectordb import create_vector_database
from config import PDF_FOLDER
from loaders import load_documents
from splitter import split_documents


# Count PDF files
pdf_files = list(Path(PDF_FOLDER).rglob("*.pdf"))

# Load all documents
documents = load_documents()

# Split documents into chunks
chunks = split_documents(documents)

# Load embedding model
embedding_model = get_embedding_model("sentence-transformers/all-MiniLM-L6-v2")

# Create Chroma vector database
vectordb = create_vector_database(chunks, embedding_model)

# Display results
print(f"\nTotal PDF files: {len(pdf_files)}")
print(f"Total pages loaded: {len(documents)}")
print(f"Total chunks created: {len(chunks)}")

print("\nFirst Chunk")
print("-" * 50)
print(chunks[0].page_content)

print("\nChunk Metadata")
print("-" * 50)
print(chunks[0].metadata)