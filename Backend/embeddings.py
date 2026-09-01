from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model(model_name):
    """
    Load any Hugging Face embedding model.
    """

    return HuggingFaceEmbeddings(
        model_name=model_name
    )