import os
import sys
from dotenv import load_dotenv
import logging

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from openai import OpenAI

# --- Load environment variables from .env file ---
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

# ── Validate API key ────────────────────────────────────────
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
if not OPENAI_API_KEY or OPENAI_API_KEY.startswith("sk-your"):
    logger.error("OPENAI_API_KEY is missing. Copy .env.example → .env and add your key.")
    sys.exit(1)

LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-4o-mini")
EMBEDDINGS_MODEL = os.environ.get("EMBEDDINGS_MODEL", "text-embedding-3-small")

# ── Clients ──────────────────────────────────────────────────
openai_client = OpenAI(api_key=OPENAI_API_KEY)
llm = ChatOpenAI(model=LLM_MODEL, temperature=0.3)
embeddings = OpenAIEmbeddings(model=EMBEDDINGS_MODEL)

logger.info(f"OpenAI clients initialised  (model: {LLM_MODEL}, embeddings: {EMBEDDINGS_MODEL})")