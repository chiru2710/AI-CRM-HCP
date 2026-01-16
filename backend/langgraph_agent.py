import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

def ai_summarize(text: str) -> str:
    if not client:
        return "AI Summary (Fallback): Interaction logged from chat input."

    try:
        response = client.chat.completions.create(
            model="gemma2-9b-it",
            messages=[{"role": "user", "content": f"Summarize this interaction: {text}"}]
        )
        return response.choices[0].message.content

    except Exception as e:
        print("Groq Error:", str(e))
        return "AI Summary (Fallback): Unable to summarize due to API issue."

def process_chat_interaction(user_text: str):
    summary = ai_summarize(user_text)

    hcp_name = "Unknown Doctor"
    samples_given = False

    if "Dr." in user_text:
        hcp_name = user_text.split("Dr.")[1].split()[0]

    if "samples" in user_text.lower():
        samples_given = True

    return {
        "hcp_name": f"Dr. {hcp_name}" if not hcp_name.startswith("Dr.") else hcp_name,
        "interaction_type": "Chat Interaction",
        "purpose": user_text,
        "samples_given": samples_given,
        "follow_up_date": None,
        "summary": summary
    }
