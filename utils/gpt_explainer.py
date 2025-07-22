import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # Make sure environment variables are loaded

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def get_gpt_feedback(faces, metadata):
    prompt = f"""
You are a deepfake detection assistant.

The uploaded image has {len(faces)} face(s).
Metadata:
{metadata}

Analyze whether this image could be a deepfake based on the number of faces and metadata. Suggest what further analysis (technical or visual) could be done to be more certain.
"""
    response = model.generate_content(prompt)
    return response.text
