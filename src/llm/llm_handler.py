from langchain_community.chat_models import ChatOpenAI
#from langchain_community.llms import HuggingFacePipeline
from src.config import GROQ_API_KEY

def get_llm():
    try:
        llm = ChatOpenAI(
            openai_api_key=GROQ_API_KEY,
            openai_api_base="https://api.groq.com/openai/v1",
            model_name="llama-3.1-8b-instant",
            temperature=0.3
        )
        return llm
    except Exception as e:
        raise RuntimeError(
            "No valid chat-compatible LLM found. Please check your GROQ_API_KEY or use a supported chat model. "
            f"Original error: {e}"
        )