from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import PromptTemplate
from backend.llm import get_llm

def load_vector_store(index_path: str = "chroma_index"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return Chroma(persist_directory=index_path, embedding_function=embeddings)


def create_rag_chain():
    """Create a modern retrieval chain (retriever + LLM combine chain)."""
    llm = get_llm()
    db = load_vector_store()
    retriever = db.as_retriever(search_kwargs={"k":3})

    template = """
    You are an HR assistant helping employees understand HR policies.

    Use the following context sections to answer the question factually.
    If the answer isn't contained in the context, say "I could not find that information in the policy."

    Context:
    {context}

    Question:
    {input}

    Answer clearly and concisely:
    """

    prompt = PromptTemplate(template=template, input_variables=["context", "input"])

    # create a combine-documents chain
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)

    # create the retrieval chain
    retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

    return retrieval_chain