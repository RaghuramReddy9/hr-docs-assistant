from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from backend.llm import get_llm

def load_vector_store(index_path: str = "faiss_index"):
    """Load existing FAISS index."""
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)

def create_rag_chain():
    """Biuld RAG Pipeline."""
    llm = get_llm()
    db = load_vector_store()
    retriever = db.as_retriever(search_kwargs={"k":3})

    template = """
    You are an HR assistant. Use the following context to answer the question.
    Context: {context}
    Question: {question}
    Provide a clear, factual answer.
    """

    prompt = PromptTemplate(template=template, input_variables=["context", "question"])

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",  
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )
