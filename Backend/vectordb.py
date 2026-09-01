from langchain_community.vectorstores import FAISS
import os


def create_vector_database(chunks, embedding_model):
    """
    Create and save a FAISS vector database.
    """

    vectordb = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    # Create folder if it doesn't exist
    os.makedirs("faiss_index", exist_ok=True)

    # Save the index locally
    vectordb.save_local("faiss_index")

    return vectordb