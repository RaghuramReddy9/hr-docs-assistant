from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from llm import get_llm
import asyncio

# Embedding model with event loop guard (safe for Streamlit)
def get_embedding_model():
    try:
        asyncio.get_event_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())
    return GoogleGenerativeAIEmbeddings(model="models/embedding-001")

def get_chain():
    embeddings = get_embedding_model()
    vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

    retriever = vectorstore.as_retriever()
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        input_key="question",   
        output_key="answer"     
    )

    chain = ConversationalRetrievalChain.from_llm(
        llm=get_llm(),
        retriever=retriever,
        memory=memory,
        return_source_documents=True,
        output_key="answer", 
        verbose=True
    )

    return chain
