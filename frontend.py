import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:5000"  

st.title("Chat with 10k Report PDF")

# Upload PDF
uploaded_file = st.file_uploader("Upload your 10-K Report (PDF)", type="pdf")
if uploaded_file:
    with st.spinner("Indexing the PDF..."):
        response = requests.post(f"{BACKEND_URL}/upload", files={"file": uploaded_file})
        if response.status_code == 200:
            st.success(response.json().get('message'))
        else:
            st.error("Failed to index the PDF. Please try again.")

# Query the PDF
query = st.text_input("Ask a question about the PDF:")
if query:
    with st.spinner("Fetching the answer..."):
        response = requests.post(f"{BACKEND_URL}/query", json={"query": query})
        if response.status_code == 200:
            st.write(response.json().get('response'))
        else:
            st.error("Failed to get a response. Please try again.")
