# STREAMLIT APPLICATION FOR SCHOLARSHIP CHATBOT

import streamlit as st
from rag_chain import get_rag_chain

st.set_page_config(page_title="Scholarship Chatbot", page_icon="🎓")
st.title("Scholarship Chatbot")
st.caption("Ask me about eligibility, income, categories, deadlines, etc.")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

rag_chain = get_rag_chain()

# Display chat messages from history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input in chat-like field
user_input = st.chat_input("Ask a scholarship question...")
if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)

    # Run RAG model
    with st.spinner("Thinking..."):
        result = rag_chain({"query": user_input})
        response = result["result"]

    # Display bot response
    st.chat_message("assistant").markdown(response)

    # Save interaction in session state
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.session_state.chat_history.append({"role": "assistant", "content": response})
