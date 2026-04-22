from google.adk.agents import Agent
from google.adk.tools import FunctionTool
import urllib.request
import json

def get_weather(city: str) -> str:
    """Returns the weather for a given city."""
    # This is a mock function to demonstrate how tools work!
    # In the real world, you would call an external API here.
    if "london" in city.lower():
        return "It is rainy and 12°C in London."
    elif "tokyo" in city.lower():
        return "It is sunny and 22°C in Tokyo."
    else:
        return f"It is currently 15°C and partly cloudy in {city}."


def get_random_fact() -> str:
    """Fetches a real random fact from the internet. This is a LIVE API call!"""
    # This tool calls a REAL, free, no-auth API to show that tools are real code.
    try:
        url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            return f"🎲 Random fact: {data['text']}"
    except Exception as e:
        return f"Could not fetch a fact right now (requires internet). Error: {e}"


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant with access to tools.',
    instruction='''Answer user questions. You have two tools:
1. Use `get_weather` when users ask about weather in a specific city.
2. Use `get_random_fact` when users ask for a fun fact, trivia, or something interesting.
Always explain what you did after using a tool.''',
    tools=[FunctionTool(get_weather), FunctionTool(get_random_fact)]
)
