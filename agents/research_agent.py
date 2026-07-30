from utils.openrouter_client import client
from utils.chroma_db import store_documents, retrieve


def research(topic):

    old_data = retrieve(topic)

    prompt = f"""
Topic:
{topic}

Previous Knowledge:
{old_data}

Write a detailed research report.

Include:

Introduction

Latest Information

Applications

Advantages

Disadvantages

Future Scope

Conclusion
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
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