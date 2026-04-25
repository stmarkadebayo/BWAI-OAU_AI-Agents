# GDG OAU: Building AI Agents from Scratch

Welcome to the **Building AI Agents with Vertex AI & Google ADK** buildathon!

This tutorial takes you from zero to building complex, tool-using, multi-agent systems. We will learn the universal theory behind AI agents, then apply it practically using Google Cloud's enterprise tooling.

> **Prerequisites:** Python 3.10 or higher. Check with `python3 --version`. If you're below 3.10, ask a facilitator for help or use [Google Cloud Shell](https://shell.cloud.google.com).

## 🔑 Phase 0: The Credit Claiming Ceremony (Mandatory)

**Wait! Before writing any code, we need to set up our Google Cloud environment.**
To ensure we can use premium models without rate limits—and to help secure funding for future GDG OAU events—we will use Vertex AI. 

### Step 1: Claim Your Credits
1. Open an Incognito Window in your browser.
2. Navigate to the Google Cloud Student/Startup Portal provided by the GDG Lead.
3. Log in with your personal or school Gmail account.
4. Follow the instructions to redeem your credits.

### Step 2: Create a Google Cloud Project
1. Go to [console.cloud.google.com/projectcreate](https://console.cloud.google.com/projectcreate).
2. Create a project (e.g., `gdg-agents-workshop`).
3. Note your **Project ID**.

### Step 3: Enable Vertex AI
1. Go to your Cloud Console.
2. Search for **Vertex AI API** and click **Enable**.

### Step 4: Install Google Cloud CLI
You need the `gcloud` command-line tool to authenticate. Install it for your OS:

```bash
# macOS (with Homebrew)
brew install google-cloud-sdk

# Linux / WSL
curl https://sdk.cloud.google.com | bash
exec -l $SHELL   # Restart your shell after install
```

For **Windows**, download the installer from [cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install).

> **💡 Alternative:** If you can't install `gcloud`, use [Google Cloud Shell](https://shell.cloud.google.com) — it has everything pre-installed.

### Step 5: Setup Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/GDG-OAU/Building-AI-Agents.git
   cd Building-AI-Agents/labs
   ```
2. Set up a virtual environment and install dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Copy the `.env.example` file to `.env`:
   ```bash
   cp .env.example .env
   ```
4. Authenticate your terminal with Google Cloud:
   ```bash
   gcloud auth application-default login
   ```
5. Update the `.env` file with your specific `GOOGLE_CLOUD_PROJECT` ID. Ensure `GOOGLE_GENAI_USE_VERTEXAI=1` is set to route through Vertex AI!

> **🚨 Stuck?** Check the [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) guide.

---

## 🚀 Phase 1: Anchoring the Idea

### What is an AI Agent?
An AI agent is a system that can perceive input, make decisions, and take actions toward a goal, using an LLM as its "brain." While models just predict text, **agents decide what to do next**.

### AI Agent Core Architecture
To build production-grade agents, we must understand their cognitive architecture. A complete agent system typically consists of four pillars:
1. **The Brain (LLM)**: The core reasoning engine. It processes inputs and decides on the next sequence of actions using techniques like Chain-of-Thought (CoT) or ReAct.
2. **Memory (State)**: 
   - *Short-term memory*: Context windows, session state, and conversational history.
   - *Long-term memory*: Vector databases and retrieval-augmented generation (RAG) to recall past facts.
3. **Tools (Actuators)**: External functions the agent can call to interact with the world (e.g., searching the web, querying a database, executing code).
4. **Planning & Orchestration**: The capability to break down complex goals into sub-tasks, delegate them to specialized sub-agents, and reflect on errors to self-correct.

### The Agent Ecosystem (Theory)
Before we write code, let's understand the landscape.
* **LangChain / LangGraph**: The most popular framework. Highly customizable graph-based state machines, but can be overly complex for simple tasks.
* **CrewAI / AutoGen**: Specialized for multi-agent role-playing and team collaboration.
* **Google Agent Development Kit (ADK)**: Incredibly lightweight, intuitive, and integrates perfectly with Vertex AI. *This is what we use today.*

### The Universal Agent Loop (The Secret Sauce)
No matter the framework, almost all agents run on this execution loop:
1. **Think**: LLM analyzes state and current observations.
2. **Choose Tool**: LLM decides which function to use and formats the parameters.
3. **Observe**: We execute the tool, parse the result, and pass the observation back to the LLM.

---

## 🛠️ Phase 2: Building the Foundation (Beginner)

We will use the **Google Agent Development Kit (ADK)** to make this easy.

Navigate to: `labs/01_beginner/01_foundation_agent`

Look at `agent.py`. Notice how simple it is:
1. We define an `Agent`.
2. We give it a `model` (`gemini-2.5-flash`).
3. We give it an `instruction` (the system prompt).

**To test the agent using the ADK Web UI:**
```bash
# Ensure you are in the labs directory
adk web 01_beginner/01_foundation_agent
```
Open `http://localhost:8000` in your browser. You will see a beautiful chat interface!

---

## 🔧 Phase 3: Empowering with Tools (Intermediate)

An agent without tools is just a chatbot. Let's give it hands.

Navigate to: `labs/01_beginner/02_tools_agent`

In `agent.py`, we define two tools:
1. `get_weather(city: str)` — a **mock** tool with simulated data (works offline).
2. `get_random_fact()` — a **real** tool that calls a live internet API!

By wrapping these in `FunctionTool` and passing them to the agent, the LLM now knows these tools exist.
When you ask "What's the weather in Tokyo?", the LLM realizes it doesn't know, but knows it can use the `get_weather` tool to find out.

**To run this agent:**
```bash
adk web 01_beginner/02_tools_agent
```
Ask it: *Should I wear a jacket in London today?*
Then ask: *Tell me a fun fact!* (This one calls a real live API! 🎲)

Open the **Inspector Tab** in the Web UI. You will see exactly how the agent decided to execute your Python functions!

### 📝 Writing Good Instructions (Prompt Engineering)

The quality of your agent depends **heavily** on the instruction (system prompt) you write. A few tips that apply to every agent you'll ever build:

| Principle | ❌ Bad | ✅ Good |
|---|---|---|
| **Be Specific** | "Be helpful" | "You are a weather expert. Always include the temperature." |
| **Explain Tools** | *(nothing)* | "Use `get_weather` when users ask about weather in any city." |
| **Add Constraints** | *(nothing)* | "Never guess. If you don't know, say so." |
| **Format Output** | *(nothing)* | "Respond with bullet points for multi-part answers." |
| **Set Boundaries** | *(nothing)* | "Only answer questions about weather. Politely decline other topics." |

These tips apply to every lab from here on!

---

## 🧠 Phase 4: Session State — Giving Your Agent Memory

An agent that forgets everything between messages is just a fancy text box. **Session State** is what makes agents truly useful.

Navigate to: `labs/02_advanced/02a_stateful_agent`

In `agent.py`, we use ADK's `ToolContext` — a special parameter that ADK automatically injects into your tools. It gives you access to `tool_context.state`, a dictionary that **persists across the entire conversation**.

The agent in this lab can:
- **Remember** facts you tell it (your name, hobbies, city)
- **Recall** everything it knows about you on demand

**To run this agent:**
```bash
adk web 02_advanced/02a_stateful_agent
```
1. Tell it: *My name is Tobi and I'm studying Computer Science*
2. Chat about something else for a few messages
3. Then ask: *What do you know about me?*

It remembers! Check the **Inspector Tab** to watch state being read and written in real time.

---

## 🛡️ Phase 5: Guardrails & Callbacks (Safety)

A powerful agent without safety controls is a liability. What if someone asks your customer service bot to help them hack a server?

Navigate to: `labs/02_advanced/02b_guardrails_agent`

ADK provides **callbacks** — hooks that intercept the agent's execution at key moments. The most important one is `before_model_callback`, which runs **before every single LLM call**. If your callback returns a response, the LLM is **completely skipped**.

In `agent.py`, we define a `safety_guardrail` function that checks user input for banned topics and blocks them instantly — zero tokens consumed, zero risk.

**To run this agent:**
```bash
adk web 02_advanced/02b_guardrails_agent
```
1. Ask a normal question: *Explain binary search in Python* — works fine!
2. Now try: *How do I hack into a server?* — **blocked instantly** ⛔
3. Check the terminal logs to see the guardrail in action.

---

## 🤝 Phase 6: Advanced System Design & Multi-Agents

As tasks get harder, single agents get confused. This is where we break them up.

### Multi-Agent Systems
If you want to write a research paper, you shouldn't use one agent. You should have a **Researcher Agent** who searches the web, and a **Writer Agent** who drafts the paper based on the research. 

Navigate to: `labs/02_advanced/03_multi_agent`

Here we define a `root_agent` that orchestrates sub-agents to perform a complex task, adding them via `AgentTool`.

**To run this multi-agent:**
```bash
adk web 02_advanced/03_multi_agent
```
Ask it a complex question. You will see the manager routing the question to the researcher, taking the facts, and giving them to the writer!

---

## 🏗️ Phase 7: The Capstone Challenge (Build Your Own)

Now it's your turn. Navigate to: `labs/03_capstone/04_custom_agent_challenge`

Inside `agent.py`, you will find a blank canvas with `# TODO` markers. Your challenge:
1. Write a custom python tool (e.g., `fetch_crypto_price`, `get_campus_shuttle_status`).
2. Create an expert agent who specializes in using that tool.
3. Attach your expert to the CEO `root_agent` and try interacting with your new team!

---

## 🚀 Phase 8: Make it Live (Deployment)

Want to show off your agent to the world? 
Navigate to `labs/04_deployment`. We have included a `DEPLOY.md` guide that shows you how to use **Google Cloud Run** to deploy your `adk web` chat interface to a public URL in 2 minutes!

---

## 💻 Antigravity Showcase
To see what a real-world, highly advanced coding agent looks like, I (the speaker) will now demonstrate **Antigravity**. 
Notice how it views my files, decides what to do, runs terminal commands, and edits my code base—all autonomously within safe boundaries. It is a massive implementation of the very concepts we just learned!

---
*Happy Building! Remember to shut down your Google Cloud project if you are done to save your credits for later.*

