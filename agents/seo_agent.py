from utils.openrouter_client import client


def generate_seo(script):

    prompt = f"""
You are an SEO Expert.

Using this video script generate:

1. SEO Optimized Title

2. YouTube Description

3. 15 SEO Keywords

4. 15 Trending Hashtags

Script:

{script}

Use simple English.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=700
    )

    return response.choices[0].message.content