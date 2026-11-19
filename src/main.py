from config import get_logger
from data import load_products

def main():
    logger = get_logger("main")
    logger.info("ADW AI is running...")
    products = load_products()
    logger.info("Loaded %d products", len(products))

if __name__ == "__main__":
    main()