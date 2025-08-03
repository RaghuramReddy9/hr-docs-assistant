import streamlit as st
from rag_chain import get_chain

st.set_page_config(page_title="HR Assistant", layout="centered")
st.title("HR Document Assistant")

# Initialize session state
if "chain" not in st.session_state:
    st.session_state.chain = get_chain()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_input = st.text_input("Ask a question about HR policies:")

# Run chain
if user_input:
    result = st.session_state.chain.invoke({
        "question": user_input,
        "chat_history": st.session_state.chat_history
    })

    response = result["answer"]
    sources = result.get("source_documents", [])

    st.session_state.chat_history.append((user_input, response, sources))

    # Display chat history
    for q, a, src in st.session_state.chat_history:
        st.markdown(f"**You:** {q}")
        st.markdown(f"**Bot:** {a}")

        # Show sources if available
        if src:
            with st.expander("View Sources"):
                for i, doc in enumerate(src, 1):
                    st.markdown(f"**Source {i}:** {doc.metadata.get('source', 'Unknown file')}")
