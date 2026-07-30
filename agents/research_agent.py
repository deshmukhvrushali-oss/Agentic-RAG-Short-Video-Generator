from utils.search import search_web
from utils.openrouter_client import client

def research(topic):

    search_result = search_web(topic)

    context = ""

    for item in search_result["results"]:
        context += f"""
Title: {item['title']}
Content: {item['content']}
Source: {item['url']}

"""

    prompt = f"""
You are an AI Research Assistant.

Using ONLY the information below, create a research summary.

Topic:
{topic}

Information:
{context}

Give:

1. Introduction
2. Latest Updates
3. Important Facts
4. Applications
5. Future Scope

Write in simple English.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=900
    )

    return response.choices[0].message.content