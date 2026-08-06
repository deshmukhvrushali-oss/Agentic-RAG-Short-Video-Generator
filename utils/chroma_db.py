import chromadb
import os

# Persistent database
os.makedirs("data", exist_ok=True)

client = chromadb.PersistentClient(path="data/chroma")

collection = client.get_or_create_collection(
    name="research_documents"
)


def store_documents(topic, content):
    """
    Store research in ChromaDB
    """

    try:
        collection.delete(ids=[topic])
    except:
        pass

    collection.add(
        ids=[topic],
        documents=[content]
    )


def retrieve(topic):
    """
    Retrieve research from ChromaDB
    """

    result = collection.query(
        query_texts=[topic],
        n_results=1
    )

    docs = result.get("documents", [])

    if docs and len(docs[0]) > 0:
        return docs[0][0]

    return ""