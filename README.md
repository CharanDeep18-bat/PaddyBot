# 🌾 PaddyBot

### A Retrieval-Augmented Generation Assistant for Paddy (Rice) Cultivation

PaddyBot is an AI-powered assistant that aims to provide
knowledge-grounded responses to questions pertaining to paddy (rice)
cultivation.

The system leverages Retrieval-Augmented Generation (RAG) to retrieve
relevant information from a curated corpus of agricultural knowledge,

and employs a locally run Large Language Model (LLM) for response

generation.
The application features a Streamlit-based conversational interface as well
as command-line support.
---
## 📌 Overview
Paddy (rice) farmers and agricultural practitioners often require
information pertaining to a wide variety of topics related to rice
cultivation such as: diseases, fertilizers, pests, irrigation and general
cultivation practices.
PaddyBot aims to address this pain point by combining:
- 📚 Agricultural knowledge documents
- 🔎 Semantic document retrieval
- 🧠 Transformer-based text embeddings
- 🗄️ FAISS vector similarity search
- 🤖 Local Large Language Model inference
- 💬 Conversational interaction
- 📄 Source and page-level references
PaddyBot replaces the standard practice of a language model leveraging
its in-context knowledge with the retrieval of the most relevant
information from the agricultural knowledge base.
---
## ✨ Features
### 🌾 Paddy Cultivation Assistance
The PaddyBot application and API provides question-answering and
general conversational capabilities around paddy cultivation, including:
- Paddy diseases
- Disease symptoms and management
- Pests, fertilizers and nutrient management
- Irrigation, cultivation and harvest-related practices
- General agricultural practices
### 🔎 Retrieval-Augmented Generation
The application retrieves relevant chunks of text from the
agricultural knowledge base to provide context to the question being
asked.
### 🧠 Semantic Search
Documents are converted to vector representations through the use of
a Sentence-Transformers embedding model.
The current implementation makes use of the following model:
`sentence-transformers/all-MiniLM-L6-v2`
### 🗄️ FAISS Vector Database
The FAISS library provides vector similarity search capabilities for
the embedded knowledge base chunks.
### 🤖 Local LLM
The Ollama API provides locally run Large Language Models for the
inference component of the PaddyBot application.
This allows the generation component to be decoupled from a cloud-hosted
LLM API.
### 💬 Conversational Interface
The Streamlit interface is capable of:
- Hosting a chat between user and PaddyBot
- Storing conversation history
- Displaying recent chats with titles
- Clearing chat history
- Providing suggested questions to the user
- Displaying sources
### 📄 Source Attribution
The retrieved response provides the source document and page number for
each piece of information used in generating the response.
---
# 🏗️ System Architecture
The overall PaddyBot system can be summarized as:
```text
Agricultural Knowledge Base
│
▼
PDF Document Loading
│
▼
Text Splitting
│
▼
Embedding Generation
│
▼
FAISS Vector Store
│
│
User Question
│
▼
Semantic Retrieval
│
▼
Relevant Documents
│
▼
RAG Prompt
│
▼
Local LLM via Ollama
│
▼
Generated Answer
│
▼
Streamlit UI
