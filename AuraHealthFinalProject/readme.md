# 🏥 AuraHealth Nexus - Retrieval Augmented Generation (RAG)

## 📌 Project Overview

AuraHealth Nexus is an AI-powered healthcare assistant built using Retrieval-Augmented Generation (RAG). The assistant answers questions only from the provided internal healthcare documents, reducing hallucinations and improving response accuracy.

The project uses semantic search with ChromaDB and Sentence Transformers, while Google Gemini generates context-aware responses.

---

## 🚀 Features

- Load multiple healthcare text documents
- Automatic document chunking
- Semantic search using embeddings
- ChromaDB Vector Database
- Google Gemini Integration
- Streamlit Chat Interface
- Source Document Citation
- Similarity Distance Display
- Conversational Memory
- Multiple Chat Sessions

---

## 🛠 Technologies Used

- Python
- Streamlit
- ChromaDB
- Sentence Transformers
- Google Gemini API
- LangChain (Utilities)

---

## 📂 Project Structure

```
AuraHealthFinalProject/
│
├── Data/
│   ├── AuraHealth_Employee_Handbook_2026.txt
│   ├── NeuroCrystal_Syndrome_Guidelines.txt
│   ├── OmniHeal_Memo_And_Project_Details.txt
│   └── ...
│
├── chroma_db/
│
├── app.py
├── config.py
├── create_database.py
├── database.py
├── rag.py
├── test_rag.py
├── requirements.txt
├── README.md
└── .env
```

---

## ⚙ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory

```bash
cd AuraHealthFinalProject
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API

Create a `.env` file

```text
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## 📦 Create Vector Database

```bash
python create_database.py
```

---

## 🧪 Test Retrieval

```bash
python test_rag.py
```

---

## ▶ Run Streamlit Application

```bash
streamlit run app.py
```

---

## 💬 Example Questions

- What is NeuroCrystal Syndrome?
- Who is the Head of the OmniHeal initiative?
- What is the treatment for Phase 2?
- What override code must be used during the Cognitive Reset Sequence?
- What specific technology powers AuraHealth facilities?
- Who reviews AI-generated recommendations from MediMind?

---

## 📈 Workflow

```
Documents
      │
      ▼
Document Loader
      │
      ▼
Text Chunking
      │
      ▼
Sentence Transformer Embeddings
      │
      ▼
ChromaDB
      │
      ▼
Semantic Retrieval
      │
      ▼
Google Gemini
      │
      ▼
Final Response + Source Documents
```

---

## 📊 Project Architecture

```
User
 │
 ▼
Streamlit GUI
 │
 ▼
RAG Pipeline
 │
 ├── Embed Query
 │
 ├── Search ChromaDB
 │
 ├── Retrieve Top-K Chunks
 │
 └── Send Context to Gemini
 │
 ▼
Answer + Sources
```

---

## 🎯 Evaluation

The application is capable of answering all evaluation questions by retrieving information only from the supplied documents.

---

## 👨‍💻 Author

**Anshula**

Built as a Retrieval-Augmented Generation (RAG) Capstone Project using Google Gemini and ChromaDB.