import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


def create_vector_store(pdf_path: str, index_path: str = "faiss_index"):
    """Load and embed HR documents into a FAISS index."""
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    # Split into smaller chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    # load the Embedding Model
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(index_path)
    return db
