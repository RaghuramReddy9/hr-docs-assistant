# 🧾 HR Document Assistant

A conversational AI assistant that helps employees query HR policies like leave, insurance, laptop use, and remote work policies — built using LangChain, FAISS, Gemini 1.5 Flash, and memory.

## Features
- RAG-based document question answering
- Powered by Google Gemini + FAISS
- Context memory across multiple queries
- Modular design with LangChain components

## Tech Stack
- LangChain
- Google Generative AI (Gemini 1.5 Flash)
- FAISS Vector Store
- Streamlit UI
- Python (3.10+)

## Folder Structure
├── app.py
├── rag_chain.py
├── ingest.py
├── llm.py
├── data/
│ └── hr_policies.pdf
├── faiss_index/
│ ├── index.faiss
│ └── index.pkl
├── .env
└── requirements.txt

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
x
## Use Case
```
HR teams can deploy this assistant to reduce repetitive queries from employees. It responds to policy-related questions in a natural language format with citation-based evidence.
```
