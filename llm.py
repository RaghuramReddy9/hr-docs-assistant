import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def get_llm():
    return ChatGoogleGenerativeAI(
        model="models/gemini-1.5-flash",
        temparature=0.3,
        convert_system_massage_to_human=True
    )