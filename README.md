# 🌾 PaddyBot

## A Retrieval-Augmented Generation Assistant for Paddy Cultivation

PaddyBot is an AI-powered agricultural assistant designed to provide knowledge-grounded answers to questions related to paddy (rice) cultivation.

The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from a curated agricultural knowledge base and uses a locally running Large Language Model (LLM) to generate responses based on the retrieved context.

PaddyBot provides a Streamlit-based conversational interface and also supports command-line interaction.

---

## 📌 Overview

Paddy farmers and agricultural practitioners often need information covering multiple aspects of rice cultivation, including diseases, fertilizers, pests, irrigation, and general cultivation practices.

PaddyBot addresses this problem by combining:

- 📚 Agricultural knowledge documents
- 🔎 Semantic document retrieval
- 🧠 Transformer-based text embeddings
- 🗄️ FAISS vector similarity search
- 🤖 Local Large Language Model inference
- 💬 Conversational interaction
- 📄 Source and page-level references

Instead of relying only on the language model's internal knowledge, PaddyBot retrieves relevant information from the agricultural knowledge base before generating an answer.

---

## ✨ Features

### 🌾 Paddy Cultivation Assistance

PaddyBot can answer questions related to:

- Paddy diseases
- Disease symptoms and management
- Pest management
- Fertilizer recommendations
- Nutrient management
- Irrigation and water management
- General cultivation practices
- Harvesting and related agricultural practices

### 🔎 Retrieval-Augmented Generation

The system retrieves relevant document chunks from the agricultural knowledge base and provides them as context to the language model.

### 🧠 Semantic Search

Documents are converted into vector representations using a Sentence-Transformers embedding model.

The current application uses:

`sentence-transformers/all-MiniLM-L6-v2`

### 🗄️ FAISS Vector Database

FAISS is used for similarity search over the embedded knowledge-base chunks.

### 🤖 Local LLM

The application uses Ollama for locally running Large Language Models, allowing the generation component to operate without relying on a cloud-based LLM API.

### 💬 Conversational Interface

The Streamlit interface supports:

- Chat-style interaction
- Conversation history
- Recent chat titles
- Clear-chat functionality
- Suggested agricultural questions
- Source display

### 📄 Source Attribution

Retrieved responses can include the source document and page number, allowing users to trace the information used for generating an answer.

---

# 🏗️ System Architecture

The overall PaddyBot pipeline follows:

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

---

# 🔄 RAG Pipeline

PaddyBot follows a retrieval-augmented generation pipeline consisting of the following stages.

## 1. Document Loading

Agricultural PDF documents are loaded using LangChain's PDF document loading functionality.

The knowledge base contains documents covering areas such as:

- Rice cultivation
- Irrigation
- Diseases
- Fertilizers
- Nutrient management
- Pests
- Rice varieties
- Weed management
- Agricultural schemes

---

## 2. Document Splitting

The loaded documents are divided into smaller chunks using `RecursiveCharacterTextSplitter`.

Chunking allows the retrieval system to identify smaller, relevant sections of documents rather than processing entire documents during each query.

---

## 3. Embedding Generation

Each document chunk is converted into a numerical vector using the Sentence-Transformers model:

`sentence-transformers/all-MiniLM-L6-v2`

These vectors represent the semantic meaning of the corresponding document chunks.

---

## 4. FAISS Indexing

The generated embeddings are stored in a FAISS vector database.

When a user submits a question, the question is converted into the same embedding space and compared against the stored document vectors.

---

## 5. Similarity Retrieval

PaddyBot retrieves the most relevant document chunks using semantic similarity.

The application's retriever uses the configured `TOP_K` value to determine the number of retrieved documents.

---

## 6. Context-Aware Generation

The retrieved documents are passed to the RAG chain.

LangChain combines the retrieved context with the user query and sends it to the configured LLM through Ollama.

---

## 7. Response Generation

The LLM generates the final response using the retrieved agricultural information as contextual evidence.

This approach helps ground the generated response in the supplied knowledge base.

---

# 🧰 Technologies Used

