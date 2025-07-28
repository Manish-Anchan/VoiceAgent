import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from logger import logger

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_PROJECT"] = "VoiceAssistant"

llm = ChatGroq(model_name="llama-3.3-70b-versatile")

TEMPLATE = """
You are an AI voice tutor named Genie who helps children aged 6 to 12 improve their English in a fun, safe, and respectful way.

Your goals:
- Use clear, short sentences with simple words that are easy for children to understand.
- Speak slowly and kindly, like a friendly teacher.
- Gently correct mistakes in a positive way, and explain new words or phrases when needed.
- Always be supportive and encouraging to help the child feel confident.
- Never use or repeat any abusive, scary, or inappropriate words—even if the child does.
- After answering, ask a simple follow-up question to help the child keep learning and practicing English.

--- Conversation so far ---
{history_str}
--- New question ---
Child: "{user_input}"
Genie:
"""

prompt = PromptTemplate(
    template=TEMPLATE,
    input_variables=["history_str", "user_input"]
)

chain = prompt | llm

def get_ai_response_with_history(transcribed_text: str, history: list[str], max_turns: int = 2) -> tuple[str, list[str]]:
    keep = max_turns * 2
    recent = history[-keep:]
    lines = []
    for i, msg in enumerate(recent):
        role = "Child" if i % 2 == 0 else "Genie"
        lines.append(f"{role}: \"{msg}\"")
    history_str = "\n".join(lines) if lines else "(no prior turns)"

    try:
        resp = chain.invoke({
            "history_str": history_str,
            "user_input": transcribed_text
        })
        ai_reply = resp.content.strip()
    except Exception as e:
        logger.error(f"LLM invocation failed: {e}")
        raise RuntimeError(f"LLM invocation failed: {e}")

    updated = history + [transcribed_text, ai_reply]
    if len(updated) > keep:
        updated = updated[-keep:]
    return ai_reply, updated
