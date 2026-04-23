from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from google.adk.tools.agent_tool import AgentTool

def mock_web_search(query: str) -> str:
    """Simulates searching the internet for factual information."""
    print(f"[Tool Execution] Searching for: {query}")
    if "agent" in query.lower():
        return "AI Agents can reason, use tools, and make autonomous decisions."
    return "No specific data found. It might be a new topic."

# The Researcher sub-agent
researcher_agent = Agent(
    model='gemini-2.5-flash',
    name='researcher_agent',
    description='An expert researcher that can search the web for facts.',
    instruction='Your job is to search for facts using the mock_web_search tool. Provide detailed facts based on your search.',
    tools=[FunctionTool(mock_web_search)]
)

# The Writer sub-agent
writer_agent = Agent(
    model='gemini-2.5-flash',
    name='writer_agent',
    description='A talented writer that turns raw facts into engaging prose.',
    instruction='Your job is to take raw facts and write a compelling, concise summary paragraph. Do not search for information yourself.'
)

# The Root Orchestrator
root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='The lead orchestrator that delegates to other agents.',
    instruction='''You are the lead orchestrator. When asked a question:
1. Delegate research to the researcher_agent.
2. Delegate writing to the writer_agent using the research facts.
3. Return the final written piece to the user.
Do not answer the question directly. Always use your team.''',
    tools=[AgentTool(agent=researcher_agent), AgentTool(agent=writer_agent)]
)