| Component | Technology |
|---|---|
| Programming Language | Python |
| User Interface | Streamlit |
| RAG Framework | LangChain |
| Embeddings | Sentence-Transformers |
| Embedding Model | all-MiniLM-L6-v2 |
| Vector Database | FAISS |
| LLM Runtime | Ollama |
| PDF Processing | PyPDF |
| Deep Learning | PyTorch / Torchvision |
| Alternative Vector Database | Chroma |
| Evaluation | Custom Retrieval Evaluation Pipeline |

---

# 📦 Dependencies

The main dependencies used by the project include:

    streamlit
    langchain
    langchain-community
    langchain-classic
    langchain-text-splitters
    langchain-huggingface
    langchain-ollama
    sentence-transformers
    faiss-cpu
    chromadb
    pypdf
    ollama
    cryptography
    torchvision

The complete dependency list is available in:

`Backend/requirements.txt`

---

# 📂 Project Structure

    PaddyBot/
    │
    ├── Backend/
    │   │
    │   ├── app.py
    │   ├── chatbot.py
    │   ├── chroma_db.py
    │   ├── config.py
    │   ├── embeddings.py
    │   ├── frontend_app.py
    │   ├── ingest.py
    │   ├── llm.py
    │   ├── loaders.py
    │   ├── prompt.py
    │   ├── requirements.txt
    │   ├── retriever.py
    │   ├── splitter.py
    │   ├── vectordb.py
    │   │
    │   └── evaluation/
    │       ├── evaluator.py
    │       ├── metrics.py
    │       ├── questions.json
    │       ├── ground_truth.json
    │       ├── compare_models.py
    │       ├── create_pool.py
    │       ├── generate_results.py
    │       ├── pooled_annotation_final.csv
    │       ├── retrieval_results_manual.csv
    │       └── evaluation result CSV files
    │
    ├── Knowledge_Basis/
    │
    ├── Papers/
    │
    ├── .gitignore
    ├── README.md
    └── LICENSE

---

# ⚙️ Installation

## 1. Clone the Repository

    git clone https://github.com/YOUR_USERNAME/PaddyBot.git
    cd PaddyBot

Replace `YOUR_USERNAME` with the GitHub username associated with the repository.

---

## 2. Create a Virtual Environment

### Windows

    python -m venv venv

Activate the environment:

    venv\Scripts\activate

### Linux / macOS

    python3 -m venv venv
    source venv/bin/activate

---

## 3. Install Dependencies

From the project root:

    pip install -r Backend/requirements.txt

---

# 🤖 Ollama Setup

PaddyBot uses Ollama for local LLM inference.

Install Ollama on the system and make sure the required language model is available locally.

The LLM configuration used by PaddyBot is defined in:

`Backend/llm.py`

The exact model can therefore be configured according to the local deployment environment.

---

# 📚 Knowledge Base Setup

PaddyBot uses a collection of agricultural PDF documents as its knowledge base.

The knowledge base covers topics including:

- Cultivation
- Diseases
- Fertilizers
- Irrigation
- Pests
- Rice Varieties
- Weed Management
- Government Agricultural Schemes

Place the required agricultural PDF documents in the configured knowledge-base directory before running the ingestion process.

---

# 🗄️ Building the Vector Database

After preparing the knowledge base, run:

    cd Backend
    python ingest.py

The ingestion pipeline:

1. Loads the agricultural PDF documents.
2. Splits the documents into smaller chunks.
3. Generates embeddings.
4. Builds the FAISS vector database.
5. Saves the resulting vector index locally.

The generated vector database is intentionally excluded from version control because it can be recreated from the source documents.

---

# ▶️ Running PaddyBot

## Streamlit Application

From the `Backend` directory:

    streamlit run frontend_app.py

The Streamlit application provides an interactive conversational interface for asking questions about paddy cultivation.

---

## Command-Line Application

PaddyBot can also be used through the command line.

From the `Backend` directory:

    python app.py

The application accepts questions interactively:

    Ask a question (or type 'exit'):

The generated answer and the retrieved source documents are displayed in the terminal.

---

# 💬 Example Questions

Users can ask questions such as:

    What are the symptoms of blast disease?

    How often should I irrigate my paddy field?

    Which fertilizer is best during the tillering stage?

    How do I control brown planthopper?

    What are the major diseases affecting rice?

    What nutrients are required during different stages of rice cultivation?

    How can weeds be managed in a paddy field?

---

# 🧪 Retrieval Evaluation

A benchmark consisting of 100 agricultural questions is used to evaluate document retrieval performance.

