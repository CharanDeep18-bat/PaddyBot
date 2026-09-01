from langchain_community.vectorstores import FAISS
from embeddings import get_embedding_model
from config import TOP_K, VECTOR_DB_PATH


def get_retriever():
    """
    Load the saved FAISS vector database
    and return a retriever.
    """

    embedding_model = get_embedding_model("sentence-transformers/all-MiniLM-L6-v2")

    vectordb = FAISS.load_local(
        VECTOR_DB_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )

    retriever = vectordb.as_retriever(
        search_kwargs={"k": TOP_K}
    )

    return retriever