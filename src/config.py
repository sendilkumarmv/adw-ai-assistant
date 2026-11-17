import os
import sys
from dotenv import load_dotenv
import logging

load_dotenv()

def get_logger(name: str) -> logging.Logger: 
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(
            logging.Formatter("%(asctime)s | %(name)-18s | %(levelname)-7s | %(message)s",
                              datefmt="%H:%M:%S")
        )
        logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

logger = get_logger("config")

openai_api_key = os.environ.get("OPENAI_API_KEY")
if not openai_api_key or openai_api_key.startswith("sk-your"):
    logger.error("OPENAI_API_KEY is not set in the environment variables.")
    sys.exit(1)
else:
    logger.info("OPENAI_API_KEY is set.")