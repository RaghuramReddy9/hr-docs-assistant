import streamlit as st
from backend.ingest import build_vector_store
from backend.rag_chain import create_rag_chain
import os

st.set_page_config(page_title="HR Document Assistant", page_icon="💼", layout="wide")
st.markdown("""
<style>
.stTextInput, .stButton>button {font-size:16px;}
h1 {color:#0a66c2;}
</style>
""", unsafe_allow_html=True)


st.title("HR Document Assistant")
st.markdown("Ask questions about HR policies and employee guidelines.")

# Initialize session state
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = build_vector_store()

uploaded = st.sidebar.file_uploader("Upload HR Policy PDF", type=["pdf"])
if uploaded:
    temp_path = os.path.join("data", uploaded.name)
    with open(temp_path, "wb") as f:
        f.write(uploaded.read())
    build_vector_store(temp_path)
    st.session_state.qa_chain = create_rag_chain()
    st.sidebar.success("Knowledge base updated!")

question = st.text_input("Enter your question:")

if st.button("Ask") and question:
    result = st.session_state.qa_chain.invoke({"input": question})
    st.write("### Answer")
    st.write(result.get("answer", "No answer found."))

    if "context" in result:
        with st.expander("View referenced policy context"):
            st.write(result["context"])
