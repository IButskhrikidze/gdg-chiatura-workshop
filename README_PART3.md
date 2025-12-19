# Build AI the Google Way - Part 3  
## A Hands-On Workshop

This workshop is the **practical continuation** of the Google AI Ecosystem journey.

You will move:
- from **direct Gemini API calls**
- to **tool calling and agent loops**
- to **production-style agents using ADK**

The goal is not to build a demo chatbot, but to understand **how Google expects developers to build AI systems**.

---

## Workshop Goals

By the end of this workshop, you will be able to:

- Use **Gemini from Python** in multiple ways
- Understand **tool calling vs agents**
- Build a **full agent loop** (reason → act → observe → respond)
- Know when to use:
  - direct SDK calls
  - REST APIs
  - ADK
- Understand where **memory** fits in agent systems

---

## Prerequisites

- Python 3.10+
- Basic familiarity with APIs
- Gemini API key **or** GCP project with Vertex AI enabled

---

## Core Terms & Definitions

### Prompt
A **prompt** is the input sent to the model.

Example:
```
Summarize this document in 3 bullet points.
```

---

### System Prompt (System Instruction)
Defines the *role, behavior, and constraints* of the model.

Example:
```
You are a senior backend engineer. Be concise and accurate.
```

---

### Tool (Function)
A **tool** is a deterministic function written by developers.

Examples:
- `get_weather(city)`
- `search_documents(query)`
- `calculate(expression)`

---

### Tool Calling
The model decides to request a tool, your code executes it, and the result is sent back to the model.

---

### Agent
An **agent** is a system that reasons, uses tools, and produces a final answer.

---

### Agent Loop (Reason–Act–Observe)

```
User Input
   ↓
Model Reasoning
   ↓
Tool Call
   ↓
Tool Result
   ↓
Final Answer
```

---

### Memory
Memory allows an agent to persist context across turns.

---

## Workshop Structure

1. Direct Gen AI SDK  
2. Direct Gen AI SDK with tool calling  
3. Direct REST calls (Developer API or Vertex AI endpoints)  
4. Agent with ADK (Agent Development Kit) with Memory

---

## Final Thought

> Building AI the Google way means treating AI as **infrastructure**, not a feature.
