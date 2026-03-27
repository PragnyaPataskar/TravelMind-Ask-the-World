from src.rag.vectorstore import get_vectorstore

def get_retriever():
    vectordb = get_vectorstore()
    return vectordb.as_retriever(search_kwargs={"k": 3})