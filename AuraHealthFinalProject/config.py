import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load variables from .env
load_dotenv()

# Get API Key
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Create LLM
llm = genai.GenerativeModel(
    "gemini-2.5-flash"
)