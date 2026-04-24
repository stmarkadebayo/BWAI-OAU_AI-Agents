# Building AI Agents with Vertex AI & Google ADK

Welcome to the **GDG OAU Data Science/ML Track** Buildathon repository!

This repository contains everything you need to go from a beginner to building complex, tool-using, multi-agent AI systems using Google's Agent Development Kit (ADK) and Vertex AI.

> **Requirements:** Python 3.10+ · Google Cloud account with credits · `gcloud` CLI

## 🚀 Getting Started

1. **Read the Curriculum:** Start by reading the [`CURRICULUM.md`](./CURRICULUM.md) file. This is the master guide for the workshop. It explains the core concepts, the "Agent Loop," and includes instructions on the mandatory **Credit Claiming Ceremony**.
2. **Setup your environment:**
   ```bash
   cd labs
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Configure Vertex AI:**
   Copy the example environment file and add your Google Cloud Project ID.
   ```bash
   cp .env.example .env
   ```
   *Make sure `GOOGLE_GENAI_USE_VERTEXAI=1` is present in your `.env` file to ensure we use your Vertex AI credits!*

> **🚨 Stuck?** See the [Troubleshooting Guide](./TROUBLESHOOTING.md) for solutions to common setup issues.

## 📂 Repository Structure

The `labs/` directory contains progressively more complex agent implementations:

### 🟢 Beginner
* **`01_beginner/01_foundation_agent`**: A simple chat agent showing the fundamental "Think/Act" loop.
* **`01_beginner/02_tools_agent`**: An agent empowered with tools — including a **real live API call**!

### 🟡 Advanced
* **`02_advanced/02a_stateful_agent`**: An agent with **memory** — it remembers facts about you across the conversation using session state.
* **`02_advanced/02b_guardrails_agent`**: An agent with **safety guardrails** — uses callbacks to block dangerous requests before they reach the LLM.
* **`02_advanced/03_multi_agent`**: A multi-agent orchestration showing a manager agent delegating tasks to a researcher and a writer.

### 🔴 Capstone & Deploy
* **`03_capstone/04_custom_agent_challenge`**: A "Bring Your Own Tool" sandbox challenge for participants to build their own agent team!
* **`04_deployment/DEPLOY.md`**: Guide for deploying your finished agents live to Google Cloud Run!

> **Note on Slides:** If you are presenting this workshop, simply open the `README.md` inside each of the lab folders. They are formatted with Mermaid diagrams to act as presentation slides!

Each subfolder contains its own `README.md` with specific details on what it teaches and how to run it.

## 🏃 Running and Testing the Agents

Instead of testing in a boring terminal, we will use the ADK's built-in **Web UI**. This spins up a local ChatGPT-style interface with an "Inspector" tab so you can see your agent's hidden thoughts!

Navigate into the `labs` directory, ensure your virtual environment is activated, and use the `adk web` command:

```bash
cd labs
adk web 01_beginner/01_foundation_agent
```
Then open **`http://localhost:8000`** in your browser.

## 🚀 Deploying to the Web
Ready to show the world? Open [`labs/04_deployment/DEPLOY.md`](./labs/04_deployment/DEPLOY.md) to learn how to instantly deploy your agent to a public URL using Google Cloud Run.

---
*Built for the GDG OAU Community.*
