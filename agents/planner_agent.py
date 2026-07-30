from utils.openrouter_client import client


def plan(topic):

    prompt = f"""
You are an AI Planner Agent.

Create a plan for generating a short educational video.

Topic:
{topic}

Return the plan in this format:

Topic:
Video Type:
Duration:
Number of Scenes:
Target Audience:
Language:
Voice Style:
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=300
    )

    return response.choices[0].message.content