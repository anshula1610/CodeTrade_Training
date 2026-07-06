import chromadb
from sentence_transformers import SentenceTransformer

# ---------------------------------
# Load Embedding Model
# ---------------------------------
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# ---------------------------------
# Connect to ChromaDB
# ---------------------------------
client = chromadb.PersistentClient(
    path="chroma_db"
)

# ---------------------------------
# Open Collection
# ---------------------------------
collection = client.get_collection(
    "aurahealth"
)

# ---------------------------------
# Retrieve Documents
# ---------------------------------
def retrieve_with_sources(question, top_k=5):

    # Convert question into embedding
    question_embedding = embedding_model.encode(question).tolist()

    # Retrieve top-k similar chunks
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_k,
        include=[
            "documents",
            "metadatas",
            "distances"
        ]
    )

    return results