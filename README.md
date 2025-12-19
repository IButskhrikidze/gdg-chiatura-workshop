# Build AI the Google Way  
## GDG Chiatura Workshop

This repository contains a **hands-on, developer-focused workshop** on building AI systems using **Google’s AI ecosystem**, progressing from direct Gemini usage to full agent-based systems with memory.

The workshop is split into **three conceptual parts** and **five practical stages**, each mapped to a dedicated folder.

---

## Repository Structure

```
gdg-chiatura-workshop/
│
├── 01_gemini_sdk/        # Direct Gemini API usage (Gen AI SDK)
├── 02_tool_calling/      # Tool calling and manual agent loops
├── 03_rest_calls/        # Direct REST API usage (Developer API / Vertex AI)
├── adk_agent/            # Agent with ADK (Agent Development Kit) with Memory
│
├── README.md             # Main overview (this file)
├── README_PART1.md       # Part 1: History of AI & ML at Google
├── README_PART2.md       # Part 2: Tools, APIs, and best practices
├── README_PART3.md       # Part 3: Hands-on workshop guide
│
├── requirements.txt
├── .env                  # Local environment variables (not committed)
└── .gitignore
```

---

## How This Workshop Is Organized

### Conceptual Parts (Read First)

These files provide **context, principles, and guidance**.

---

### 📘 Part 1 — Brief History of AI & Machine Learning at Google  
**File:** `README_PART1.md`

Covers:
- How AI evolved inside Google
- Key breakthroughs (PageRank, Deep Learning, Transformers)
- Google’s long-term contributions to AI
- Why scale and systems matter

**Purpose:**  
Understand *why* Google builds AI the way it does.

---

### 📘 Part 2 — Tools, APIs, and Best Practices for Developers  
**File:** `README_PART2.md`

Covers:
- Google’s AI engineering philosophy
- Gemini, Vertex AI, and AI Studio
- Embeddings, retrieval, and RAG
- Agents, tools, and orchestration
- Security, governance, and cost awareness

**Purpose:**  
Learn the *mental model* behind Google-style AI systems.

---

### 📘 Part 3 — A Hands-On Workshop  
**File:** `README_PART3.md`

Covers:
- Practical implementation roadmap
- Concepts needed before writing code
- Agent loops, tools, and memory

**Purpose:**  
Prepare for implementation.

---

## Hands-On Workshop Stages (Code)

Each folder corresponds to a **practical step** in the workshop.

---

### 1️⃣ `01_gemini_sdk`
**Direct Gemini API usage**
- Basic text generation
- System prompts
- Structured output
- Streaming

➡ Learn how to call Gemini from Python.

---

### 2️⃣ `02_tool_calling`
**Tool calling & manual agent loop**
- Function/tool definitions
- Model requesting tools
- Executing tools in code
- Feeding results back to the model

➡ Understand how agents actually work.

---

### 3️⃣ `03_rest_calls`
**Direct REST API calls**
- Developer API
- Vertex AI endpoints
- No SDK abstractions

➡ See the foundation beneath the SDKs.

---

### 4️⃣ `adk_agent`
**Agent Development Kit (ADK)**
- Declarative agent definitions
- Tool registration
- Running agents via `adk run`
- Having persistent memory

➡ Build structured, production-style agents.

---

## Recommended Learning Path

1. Read `README_PART1.md`
2. Read `README_PART2.md`
3. Read `README_PART3.md`
4. Work through folders:
   - `01_gemini_sdk`
   - `02_tool_calling`
   - `03_rest_calls`
   - `adk_agent`

Skipping steps will reduce understanding.

---

## Who This Workshop Is For

- Software engineers
- Backend & platform engineers
- Cloud & DevOps engineers
- Technical leads
- Anyone who wants to build **production AI systems**, not demos

---

## Guiding Principle

> Building AI the Google way means treating AI as **infrastructure** —  
> engineered, observable, secure, and scalable.

---

## Disclaimer

This repository is for **educational purposes only**.  
It is not affiliated with or endorsed by Google.
