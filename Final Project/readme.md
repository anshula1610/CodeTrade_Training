# AuraHealth Nexus RAG System

## Overview

This project implements a Retrieval-Augmented Generation (RAG) system for the fictional healthcare company **AuraHealth Nexus**. The application retrieves relevant information from internal documents and uses Google's Gemini model to generate accurate answers based only on the retrieved context.

The project was developed as part of a RAG Capstone assignment.

---

## Features

- Load and process multiple text documents
- Text chunking for efficient retrieval
- SentenceTransformer embeddings
- ChromaDB vector database
- Semantic similarity search
- Gemini-powered answer generation
- Context-aware responses with minimal hallucination

---

## Project Structure

```
.
├── synthetic_data/
│   ├── document1.txt
│   ├── ...
│   └── document10.txt
├── final_project.ipynb
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Sentence Transformers
- ChromaDB
- Google Gemini API
- tqdm

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Create a virtual environment (recommended):

```bash
python -m venv venv
```

Activate it.

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a Google AI Studio API key.

Set the API key in your notebook or as an environment variable:

```python
GOOGLE_API_KEY = "YOUR_API_KEY"
```

or

```bash
export GOOGLE_API_KEY="YOUR_API_KEY"
```

---

## Running the Project

Open the notebook:

```bash
jupyter notebook final_project.ipynb
```

Run all cells sequentially.

The notebook will:

1. Load all documents
2. Split them into chunks
3. Generate embeddings
4. Store embeddings in ChromaDB
5. Retrieve the most relevant chunks
6. Generate answers using Gemini

---

## Workflow

```
Documents
      │
      ▼
Text Chunking
      │
      ▼
SentenceTransformer Embeddings
      │
      ▼
ChromaDB
      │
      ▼
Semantic Search
      │
      ▼
Retrieved Context
      │
      ▼
Gemini LLM
      │
      ▼
Final Answer
```

---

## Example Query

```
What override code must be used during the Cognitive Reset Sequence?
```

The system retrieves the relevant document chunks and generates an answer strictly from the retrieved context.

---

## Future Improvements

- Conversational memory
- Hybrid search (keyword + semantic)
- Streamlit web interface
- Metadata filtering
- Persistent Chroma database
- Better chunking strategies
- Evaluation metrics for retrieval quality

---

## Author

Anshula
Arya college of engineering and I.T.