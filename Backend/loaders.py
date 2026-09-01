from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from config import PDF_FOLDER


def load_documents():
    """
    Load all PDF files from the knowledge base.
    Returns a list of LangChain Document objects.
    """

    loader = DirectoryLoader(
        PDF_FOLDER,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader
    )

    documents = loader.load()
    return documents