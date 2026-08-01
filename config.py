import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Models
LLM_MODEL = "openai/gpt-oss-20b:free"

# Output
OUTPUT_FOLDER = "output"

# Assets
IMAGE_FOLDER = "assets/images"
MUSIC_FOLDER = "assets/music"
FONT_FOLDER = "assets/fonts"

# Chroma
CHROMA_PATH = "data/chroma"

# Video
VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30