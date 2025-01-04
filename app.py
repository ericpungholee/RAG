from flask import Flask, request, jsonify
from PyPDF2 import PdfReader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI


app = Flask(__name__)

# Initialize the embeddings model and vector store
hf_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = None  

@app.route('/upload', methods=['POST'])
def upload_pdf():
    global vector_store
    file = request.files['file']
    
    # Extract text from PDF
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    # Chunk the text
    chunk_size = 500
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    
    # Use HuggingFaceEmbeddings to compute embeddings
    vector_store = FAISS.from_texts(chunks, hf_embeddings)
    
    return jsonify({'message': 'PDF indexed successfully'})

@app.route('/query', methods=['POST'])
def query():
    global vector_store
    if vector_store is None:
        return jsonify({'error': 'No PDF has been uploaded yet.'}), 400
    
    query_text = request.json.get('query', '')
    if not query_text:
        return jsonify({'error': 'Query text is required.'}), 400
    
   
    retriever = vector_store.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY),
        retriever=retriever,
        chain_type="stuff"
    )
    response = qa_chain.run(query_text)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
