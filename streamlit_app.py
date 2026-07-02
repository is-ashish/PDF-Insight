# streamlit_app.py
import streamlit as st
import requests

# Streamlit UI
st.title("📄 PDF-Insights ...")
st.write("Ask Questions From Your Ingested Documents.")

# Maintain chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
if user_query := st.chat_input("🔍 Query Documents ..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    try:
        # Call FastAPI backend
        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={"question": user_query}
        )
        response.raise_for_status()
        answer = response.json().get("answer", "⚠️ No answer returned")

    except Exception as e:
        answer = f"❌ Error contacting backend: {e}"

    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
