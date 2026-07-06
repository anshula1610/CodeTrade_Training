import os
import chromadb

from sentence_transformers import SentenceTransformer


# -----------------------------
# Load Embedding Model
# -----------------------------

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# -----------------------------
# Create Chroma Database
# -----------------------------

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name="aurahealth"
)

# -----------------------------
# Text Splitter
# -----------------------------

def split_text(text, chunk_size=500, overlap=100):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunks.append(text[start:end])

        start += chunk_size - overlap

    return chunks
# -----------------------------
# Data Folder
# -----------------------------

DATA_FOLDER = "Data"

doc_id = 0

# -----------------------------
# Read Every Text File
# -----------------------------

for filename in os.listdir(DATA_FOLDER):

    if filename.endswith(".txt"):

        filepath = os.path.join(DATA_FOLDER, filename)

        with open(filepath, "r", encoding="utf-8") as file:

            text = file.read()

        chunks = split_text(text)

        for chunk in chunks:

            embedding = embedding_model.encode(chunk).tolist()

            collection.add(

                ids=[str(doc_id)],

                embeddings=[embedding],

                documents=[chunk],

                metadatas=[

                    {

                        "source": filename

                    }

                ]

            )

            doc_id += 1

print("Database Created Successfully!")