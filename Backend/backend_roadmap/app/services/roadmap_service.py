import os
import requests
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
MODEL_NAME = os.getenv("HF_MODEL")

API_URL = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"

headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_KEY}"
}

def generate_ai_roadmap(career: str):
    prompt = (
        f"Generate a step-by-step learning roadmap for a beginner who wants to become a "
        f"{career}. Include around 8 to 10 steps, clearly numbered."
    )

    payload = {
    "inputs": prompt,
    "options": {
        "wait_for_model": True
    }
}

    response = requests.post(API_URL, headers=headers, json=payload)

    # DEBUG: print response if error
    if response.status_code != 200:
        print("Hugging Face Error:", response.status_code, response.text)
        return None

    result = response.json()

    # Sometimes HF returns a dict instead of list
    if isinstance(result, dict) and "error" in result:
        print("HF Model Error:", result["error"])
        return None

    # Normal successful response
    generated_text = result[0]["generated_text"]
    return generated_text

def get_resources_for_step(step_title: str):
    return {
        "youtube": [
            "https://www.youtube.com/results?search_query=" + step_title.replace(" ", "+")
        ],
        "courses": [
            "https://www.coursera.org/search?query=" + step_title.replace(" ", "+")
        ]
    }
