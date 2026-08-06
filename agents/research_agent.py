from utils.openrouter_client import client
from utils.chroma_db import store_documents, retrieve
import time

start = time.time()

response = client.chat.completions.create(
    ...
)

print(f"Research API Time: {time.time() - start:.2f} seconds")

def research(topic):

    # Check cache
    old_data = retrieve(topic)

    if old_data.strip():
        print("Research found in ChromaDB")
        return old_data

    print("Generating new research...")

    prompt = f"""
Topic:
{topic}

Write a detailed research report.

Include:

1. Introduction
2. Latest Information (2026)
3. Applications
4. Advantages
5. Disadvantages
6. Future Scope
7. Conclusion

Return proper Markdown.
"""

    response = client.chat.completions.create(
        model="google/gemma-4-26b-a4b-it:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    text = response.choices[0].message.content

    store_documents(topic, text)

    return text