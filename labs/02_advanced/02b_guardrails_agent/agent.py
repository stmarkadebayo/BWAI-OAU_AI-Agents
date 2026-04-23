from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmResponse, LlmRequest
from typing import Optional
from google.genai import types

# ==============================================================================
# Callbacks & Guardrails: The Agent's Immune System
# ==============================================================================
# In production, you can't just let an LLM do whatever it wants.
# What if a user asks your customer service bot to write malware?
# What if someone tries prompt injection to bypass your instructions?
#
# CALLBACKS are hooks that intercept the agent's execution at key points:
#   - before_model_callback  → Runs BEFORE every LLM call
#   - after_model_callback   → Runs AFTER every LLM call
#   - before_tool_callback   → Runs BEFORE every tool execution
#   - after_tool_callback    → Runs AFTER every tool execution
#
# If a before_model_callback returns an LlmResponse, the real LLM is SKIPPED.
# This is how you build guardrails — you intercept and block bad requests.
# ==============================================================================


# --- The Guardrail Function ---
# This runs BEFORE every single message is sent to the LLM.
BLOCKED_TOPICS = ["hack", "exploit", "jailbreak", "ignore your instructions"]

def safety_guardrail(
    callback_context: CallbackContext, llm_request: LlmRequest
) -> Optional[LlmResponse]:
    """Inspects user input and blocks requests containing forbidden topics.
    
    - Returns None → Allow the request (proceed to LLM as normal).
    - Returns LlmResponse → BLOCK the request (skip the LLM entirely).
    """
    agent_name = callback_context.agent_name
    print(f"[🛡️ Guardrail] Checking input for agent: {agent_name}")

    # Extract the user's latest message from the request
    last_user_message = ""
    if llm_request.contents and llm_request.contents[-1].role == 'user':
        if llm_request.contents[-1].parts:
            last_user_message = llm_request.contents[-1].parts[0].text
    
    print(f"[🛡️ Guardrail] User said: '{last_user_message}'")

    # Check for blocked topics
    message_lower = last_user_message.lower()
    for topic in BLOCKED_TOPICS:
        if topic in message_lower:
            print(f"[🛡️ Guardrail] ⛔ BLOCKED — found '{topic}' in message!")
            
            # Return a canned response — the LLM never even sees this message
            return LlmResponse(
                content=types.Content(
                    role="model",
                    parts=[types.Part(text=(
                        "⛔ I'm sorry, but I can't help with that topic. "
                        "This request was blocked by a safety guardrail. "
                        "Please ask something else!"
                    ))],
                )
            )

    # No issues found — let the request through to the LLM
    print("[🛡️ Guardrail] ✅ Input is clean. Proceeding to LLM.")
    return None


# --- The Agent with the Guardrail Attached ---
root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant protected by safety guardrails.',
    instruction='''You are a helpful, friendly coding tutor for university students.
You answer questions about programming, algorithms, data structures, and software engineering.
Be encouraging and use simple explanations with examples.''',
    before_model_callback=safety_guardrail,  # ← The magic line!
)
