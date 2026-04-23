from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from google.adk.tools.agent_tool import AgentTool

# ==============================================================================
# STEP 1: Build a Custom Python Tool
# ==============================================================================
# TODO: Rename this function and make it do something interesting!
# Examples: 
# - fetch_crypto_price(ticker: str)
# - check_campus_shuttle(route: str)
# - calculate_gpa(grades: str)

def my_custom_tool(input_data: str) -> str:
    """A highly descriptive docstring explaining exactly what this tool does."""
    print(f"[Executing Custom Tool] Input received: {input_data}")
    # Write your logic here
    return f"Processed data based on {input_data}"


# ==============================================================================
# STEP 2: Create an Expert Sub-Agent
# ==============================================================================
# TODO: Create an agent that specializes in using the tool you just built.

expert_agent = Agent(
    model='gemini-2.5-flash',
    name='expert_agent',
    description='Describe what kind of expert this agent is.',
    instruction='Give this agent a strict persona and tell it to use my_custom_tool.',
    tools=[FunctionTool(my_custom_tool)]
)

# ==============================================================================
# STEP 3: Connect it to the Root Agent (The Manager)
# ==============================================================================
# TODO: Add your `expert_agent` to the manager's tools using `AgentTool(agent=expert_agent)`.
# TODO: Update the manager's instruction so it knows when to delegate to your expert.

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='The Manager of the AI team.',
    instruction='''You are the CEO of a digital agency. 
When users ask you for help, delegate tasks to your specialized team members.
Do not answer complex questions yourself.''',
    tools=[
        # Add AgentTool(agent=expert_agent) here!
    ]
)