The benchmark contains questions from five agricultural domains:

| Category | Questions |
|---|---:|
| General Cultivation | 20 |
| Disease Management | 20 |
| Pest Management | 20 |
| Nutrient Management | 20 |
| Irrigation and Water Management | 20 |
| **Total** | **100** |

The evaluation framework records the documents retrieved for each question and evaluates retrieval quality.

---

# 📊 Evaluation Metrics

The retrieval evaluation uses metrics including:

- Precision@K
- Recall@K
- Reciprocal Rank

The evaluation implementation is available in:

`Backend/evaluation/metrics.py`

The benchmark questions are stored in:

`Backend/evaluation/questions.json`

Ground-truth information is stored in:

`Backend/evaluation/ground_truth.json`

---

# 🧠 Embedding Model Comparison

The project evaluates multiple embedding models to investigate their retrieval performance for the agricultural knowledge base.

The evaluated models are:

1. `sentence-transformers/all-MiniLM-L6-v2`
2. `BAAI/bge-base-en-v1.5`
3. `intfloat/e5-base-v2`
4. `jinaai/jina-embeddings-v2-base-en`

The evaluation results are stored in:

`Backend/evaluation/`

---

# 🗄️ FAISS and Chroma Comparison

The evaluation framework compares two vector database approaches:

- FAISS
- Chroma

The main PaddyBot application currently uses FAISS as its vector retrieval backend.

Chroma is implemented as an alternative vector database for comparative evaluation.

The comparison investigates retrieval performance across different embedding models and vector database configurations.

---

# ⏱️ Retrieval Time Evaluation

The evaluation framework also measures retrieval time.

For each benchmark question, the similarity-search operation is timed independently.

The average retrieval time is then calculated across the benchmark questions.

This allows the system to compare not only retrieval quality but also retrieval efficiency across different embedding models and vector database configurations.

---

# 📈 Research Results

The repository contains the retrieval evaluation results generated during the experiments.

The evaluation files include results for:

- FAISS + all-MiniLM-L6-v2
- FAISS + BGE
- FAISS + E5
- FAISS + Jina
- Chroma + all-MiniLM-L6-v2
- Chroma + BGE
- Chroma + E5
- Chroma + Jina

The corresponding CSV files are available under:

`Backend/evaluation/`

These files can be used for further analysis and reproduction of the reported retrieval experiments.

---

# 🖼️ Project Visualizations

The project can include figures such as:

- `architecture.png`
- `faiss_performance.png`
- `faiss_chroma_comparison.png`

### Architecture

The architecture diagram illustrates the complete PaddyBot RAG pipeline from agricultural documents through retrieval and LLM-based response generation.

### FAISS Performance

The FAISS performance visualization compares retrieval performance across the evaluated embedding models.

### FAISS vs Chroma

The FAISS-Chroma comparison visualization presents the retrieval performance of the two vector database approaches.

---

# 🔬 Research Contribution

PaddyBot combines retrieval-augmented generation with agricultural knowledge retrieval to provide a domain-focused conversational assistant for paddy cultivation.

The research component investigates the effect of different embedding models and vector database implementations on retrieval quality and retrieval efficiency.

The evaluation uses a manually constructed agricultural benchmark covering multiple domains of rice cultivation.

---

# 🔐 Knowledge Base and Copyright

The agricultural source documents used to construct the knowledge base may be subject to their respective copyright and redistribution conditions.

Therefore, the repository does not necessarily redistribute all source PDF documents.

Users should obtain the relevant source documents independently and place them in the configured knowledge-base directory before running the ingestion pipeline.

---

# 🚀 Future Work

Future development will focus on:

- Deployment of PaddyBot as a publicly accessible agricultural assistance system.
- Expansion of the agricultural knowledge base.
- Support for additional crops and regional agricultural practices.
- Evaluation of additional embedding models.
- Investigation of hybrid retrieval approaches.
- Improvement of retrieval and response latency.
- Integration of more advanced agricultural decision-support features.
- Deployment of the system on scalable cloud infrastructure.
- Expansion of the system to support multilingual agricultural assistance.
---

This project is intended for academic and research purposes.

Please refer to the licenses and usage conditions of the individual software frameworks, models, datasets, and agricultural source documents used by the project.
