from agents.planner_agent import plan
from agents.research_agent import research
from agents.script_agent import generate_script
from agents.seo_agent import generate_seo
from agents.image_agent import download_images
from agents.voice_agent import generate_voice
from agents.video_agent import create_video
from agents.review_agent import review

import os

print("=" * 50)
print("Agentic RAG Short Video Generator")
print("=" * 50)

topic = input("Enter Topic: ")

# Create output folder
os.makedirs("output", exist_ok=True)

# ===========================
# Planner Agent
# ===========================

planner_output = plan(topic)

with open("output/plan.txt", "w", encoding="utf-8") as f:
    f.write(planner_output)

print("\nPlanner Agent Completed\n")
print(planner_output)

# ===========================
# Research Agent
# ===========================

research_report = research(topic)

with open("output/research.txt", "w", encoding="utf-8") as f:
    f.write(research_report)

print("✅ Research Completed")

# ===========================
# Script Agent
# ===========================

script = generate_script(research_report)

with open("output/script.txt", "w", encoding="utf-8") as f:
    f.write(script)

print("✅ Script Completed")

# ===========================
# SEO Agent
# ===========================

seo = generate_seo(script)

with open("output/seo.txt", "w", encoding="utf-8") as f:
    f.write(seo)

print("✅ SEO Completed")

# ===========================
# Image Agent
# ===========================

download_images(topic)

print("✅ Images Downloaded")

# ===========================
# Voice Agent
# ===========================

voice_file = generate_voice(script)

print("✅ Voice Saved:", voice_file)

# ===========================
# Video Agent
# ===========================

create_video()

print("✅ Video Created")

# ===========================
# Review Agent
# ===========================

review()

print("\n")
print("=" * 50)
print("PROJECT COMPLETED SUCCESSFULLY")
print("=" * 50)