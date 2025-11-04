import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def get_llm():
    """Initialize and return the Gemini model."""

    return ChatGoogleGenerativeAI(
        model="models/gemini-2.5-flash",
        temparature=0.2,
        convert_system_massage_to_human=True
    )