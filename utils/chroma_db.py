import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="research_documents"
)

model = SentenceTransformer("all-MiniLM-L6-v2")


def store_documents(search_results):

    ids = []
    docs = []

    for i, item in enumerate(search_results["results"]):

        ids.append(str(i))

        docs.append(
            f"""
Title:
{item['title']}

Content:
{item['content']}

Source:
{item['url']}
"""
        )

    collection.add(
        ids=ids,
        documents=docs
    )


def retrieve(query):

    result = collection.query(
        query_texts=[query],
        n_results=3
    )import chromadb

client = chromadb.PersistentClient(path="data/chroma")

collection = client.get_or_create_collection(
    name="research_documents"
)


def store_documents(topic, content):
    collection.add(
        documents=[content],
        ids=[topic]
    )


def retrieve(topic):
    result = collection.query(
        query_texts=[topic],
        n_results=1
    )

    if result["documents"]:
        return result["documents"][0][0]

    return ""

    return result["documents"][0]