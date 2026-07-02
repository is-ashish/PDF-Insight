🛡️ Module 1: AI Guardrails & Security
Learn how to implement security layers to shield applications from prompt injections, jailbreaks, and off-topic leaks.
 [03:03] — Introduction to LLM Security & Guardrails
 [11:43] — Architecture: How Guardrails Sit Between the User and the LLM
 [16:30] — Overview of Popular Guardrail Frameworks (NVIDIA NeMo, Guardrails AI, Meta Llama Firewall)
 [20:50] — Raw LLM Call vs. Guarded LLM Call Live Demonstration
 [24:07] — Deep Dive: Handling Off-Topic Queries
 [27:35] — Deep Dive: Defending Against Jailbreaks & Prompt Injections
 [31:15] — Deep Dive: Blocking Sensitive/Malicious Topics
 [35:37] — Deep Dive: Masking PII (Personal Identifiable Information)
📊 Module 2: LLM Evaluation Frameworks
Build rigorous benchmarking systems to measure retrieval-augmented generation (RAG) metrics like faithfulness and relevancy.
 [01:13:30] — Introduction to LLM App Evaluations (Theory & Analogies)
 [01:18:06] — Understanding "Goldens" (Evaluation Baseline Datasets)
 [01:41:20] — RAG Triad Concept & Automating Evaluation
 [01:49:54] — Utilizing LLM-as-a-Judge (SOTA Models vs. Budget Considerations)
 [01:52:55] — Deep Dive: Calculating Faithfulness (Detecting Hallucinations)
 [02:12:03] — Deep Dive: Calculating Answer Relevancy
 [02:18:02] — Deep Dive: Calculating Context Precision (Reranking & Chunk Ordering)
 [02:24:39] — Deep Dive: Calculating Context Recall
 [02:30:07] — Deep Dive: Calculating Answer Correctness (Factual + Semantic Weighting)
🧠 Module 3: Agentic Memory Techniques
Explore the evolution and implementation of short-term vs. long-term persistent memory slots within autonomous loops.
 [02:48:10] — Introduction to Short-Term & Long-Term Memory Lineages
 [03:00:57] — Technical Breakdown: Conversational Buffer Memory & Token Bloating
 [04:12:43] — Technical Breakdown: Sliding Window Memory (Turn Eviction Architecture)
 [04:14:00] — Technical Breakdown: Summary Memory & Abstractive/Hierarchical Summarization
 [04:16:03] — Technical Breakdown: Summary Buffer Memory
 [04:20:05] — Technical Breakdown: Token Buffer Memory (Hard vs. Bounded Evictions)
 [04:24:41] — Technical Breakdown: Vector Store Memory (Long-Term Vectorized Persistent Shuffling)
 [04:41:11] — Technical Breakdown: Entity Memory (Named Entity Recognition and CRM Lookup States)
 [04:50:04] — Memory Updation Engineering: Hot Path vs. Background Cold Path Update Loops
 [05:02:28] — Technical Breakdown: Episodic Memory (Time-Aware, Post-Session Synthetic Memory Bundles)
 [05:15:54] — Technical Breakdown: Semantic Memory (Distilling Reusable General Facts and Behavioral Traits)
 [05:20:14] — Technical Breakdown: Procedural Memory (Self-Improving Dynamic System Prompts)
 [05:25:46] — Technical Breakdown: Self-Reflection Memory (Verbal Post-Mortems for Execution Improvements)
 [05:33:13] — Deep Dive: Memory Routing Mechanisms (Intent-Driven Dynamic Memory Selection)
 [05:40:23] — Deep Dive: Forgetting and Decay Algorithms (Implementing Ebbinghaus Forgetting Curves & Half-Life Scores)
🚀 Module 4: AgentOps
Scale autonomous setups, observe complex multi-agent spans, and deploy workflows through production environments.
 [05:50:47] — Introduction to AgentOps (Tracing, Benchmarking, and Deployment Lifecycle)
 [05:55:11] — RAG Architecture Component Breakdown: Apache Airflow (Data Ingestion Pipeline)
 [05:57:31] — RAG Architecture Component Breakdown: PostGreSQL/Neon (Relational Storage metadata tracking)
 [05:58:33] — RAG Architecture Component Breakdown: OpenSearch (Vector Database and Management Dashboard)
 [06:06:08] — Live Demo: Trace Logging and Waterfalls using Pydantic Logfire & LangFuse
 [06:21:04] — Core Code Walkthrough: Guardrails, Model Fallbacks, and Factory Patterns
 [06:40:41] — RAG Retrieval Techniques: Reciprocal Rank Fusion (RRF) & BM25 Hybrid Matching
 [06:48:48] — Mapping Agent State Machines with LangGraph Node Flows
 [06:53:11] — Exposing Agent Architectures via the Model Context Protocol (MCP) Server Integration
 [07:06:51] — Orchestrating Autonomous Infrastructures over AWS EKS (Kubernetes Pod Cluster Setups)
 [07:14:19] — Deep Dive: Stress & Load Testing with Locust (Monitoring Autoscaling, HPA Spikes, and Thread Concurrency)