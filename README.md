 whatsapp-ollama-tool-agent
AMIRA — AI Receptionist for Interior DESIGNER AND ARCHITECTURE
AMIRA operates as a multi-turn, state-aware AI Automation Agent designed for premium interior design studios. Instead of basic linear keyword matching, it utilizes a reactive cognitive loop driven by localized Large Language Models (LLMs) and structured Python functional bindings over the Meta Graph API (v20.0).

 🪐 Deep Architecture & End-to-End Workflow

1. Webhook Ingress: Live customer message packets are captured asynchronously via Flask hooks.
2. Immediate 200 OK Handshake: The server dispatches an immediate response to Meta within milliseconds using background threading (`threading.Thread`), completely preventing message retry loops.
3. Context Synchronization: The user identity is checked against MongoDB to fetch historical context states, pulling data logs dynamically.
4. Multi-Turn Tool Calling Loop: The LLM parses user intents alongside explicit functional schemas. If the task requires execution, it suspends text generation to call localized tools, feeds the outputs back into its context, and reframes the final human-centric response.

 🛠️ Core Functional Capabilities (Tool Integrations)

1. Whitelisted YouTube Automation Tool
2. Targeted Activation:** For specific whitelisted phone numbers, the agent activates a specialized `yt-dlp` flat-extraction pipeline.
Semantic Search Delivery:** Upon receiving a specific query phrase, it instantly queries and extracts the top 3 matching YouTube videos—complete with titles and exact URLs—and dispatches them as an integrated list directly to the user's WhatsApp interface.

 2. Asynchronous Consultation & Instant Owner Alerts
   Client Handshake: When an appointment intent is classified, the agent processes dates and times safely, alerting the user that the slot is being secured.
  Owner Notification Bridge:   Instantly triggers a distinct background transaction via Meta's endpoint to dispatch a structured **Consultation Alert** directly to the business owner's phone for immediate operational tracking.

    3. High-Fidelity Media Showcase Engine
     Visual Portfolios & Walkthroughs: When clients request project portfolios, architectural concepts, or design layouts, the model triggers specialized data retrieval methods.
  CDN-Backed Dispatch:  Delivers verified image nodes and cinematic walkthrough video schemas directly to the client's WhatsApp interface.

 4. State Management & Dynamic MongoDB Storage
   Legacy Session Rehydration: On every incoming token hit, the backend runs queries on MongoDB collections to stream previous chat history UPTO 12 LAST MESSAGES TO AND FROM THE USER, placing them sequentially (`.insert(1, ...)` logic) to prevent context inversion.
Persistent Auditing: Parallel threads dump every incoming and outgoing exchange safely into document logs without intercepting the main chat stream.

🖥️ Local Infrastructure Prerequisites

Since this entire framework computes model inferences locally without relying on external paid LLM wrappers, **Ollama must be installed and actively running on your host machine.

1. Ensure Ollama is broadcasting on port `11434`.
2. Pull the target model instance locally before launching the server:
