# RAG Chat Bot

This project allows users to upload a PDF document and ask questions about its content. The system uses natural language processing (NLP) techniques to index the PDF, and then provides accurate answers based on user queries. The application consists of a frontend built with Streamlit and a backend using Flask.

---

## Features
- Upload a PDF document.
- Automatically indexes the PDF for quick retrieval.
- Ask questions about the content and receive detailed answers.
- Interactive and user-friendly interface.

---

## Tech Stack

### Frontend
- **Streamlit**: For building the interactive web application.
- **Requests**: For communicating with the backend API.

### Backend
- **Flask**: Backend framework for handling API requests.
- **PyPDF2**: To extract text from the uploaded PDF.
- **HuggingFace Sentence Transformers**: For embedding the text content of the PDF.
- **FAISS**: For vector storage and similarity search.
- **LangChain**: To integrate embeddings and build a retrieval-based question-answering system.

### APIs and Models
- **HuggingFaceEmbeddings**: Pretrained embeddings for semantic search.
- **OpenAI GPT-3.5 Turbo**: Used for natural language question-answering.

---

## Prerequisites

- Python 3.7+
- OpenAI API Key (for GPT-based question answering)

---

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo-name/rag-chat-bot.git
   cd rag-chat-bot
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```env
     OPENAI_API_KEY=your_openai_api_key_here
     ```

5. **Run the Backend**
   ```bash
   python backend.py
   ```
   The backend will run on `http://127.0.0.1:5000`.

6. **Run the Frontend**
   ```bash
   streamlit run frontend.py
   ```
   The frontend will open in your browser, or you can access it at `http://localhost:8501`.

---

## Usage

1. Upload a PDF document using the file uploader in the Streamlit app.
2. Wait for the indexing process to complete.
3. Enter your question in the query box and get the answer instantly.

---

## Project Structure
```
rag-chat-bot/
├── backend.py         # Flask backend
├── frontend.py        # Streamlit frontend
├── requirements.txt   # Python dependencies
└── README.md          # Documentation
```

---

## Acknowledgments
- [OpenAI](https://openai.com/) for GPT models.
- [HuggingFace](https://huggingface.co/) for embedding models.
- [LangChain](https://langchain.com/) for simplifying the question-answering pipeline.

