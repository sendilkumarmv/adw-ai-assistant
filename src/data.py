import json
from pathlib import Path
from typing import Any


PRODUCTS_FILE = Path(__file__).resolve().parent.parent / "data" / "products_5000.json"

# dict[str, Any] instead of just dict to enforce key is only string.
def load_products() -> list[dict[str, Any]]:
    """Load product records from the workspace's products JSON file."""
    with PRODUCTS_FILE.open(encoding="utf-8") as file:
        products = json.load(file)

    if not isinstance(products, list) or not all(
        isinstance(product, dict) for product in products
    ):
        raise ValueError(f"Expected a JSON array of product objects in {PRODUCTS_FILE}")

    return products