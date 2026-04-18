from sentence_transformers import SentenceTransformer
import chromadb
from documents import documents

EMBED_MODEL_NAME = "all-MiniLM-L6-v2"
COLLECTION_NAME = "study_buddy_kb"

embedder = SentenceTransformer(EMBED_MODEL_NAME)

chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name=COLLECTION_NAME)

existing = collection.get()
existing_ids = set(existing.get("ids", [])) if existing else set()

for doc in documents:
    if doc["id"] not in existing_ids:
        embedding = embedder.encode(doc["text"]).tolist()
        collection.add(
            ids=[doc["id"]],
            documents=[doc["text"]],
            embeddings=[embedding],
            metadatas=[{"topic": doc["topic"]}]
        )