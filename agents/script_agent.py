from utils.openrouter_client import client


def generate_script(research_text):

    prompt = f"""
You are an expert YouTube Shorts script writer.

Using the research below, create a 45–60 second short video script.

Research:
{research_text}

Generate in this format:

🎬 Hook

🟢 Scene 1

🟢 Scene 2

🟢 Scene 3

📢 Call To Action

Use simple English.
Keep it engaging.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=800
    )

    return response.choices[0].message.content