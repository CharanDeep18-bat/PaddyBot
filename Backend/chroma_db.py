from langchain_chroma import Chroma

def create_chroma_database(chunks, embeddings, collection_name):

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=collection_name
    )

    return vectordb