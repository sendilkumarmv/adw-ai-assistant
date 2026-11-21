
from langchain_core.documents import Document
from langchain_chroma import Chroma


from config import embeddings, get_logger
from data import load_products

logger = get_logger("rag")

def _build_document() -> list[Document]:
    products = load_products()
    docs: list[Document] = []
    if len(products) == 0:
        return docs

    for p in products:
        content = (
            f"Product ID: {p['productId']}\n"
            f"Product: {p['name']}\n"
            f"Category: {p['category']}\n"
            f"Subcategory: {p['subcategory']}\n"
            f"Brand: {p['brand']}\n"
            f"Description: {p['description']}\n"
            f"Price: {p['price']} {p['currency']}\n"
            f"Stock: {p['stock']}\n"
            f"Rating: {p['rating']}\n"
            f"Review Count: {p['reviewCount']}\n"
            f"SKU: {p['sku']}\n"
            f"Color: {p['color']}\n"
            f"Weight (kg): {p['weightKg']}\n"
            f"Active: {p['isActive']}\n"
            f"Created At: {p['createdAt']}\n"
        )
        docs.append(
            Document(
                page_content=content, 
                metadata={
                    "id": p["productId"],
                    "name": p["name"],
                    "brand": p["brand"],
                    "category": p["category"],
                    "price": p["price"],
                    "rating": p["rating"],
                }
            )
        )

    return docs


def build_vector_store() -> Chroma:
    docs = _build_document()
    vector_store = Chroma.from_documents(
        embedding=embeddings,
        documents=docs,
        collection_name="adw_products"
    )
    logger.info(f"Vector store is ready with {len(docs)} projects")
    return vector_store

product_vector_store = build_vector_store()
