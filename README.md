# Agentic AI Foundations

Welcome to **Agentic AI Foundations**! This repository is dedicated to exploring, designing, and building foundational architectures, patterns, and applications for autonomous AI agents.

---

## 📌 Overview & Core Concepts

Agentic AI represents a paradigm shift from passive model interaction to proactive, goal-driven AI systems capable of planning, using tools, executing complex workflows, and collaborating with human users.

- **Agent Architectures**: Memory systems, planning modules, reflection loops, and decision-making mechanisms.
- **Tool Use & Integrations**: Interfacing with APIs, CLI execution, web navigation, and specialized toolkits.
- **Multi-Agent Systems**: Task delegation, multi-agent coordination, and peer-to-peer workflows.
- **Safety & Alignment**: Guardrails, human-in-the-loop (HITL) validation, and execution monitoring.

---

## 🤖 What is an AI Agent?

An **AI Agent** transforms a standalone language model into an autonomous problem solver capable of executing complex goals ([mylearn.oracle](https://mylearn.oracle.com/ou/course/oracle-agentic-ai-foundations-2026/163240/271870)):

$$\text{AI Agent} = \text{LLM} + \text{Tools} + \text{Loop} + \text{Reasoning Patterns}$$

- **LLM**: The "brain" that reasons and decides what to do.
- **Tools**: Functions, APIs, databases, or services the agent can call.
- **Loop**: Repeated cycle of *"think $\rightarrow$ act $\rightarrow$ observe $\rightarrow$ think again"* until the goal is met.
- **Reasoning Patterns**: Strategies like planning, reflection, and multi-step workflows that guide how the agent uses the loop.

---

### 🔄 The Agent Execution Loop

The core dynamic of an AI agent is its continuous execution loop:

![The Agent Execution Loop](assets/agent_execution_loop.png)

```
Perceive (Input/Observation) ──► Reason (Select Next Step) ──► Act (Call Tool/Respond) ──► Observe (Receive Result/Feedback) ──► (Repeat Loop)
```

---

### ⚡ Key Contrast: Chatbot vs. AI Agent

- **Chatbot**: $\text{Prompt} \longrightarrow \text{LLM} \longrightarrow \text{Single Answer}$
- **Agent**: $\text{Prompt} \longrightarrow \text{LLM} \longrightarrow \text{Choose Tool} \longrightarrow \text{Execute} \longrightarrow \text{Observe} \longrightarrow \text{LLM Again} \longrightarrow \text{More Tool Calls} \longrightarrow \text{Final Answer}$ ([mylearn.oracle](https://mylearn.oracle.com/ou/course/oracle-agentic-ai-foundations-2026/163240/271870))

#### Standalone LLM vs. (LLM-based) AI Agent

![LLM vs AI Agent Comparison](assets/llm_vs_ai_agent.png)

| Capability | Standalone LLM | AI Agent (LLM-based) |
| :--- | :--- | :--- |
| **Knowledge Access** | Training data + provided context (prompt); no built-in live access | Training + live tools (dynamic) |
| **Actions** | Generate text | Search, compute, call APIs, write code |
| **Memory** | None between calls | Working + persistent memory |
| **Planning** | Single-pass response | Multi-step planning & iteration |
| **Self-Correction** | Can do internal consistency checks; ext. verification requires tools or retrieval | Observes results, retries on error |
| **State** | No built-in persistent state (state is app-managed) | Maintains context across steps |

---

### 🚀 Why "Agentic" AI Matters

> *Moving from "AI that talks" to "AI that does."*

- **Automates Multi-Step Tasks**: Handles complex workflows autonomously instead of just answering questions.
- **Interacts with Real Systems**: Connects directly with databases, enterprise applications, and cloud services.
- **Enables Goal-Oriented Behavior**: Keeps working and iterating until a defined objective is fully achieved ([mylearn.oracle](https://mylearn.oracle.com/ou/course/oracle-agentic-ai-foundations-2026/163240/271870)).

---

## 🧩 AI Agent Core Components

An AI agent is built by combining an LLM with instructions, tools, memory or state, and an execution loop. These components enable it to understand a goal, select actions, use external systems, evaluate results, and produce a useful final response ([mylearn.oracle](https://mylearn.oracle.com/ou/course/oracle-agentic-ai-foundations-2026/163240/271870)).

![AI Agent Core Components Architecture](assets/ai_agent_core_components.png)

```
User Goal ──► LLM Reasoning ──► Tool Action ──► Observation ──► Next Decision / Final Response
```

The agent repeats this cycle until it has enough information to complete the task or reaches a stopping condition.

- **Input**: User request, system instructions, and available context.
- **Reasoning**: The LLM interprets the request and decides whether it can answer directly or needs an action.
- **Action**: The agent calls a tool or function.
- **Observation**: The tool result is returned to the agent.
- **Final Response**: The LLM converts the result into a clear user-facing answer.

---

### 1. Large Language Model (LLM) - The Reasoning Engine

The **LLM** is the agent's central reasoning engine.
- Understands natural-language instructions and user questions.
- Interprets current context and determines the next best action.
- Can generate a direct response, choose a tool, form tool arguments, or decide whether another step is required.
- *Knowledge boundaries*: Does not inherently possess live knowledge, private enterprise data access, or direct external system capabilities—these are unlocked via tools and retrieval components.

> **Important**: The LLM makes decisions based on system instructions, conversation context, tool definitions, and results from previous actions.

---

### 2. Instructions & System Prompts

Instructions define the agent's role, boundaries, style, and operational objectives. Clear instructions reduce ambiguity in the LLM's decisions and increase reliability:

- **Role**: e.g., *"You are an enterprise customer support assistant."*
- **Goal**: The targeted outcome the agent must achieve.
- **Scope**: Boundaries defining which requests the agent should handle.
- **Constraints**: Strict guardrails avoiding unauthorized data exposure or unapproved transactions.
- **Tool Guidance**: Specific criteria describing when and how tools should be called.
- **Response Format**: Output expectations (e.g., concise summary, JSON schema, step-by-step markdown report).
- **Escalation Rules**: Protocols for asking clarification or handing off tasks to human agents.

---

### 3. Tools & Tool Calling

Tools give an agent the ability to interact with the world beyond text generation ([mylearn.oracle](https://mylearn.oracle.com/ou/course/oracle-agentic-ai-foundations-2026/163240/271870)).

#### Common Tool Types
- **Database Queries**: Retrieving enterprise relational or vector data.
- **APIs**: Integrating weather, inventory, CRM, payment, calendar, or ticketing platforms.
- **Search & Retrieval**: Document search across enterprise knowledge bases (RAG).
- **Code Execution**: Sandboxed Python/Bash tools for data analysis and calculation.
- **File System Tools**: Reading, generating, or modifying local and cloud files.
- **Communication Tools**: Dispatching emails, Slack messages, or push notifications.

#### Tool Definition Elements
| Element | Purpose |
| :--- | :--- |
| **Tool Name** | Identifies the unique action (e.g., `get_customer_order`). |
| **Description** | Tells the LLM *when* and *why* the tool should be invoked. |
| **Input Schema** | Defines required and optional parameters (JSON Schema). |
| **Output** | Returns structured data or execution results back to the agent. |
| **Permissions** | Limits authorization and protects sensitive enterprise systems. |

#### Tool Calling Flow
The LLM does **not** execute the tool directly. The agent runtime receives the tool request from the LLM, executes the call securely against external services, feeds the observation back into context, and allows the LLM to decide the next step.

```
User: "Where is my order?" 
  ──► Agent recognizes order lookup needed 
  ──► LLM selects order_tracking tool 
  ──► Runtime passes Order ID to API 
  ──► Tool returns shipment status 
  ──► LLM summarizes status for User
```

---

### 4. Context, Memory, and Retrieval

An agent requires structured context to make coherent decisions across multi-turn interactions.

```mermaid
graph TD
    A["Context & Memory"] --> B["Short-Term Memory"]
    A --> C["Long-Term Memory"]
    A --> D["Knowledge & Retrieval (RAG)"]
    
    B --> B1["Session dialogue history"]
    B --> B2["Prior tool calls & results"]
    
    C --> C1["Persistent user preferences"]
    C --> C2["Cross-session facts & history"]
    
    D --> D1["Vector database search"]
    D --> D2["Enterprise document retrieval"]
```

- **Short-Term Memory**: Information retained during the active workflow/session (maintains dialogue continuity, tracks prior tool calls, prevents duplicate queries).
- **Long-Term Memory**: External persistence preserving user preferences and facts across sessions (requires governance, retention policies, and privacy controls).
- **Knowledge & Retrieval (RAG)**: Dynamically fetches relevant passages from enterprise knowledge bases, vector stores, or APIs to ground model answers with zero pre-training cost.

---

### 5. The Agent Loop & Stopping Conditions

The **Agent Loop** drives iterative execution:
1. Receive user goal.
2. Read system instructions & context.
3. Decide whether to answer directly or call a tool.
4. Generate tool inputs if required.
5. Runtime executes tool & captures observation.
6. Evaluate if goal is accomplished.
7. Repeat loop or emit final response.

#### Essential Stopping Conditions:
- Goal successfully completed.
- Sufficient information gathered.
- Maximum step/iteration limit reached.
- Unrecoverable tool failure encountered.
- Human review or clarification required.
- Safety policy guardrail triggered.

---

### 6. Planning, Reasoning & State Management

- **Planning & Reasoning**: Deconstructs high-level objectives into sequential micro-steps (e.g., *"Prepare weekly sales report"* $\rightarrow$ *query DB $\rightarrow$ calculate totals $\rightarrow$ generate report $\rightarrow$ lookup manager email $\rightarrow$ confirm sending $\rightarrow$ send email*).
- **State Management**: Maintains a structured record of user intent, execution steps, tool call history, intermediate outputs, errors, retries, and approval flags. Essential for long-running and multi-agent workflows.

---

### 7. Safety Guardrails & Human-in-the-Loop

Guardrails control what an agent can read, write, and execute across multiple checkpoints:

- **Input Validation**: Filters out malformed, malicious, or out-of-scope prompts (jailbreak prevention).
- **Authorization & RBAC**: Verifies user access rights before executing sensitive tool calls.
- **Action Restrictions**: Restricts destructive operations (e.g., database deletion, unapproved funds transfer).
- **Human Approval (HITL)**: Requires human confirmation before high-impact consequential actions.
- **Output Filtering**: Prevents PII leakage or harmful text generation.
- **Rate Limits & Auditing**: Monitors timeouts, tool call quotas, and execution logs.

---

### 🛡️ Real-World Example: Customer Support Agent

Below is an enterprise workflow showing how core components cooperate to process a customer request: *"Can you cancel my order 12345?"*

![Customer Support Agent Workflow](assets/support_agent_workflow.png)

| Component | Role & Function in Workflow |
| :--- | :--- |
| **Instructions** | Defines cancellation eligibility policy and human approval rules. |
| **LLM** | Interprets intent, checks required order parameters, and selects actions. |
| **Context** | Passes customer authentication token and session history. |
| **Tool** | Queries order DB to inspect order status for ID `12345`. |
| **Guardrail** | Verifies customer ownership of order `12345` and confirms cancellation window. |
| **Loop** | Retrieves details, evaluates eligibility, and determines if approval is needed. |
| **Human Confirmation** | Prompts support lead/user for high-value order cancellation confirmation. |
| **Final Response** | Generates clear confirmation message and refund processing status to user. |

---

### 🔑 Key Takeaways

1. An AI agent is a unified system combining an **LLM**, **Instructions**, **Tools**, **Memory**, an **Execution Loop**, and **Guardrails**.
2. The **LLM** makes decisions; **Tools** execute actions and fetch real-world data.
3. **Context and Memory** keep interactions consistent, personal, and relevant.
4. The **Agent Loop** empowers autonomous multi-step problem solving.
5. **State Management** makes long-running workflows recoverable and auditable.
6. **Guardrails & Human-in-the-Loop** controls are mandatory for secure enterprise deployment.

---

## 🎓 Course Curriculum: Oracle Agentic AI Foundations

This repository aligns with and builds upon concepts from the [Oracle Agentic AI Foundations](https://mylearn.oracle.com/ou/course/oracle-agentic-ai-foundations-2026/163240/273946) course.

### 🎯 What You’ll Learn
The course covers AI-agent architecture, LLMs, tools, execution loops, reasoning patterns, safety guardrails, LangChain, the Model Context Protocol (MCP), and the OpenAI Responses API and Agents SDK. It then applies these topics to OCI Enterprise AI and Oracle AI Database ([mylearn.oracle](https://mylearn.oracle.com/ou/course/oracle-agentic-ai-foundations-2026/163240/273946)).

By the end, you should be able to design agents with LangChain and the OpenAI agent stack, incorporate MCP into workflows, build agents on OCI Enterprise AI Platform, and use Oracle AI Database capabilities for agentic solutions ([mylearn.oracle](https://mylearn.oracle.com/ou/course/oracle-agentic-ai-foundations-2026/163240/273946)).

---

### 📚 Course Structure

1. **Introduction to AI Agents**: Agent definitions, components, reasoning, a first-agent walkthrough, and guardrails ([mylearn.oracle](https://mylearn.oracle.com/ou/course/oracle-agentic-ai-foundations-2026/163240/273946)).
2. **LangChain for AI Agents**: LangChain basics, building an agent, demos, and internal agent behavior ([mylearn.oracle](https://mylearn.oracle.com/ou/course/oracle-agentic-ai-foundations-2026/163240/273946)).
3. **Introduction to MCP**: MCP concepts and components, connecting an MCP server to an agent, and practical server examples ([mylearn.oracle](https://mylearn.oracle.com/ou/course/oracle-agentic-ai-foundations-2026/163240/273946)).
4. **OpenAI Responses API and Agents SDK**: OpenAI agent stack, APIs, SDKs, tool/function calling, multi-agent handoffs, safety, and a customer-support-agent demo ([mylearn.oracle](https://mylearn.oracle.com/ou/course/oracle-agentic-ai-foundations-2026/163240/273946)).
5. **Agentic AI for OCI Enterprise AI**: Agent lifecycle and runtime, OCI Enterprise AI Platform and Agents, deployment, and scaling ([mylearn.oracle](https://mylearn.oracle.com/ou/course/oracle-agentic-ai-foundations-2026/163240/273946)).
6. **Agentic AI for Oracle AI Database**: Vector search, Private Agent Factory, and an Autonomous AI Database MCP server ([mylearn.oracle](https://mylearn.oracle.com/ou/course/oracle-agentic-ai-foundations-2026/163240/273946)).

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.10+ / Node.js 18+
- API Credentials for target LLM providers

### Setup

```bash
# Clone the repository
git clone https://github.com/Tarunkommi/Agentic-AI-Foundations.git

# Navigate into the project directory
cd Agentic-AI-Foundations
```

---

## 📝 License

This project is open-source under the [MIT License](LICENSE).

---

## 🧠 How Large Language Models (LLMs) Are Built and Deployed

Understanding the foundation of Agentic AI requires understanding how Large Language Models (LLMs) are created, trained, and operated. 

An LLM is **not** a database that inherently understands facts; it is a statistical system trained to predict the most likely next token based on patterns learned from enormous datasets.

![LLM Lifecycle Architecture](assets/llm_lifecycle_architecture.png)

```
Data Collection ──► Cleaning & Filtering ──► Tokenization ──► Vector Embeddings ──► Transformer Neural Network ──► Next-Token Training ──► Supervised Fine-Tuning (SFT) ──► RLHF Alignment ──► Real-Time Inference
```

---

### 1. The Four Stages of LLM Development

The creation of a modern LLM can be understood through the analogy of raising and educating a child:

| Stage | Human Analogy | LLM Term | What It Achieves |
| :--- | :--- | :--- | :--- |
| **1** | Child absorbs books, media, and conversations | **Pre-training** | Learns broad language structure, coding patterns, and world knowledge. |
| **2** | Teacher demonstrates proper Q&A responses | **Supervised Fine-Tuning (SFT)** | Learns instruction-following, structured response formats, and assistant style. |
| **3** | Society gives feedback on behavior & safety | **RLHF (Human Feedback Alignment)** | Learns preferred, safer, polite, and helpful outputs. |
| **4** | Child answers a new question in real time | **Inference** | Generates responses token-by-token for end users in real time. |

Products such as **ChatGPT**, **Claude**, and **Gemini** expose these underlying trained models through user-facing chat interfaces and APIs.

---

### 2. Pre-training Data & Scale

Pre-training exposes the network to vast volumes of textual and source code data.

- **Data Sources**: Common Crawl web data, GitHub repositories, Wikipedia, digital books, academic papers, Reddit, forums, and Stack Overflow.
- **Scale of Data**:
  - **GPT-3**: ~300 Billion tokens
  - **Llama 3**: ~15 Trillion tokens
- **What is a Token?**: A token is a word fragment or character sequence. This scale allows models to process far more text during training than any human could read in multiple lifetimes.

---

### 3. Data Cleaning & The Filtering Funnel

Raw internet data contains duplicate content, broken code, spam, toxic content, and sensitive personal information. Data quality directly governs model safety and capability ("Garbage in, Garbage out").

```mermaid
flowchart TD
    A["Raw Internet Data (~100 Petabytes)"] --> B["Deduplication (Exact & Near-Duplicates)"]
    B --> C["Language Filtering"]
    C --> D["Quality Scoring (Credibility & Utility)"]
    D --> E["Toxicity Filtering"]
    E --> F["PII Removal (Personal Data Redaction)"]
    F --> G["Curated Pre-training Corpus (5 - 10 Petabytes)"]
```

*Example*: Data preprocessing funnels often shrink raw web dumps from **100 Petabytes** down to **5–10 Petabytes** of high-quality training text.

---

### 4. Tokens and Tokenization

Computers cannot process raw characters directly. A **tokenizer** parses text into smaller units (words, word fragments, or punctuation) and maps them to integer numerical IDs.

```mermaid
graph LR
    A["'The cat sat on the mat'"] --> B["Tokenizer (e.g., BPE)"]
    B --> C["Token Array: ['The', ' cat', ' sat', ' on', ' the', ' mat']"]
    C --> D["Token IDs: [464, 3797, 3318, 319, 262, 2603]"]
```

- **Byte Pair Encoding (BPE)**: A common algorithm that iteratively merges frequent character pairs to create an efficient vocabulary of subword units.
- **Language Efficiency**: Tokenization efficiency varies by language. For instance, a phrase in Telugu may tokenize into significantly more tokens than an equivalent English phrase, directly impacting context window usage and API execution costs.

---

### 5. Vector Embeddings

Numerical token IDs do not intrinsically convey semantic meaning. An **Embedding Layer** transforms each token ID into a high-dimensional vector of real numbers (e.g., 1,536 dimensions).

$$ \text{Text} \longrightarrow \text{Tokens} \longrightarrow \text{Token IDs} \longrightarrow \text{Embedding Vectors} $$

In this high-dimensional vector space, semantically related concepts reside close to one another:
- $\text{Vector}(\text{"king"}) \approx \text{Vector}(\text{"queen"})$
- $\text{Vector}(\text{"apple"}) \approx \text{Vector}(\text{"banana"})$

Embeddings make natural language mathematically operable for neural networks.

---

### 6. Transformer Neural Networks & Attention

Modern LLMs rely on the **Transformer** architecture introduced in Google's 2017 landmark paper, *"Attention Is All You Need"*. Transformers superseded older architectures like RNNs and LSTMs by eliminating sequential processing bottlenecks and enabling massive parallel training across long contexts.

```mermaid
flowchart LR
    SubGraph1["Input Embeddings"] --> PE["Positional Encodings"]
    PE --> MHA["Multi-Head Self-Attention"]
    MHA --> FF["Feed-Forward Layers"]
    FF --> Out["Output Logits / Probabilities"]
```

#### Core Components:
1. **Positional Encodings**: Inject sequence order information so the model differentiates word meanings based on placement (e.g., *"river bank"* vs. *"went to the bank"*).
2. **Self-Attention Mechanism**: Computes contextual weights between all pairs of tokens in a sequence.
   - *Example*: In *"The cat sat on the mat because it was tired"*, self-attention calculates that **"it"** refers to **"cat"**.

---

### 7. The Training Loop

The fundamental pre-training objective is **Next-Token Prediction**. Given an input sequence, the model outputs a probability distribution over its vocabulary for what token comes next.

```mermaid
graph TD
    A["Input Context Tokens"] --> B["Transformer Forward Pass"]
    B --> C["Predicted Next-Token Probabilities"]
    C --> D["Calculate Error (Cross-Entropy Loss vs Target)"]
    D --> E["Backpropagation & Weight Updates (Gradient Descent)"]
    E --> A
```

The network compresses complex statistical, grammatical, and factual relationships into its billions of parameter weights rather than storing a traditional explicit lookup database.

---

### 8. Compute Infrastructure & Training Costs

Training modern frontier models requires vast computing clusters running highly parallel operations:

- **Infrastructure**: Clusters containing tens of thousands of specialized GPUs (e.g., NVIDIA H100s/A100s).
- **Cost Allocation**: The majority of reported multi-million dollar model development costs (~$100 Million) is concentrated in the **Pre-training** phase.
- **Scale Illustration**: Running ~25,000 GPUs continuously over ~6 months incurs approximately $80 Million+ in pure hardware, energy, and facility expenses.

---

### 9. Supervised Fine-Tuning (SFT)

A raw pre-trained base model excels at continuing text, but may not act as a helpful conversational assistant (e.g., prompted with a question, it might append more questions instead of answering).

**Supervised Fine-Tuning (SFT)** uses curated dataset pairs of human-authored prompts and ideal responses to teach the model:
- Direct instruction following
- Conversational persona and tone
- Structured output formatting (JSON, Markdown, code blocks)
- Explanatory techniques (e.g., *"Explain like I'm 10"*)

---

### 10. RLHF & Safety Alignment

**Reinforcement Learning from Human Feedback (RLHF)** further aligns the model with human preferences and safety standards.

1. **Human Preference Ranking**: Annotators rate multiple candidate model outputs.
2. **Reward Model Training**: A separate model learns to score responses based on human preferences.
3. **Policy Optimization (PPO/DPO)**: The base LLM is fine-tuned to maximize scores from the reward model while maintaining factual integrity.
4. **Safety Refusals**: Rules and guardrails train the system to decline dangerous, illicit, or harmful requests gracefully.

---

### 11. Real-Time Inference

Inference occurs when an end user submits a prompt to an application or API.

```
Prompt Input ──► Context Encoding ──► Probability Distribution Calculation ──► Token Sampling ──► Append Token ──► Repeat Loop
```

- **Autoregressive Generation**: The model predicts and emits one token at a time, appending each newly generated token back into its context window for the next iteration. This creates the streaming text effect in user interfaces.
- **API Economics**: Computational load scales with both input context length and output generation length, which is why API providers bill separately for **Input Tokens** and **Output Tokens**.

---

### 12. Model Limitations & Mental Model

#### Key Limitations:
- **Hallucinations**: Generates statistically plausible text that may not be factually correct.
- **Knowledge Cutoff**: Information is static up to the date data collection ended.
- **Language Imbalance**: Models perform best in high-resource languages (e.g., English) compared to low-resource languages.
- **Sensitivity & Non-Determinism**: Minor prompt variations or sampling parameters (temperature, top-p) lead to different responses.

#### Practical Mental Model:
Think of an LLM as a high-dimensional probability engine estimating:

$$ P(\text{Next Token} \mid \text{Previous Tokens}) $$

It translates pre-training pattern recognition, refined through SFT and RLHF alignment, into fluent generation—balancing immense capabilities in reasoning and coding with inherent limitations in static fact recall.

---


