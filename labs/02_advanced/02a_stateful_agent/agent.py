from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from google.adk.tools import ToolContext

# ==============================================================================
# Session State: Giving Your Agent Memory
# ==============================================================================
# Without state, every message is a blank slate. The agent forgets everything
# between turns. With session state, the agent can remember facts, preferences,
# and context across the entire conversation.
#
# HOW IT WORKS:
# - ADK provides a `ToolContext` object to any tool that requests it.
# - `tool_context.state` is a dictionary that persists for the session.
# - You can also use `{key_name}` in the agent's instruction to inject
#   state values directly into the prompt!
# ==============================================================================


def remember_fact(key: str, value: str, tool_context: ToolContext) -> str:
    """Saves a piece of information about the user to memory.

    Args:
        key: A short label for what to remember (e.g. 'name', 'favorite_color', 'city').
        value: The actual value to remember (e.g. 'Alice', 'blue', 'Lagos').
        tool_context: Automatically provided by ADK — do NOT pass this yourself.
    """
    tool_context.state[key] = value
    return f"✅ Got it! I'll remember that your {key} is '{value}'."


def recall_memory(tool_context: ToolContext) -> str:
    """Retrieves everything the agent currently remembers about the user.

    Args:
        tool_context: Automatically provided by ADK — do NOT pass this yourself.
    """
    state = tool_context.state
    if not state:
        return "🤔 I don't remember anything about you yet. Tell me something!"

    memories = "\n".join([f"  • {k}: {v}" for k, v in state.items()])
    return f"📋 Here's what I remember:\n{memories}"


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A personal assistant that remembers things about you.',
    instruction='''You are a friendly personal assistant with memory.

YOUR CAPABILITIES:
- You can REMEMBER things users tell you using the `remember_fact` tool.
- You can RECALL everything you know about the user using the `recall_memory` tool.

BEHAVIOR:
- When a user shares personal info (name, location, hobbies, preferences), 
  use `remember_fact` to save it immediately.
- When a user asks "what do you know about me?" or similar, use `recall_memory`.
- Always be warm and reference what you know about the user in conversation.
- If the user hasn't told you anything yet, encourage them to share!

EXAMPLES OF THINGS TO REMEMBER:
- "My name is Tobi" → remember_fact(key="name", value="Tobi")
- "I love jollof rice" → remember_fact(key="favorite_food", value="jollof rice")
- "I'm studying Computer Science" → remember_fact(key="course", value="Computer Science")
''',
    tools=[FunctionTool(remember_fact), FunctionTool(recall_memory)]
)
