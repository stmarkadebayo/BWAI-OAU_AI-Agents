# 1️⃣ The Foundation Agent

Welcome to the ground floor. Before we can give an agent tools or a team, we need to understand what an agent actually is.

---

## 🧠 LLMs vs. Agents
*   **LLM (Model)**: A text-prediction engine. You give it a prompt, it returns the most statistically likely completion.
*   **Agent**: A system that uses an LLM as its *reasoning engine*. It perceives its environment, makes decisions, and takes autonomous actions.

## 🔁 The Core Agent Loop
Under the hood, almost every agent framework (LangChain, ADK, AutoGPT) runs a variation of this fundamental loop:

```mermaid
graph TD
    User([User Input]) --> Gateway[Input Processor]
    Gateway --> LLM{LLM Core Engine}
    
    subgraph Cognitive Architecture
        LLM -->|Analyze Intent| Context[Context Retrieval]
        Context --> LLM
        LLM -->|Formulate Plan| Plan[Action Planner]
        Plan --> Decision{Need External Data?}
    end
    
    Decision -->|No| Gen[Generate Final Response]
    Decision -->|Yes| Select[Select Appropriate Tool]
    Select --> Exec[Execute Tool via API/Function]
    Exec --> Obs[Observe Result]
    Obs --> LLM
    
    Gen --> Output([Final Output])
    
    classDef core fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef internal fill:#fff3e0,stroke:#e65100,stroke-width:2px;
    class LLM core;
    class Context,Plan internal;
```

## 💻 In This Lab
We are building a barebones agent. It has no tools yet, so it will always choose "No" in the flowchart above. 

We are defining:
1. The **Model** (`gemini-2.5-flash`)
2. The **Persona / Instruction** ("You are a helpful assistant...")

### 🚀 How to Run (Interactive UI)
Instead of a boring terminal, we will use the ADK's built-in Web Server to get a ChatGPT-like interface!

From the `labs` directory, run:
```bash
adk web 01_beginner/01_foundation_agent
```
Then open **`http://localhost:8000`** in your browser.
