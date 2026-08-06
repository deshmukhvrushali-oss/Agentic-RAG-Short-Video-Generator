from utils.openrouter_client import client
from config import LLM_MODEL


def plan(topic):

    prompt = f"""
You are an expert YouTube Shorts content planner.

Topic: {topic}

Create a professional short video plan.

Return ONLY in this format.

TITLE:
INTRO:
SCENE 1:
SCENE 2:
SCENE 3:
SCENE 4:
SCENE 5:
OUTRO:

Each scene should contain only 1-2 short sentences.

Language: English.
"""

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content