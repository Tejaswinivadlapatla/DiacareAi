from pathlib import Path
import os

from dotenv import load_dotenv
from google import genai


PROJECT_FOLDER = Path(__file__).resolve().parent.parent
ENV_PATH = PROJECT_FOLDER / ".env"

load_dotenv(ENV_PATH)

API_KEY = os.getenv("GEMINI_API_KEY")
print("API Key:", API_KEY)


def ask_diacare_ai(question, conversation_history):
    if not API_KEY:
        return (
            "Gemini API key was not found. Check that your .env file contains:\n"
            "GEMINI_API_KEY=your_key_here"
        )

    system_instruction = """
You are DiaCare AI, a friendly diabetes-awareness and nutrition assistant.

Rules:
- Give general educational information only.
- Do not diagnose diabetes or prescribe medicines.
- Encourage users to consult a qualified doctor for symptoms, emergencies,
  medication decisions, pregnancy-related concerns, or abnormal test results.
- If a user mentions chest pain, severe weakness, confusion, fainting, severe
  dehydration, difficulty breathing, or very high/low blood sugar symptoms,
  tell them to seek urgent medical help.
- Keep answers simple, supportive, and practical.
- Use short paragraphs or bullet points.
"""

    history_text = ""

    for user_message, assistant_message in conversation_history[-5:]:
        history_text += f"User: {user_message}\n"
        history_text += f"DiaCare AI: {assistant_message}\n"

    prompt = f"""
{system_instruction}

Previous conversation:
{history_text}

User question:
{question}
"""

    try:
        client = genai.Client(api_key=API_KEY)

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        if response.text:
            return response.text

        return "I could not create a response. Please try again."

    except Exception:
        return (
            "I could not connect to Gemini right now. "
            "Please check your internet connection and API key."
        )