import json
from pathlib import Path
import time
from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.vectorstores import FAISS

import csv
import sys
from pathlib import Path
from metrics import (
    precision_at_k,
    recall_at_k,
    reciprocal_rank,
)

# Add Backend directory to Python path
BACKEND_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BACKEND_DIR))

from embeddings import get_embedding_model
from loaders import load_documents
from splitter import split_documents
from vectordb import create_vector_database

from chroma_db import create_chroma_database

BASE_DIR = Path(__file__).parent
QUESTIONS_FILE = BASE_DIR / "questions.json"
with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
    questions = json.load(f)


print(f"Loaded {len(questions)} questions.")

MODELS = [
    "sentence-transformers/all-MiniLM-L6-v2",
    "BAAI/bge-base-en-v1.5",
    "intfloat/e5-base-v2",
    "jinaai/jina-embeddings-v2-base-en",
]

DATABASES = {
    "faiss": create_vector_database,
    "chroma": create_chroma_database,
}

print("\nLoading documents...")
documents = load_documents()

print(f"Loaded {len(documents)} pages.")

print("\nSplitting documents...")
chunks = split_documents(documents)

print(f"Created {len(chunks)} chunks.")
for db_name, db_builder in DATABASES.items():

    print("\n" + "=" * 80)
    print(f"DATABASE : {db_name.upper()}")
    print("=" * 80)

    for MODEL_NAME in MODELS:

        print("\n" + "-" * 60)
        print(f"Embedding : {MODEL_NAME}")
        print("-" * 60)

        embeddings = get_embedding_model(MODEL_NAME)

        model_short = MODEL_NAME.split("/")[-1].replace(".", "_")

        print(f"\nBuilding {db_name.upper()} index...")

        if db_name == "chroma":
            vectordb = db_builder(
                chunks,
                embeddings,
                collection_name=model_short
            )
        else:
            vectordb = db_builder(
                chunks,
                embeddings
            )

        print(f"{db_name.upper()} index created successfully!")

        

        OUTPUT_FILE = BASE_DIR / f"{db_name}_{model_short}.csv"

        with open(
            OUTPUT_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as csv_file:

            writer = csv.writer(csv_file)

            writer.writerow([
                "Question ID",
                "Category",
                "Difficulty",
                "Question",
                "Rank",
                "Retrieved PDF"
            ])

            retrieval_times = []

            for q in questions:

                query = q["question"]

                # Measure embedding time
                t1 = time.perf_counter()
                query_embedding = embeddings.embed_query(query)
                t2 = time.perf_counter()

                start = time.perf_counter()
                # Measure only vector search
                docs = vectordb.similarity_search_by_vector(
                    query_embedding,
                    k=10
                )
                end = time.perf_counter()
                t3 = time.perf_counter()

                embedding_time = (t2 - t1) * 1000
                search_time = (t3 - t2) * 1000

                print(
                    f"Embedding: {embedding_time:.2f} ms | "
                    f"Search: {search_time:.2f} ms"
                )

                retrieval_times.append((end - start) * 1000)

                unique_docs = []
                seen = set()

                for doc in docs:

                    source = Path(doc.metadata["source"]).name

                    if source not in seen:
                        seen.add(source)
                        unique_docs.append(source)

                    if len(unique_docs) == 5:
                        break

                for rank, pdf in enumerate(unique_docs, start=1):

                    writer.writerow([
                        q["id"],
                        q["category"],
                        q["difficulty"],
                        q["question"],
                        rank,
                        pdf
                    ])

        print(f"Saved -> {OUTPUT_FILE.name}")

        avg_time = sum(retrieval_times) / len(retrieval_times)

        print(f"\nAverage Retrieval Time : {avg_time:.2f} ms")