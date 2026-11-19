
from langchain_core.documents import Document
from langchain_chroma import Chroma

from src.config import embeddings


def _build_document() -> list[Document]:
    pass


def build_vector_store() -> Chroma:
    docs = _build_document()
    vector_store = Chroma.from_documents(
        embedding=embeddings,
        documents=docs,
        collection_name="adw_products"
    )
    return vector_store