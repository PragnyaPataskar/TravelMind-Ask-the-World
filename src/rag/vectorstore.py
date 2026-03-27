from langchain_community.vectorstores import Chroma
from src.rag.embeddings import get_embeddings
from src.config import VECTOR_DB_DIR

def get_vectorstore():
    embeddings = get_embeddings()
    return Chroma(persist_directory=VECTOR_DB_DIR, embedding_function=embeddings)