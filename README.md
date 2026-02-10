# Endee RAG Assignment

## Overview

This project demonstrates a **Retrieval-Augmented Generation (RAG) pipeline** using **Endee (nD) vector database** and **HuggingFace sentence embeddings**. The system allows efficient storage of documents as embeddings and semantic similarity search to answer user queries.

It’s designed as a **prototype of an intelligent knowledge retrieval system**, highlighting the integration of **vector databases** with **state-of-the-art NLP embeddings**, and can serve as a foundation for **question-answering systems, chatbots, and educational tools**.

---

## Features

* Store and manage documents in **Endee vector database**.
* Convert text documents to **semantic embeddings** using HuggingFace Sentence Transformers (`all-MiniLM-L6-v2`).
* Perform **fast similarity search** to answer natural language queries.
* Fully **containerized** with Docker for easy deployment (optional).
* Python-based, with **virtual environment support** for clean dependency management.
* Ready for extension to **larger datasets or multi-user applications**.

---

## Technologies Used

* **Python 3.11+**
* **Endee (nD) Vector Database** – high-performance vector storage.
* **LangChain / Endee-LangChain** – abstraction for vector storage and retrieval.
* **HuggingFace Sentence Transformers** – semantic embeddings (`all-MiniLM-L6-v2`).
* **Docker & Docker Compose** – optional containerized deployment.
* **.env configuration** – secure API token management.

---

## Project Structure

```
rag_project/
├── app.py                  # Main script to run RAG pipeline
├── rag_pipeline.py         # Core functions: vector store, add/search docs
├── requirements.txt        # Python dependencies
├── .env.example            # Template for environment variables
├── Dockerfile              # Optional Docker setup
├── docker-compose.yml      # Optional Docker Compose setup
├── README.md               # Project documentation
└── venv/                   # Python virtual environment (not pushed)
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Anhu22/Endee_Assessment.git
cd Endee_Assessment/rag_project
```

### 2. Create and activate a Python virtual environment

```bash
python -m venv venv
```

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env`:

```env
ENDEE_API_TOKEN=your_endee_api_token
HF_TOKEN=your_huggingface_token  # optional for faster model downloads
```

> **Note:** Do not commit your actual tokens. `.env` is ignored by Git.

---

## Running the Project

### Option 1: Using Docker Compose (Recommended)

```bash
docker-compose up -d
```

This will start the **Endee server** on `localhost:8080`.

### Option 2: Using Local Binary

If you have built Endee manually:

```bash
./build/ndd
```

### Run the RAG Pipeline

```bash
python app.py
```

---

## Example Usage

The pipeline adds **sample documents** to the Endee vector store and allows the user to query them:

```
Ask a question: What is machine learning?
Top Results:
1. "Machine learning is a subset of Artificial Intelligence"
2. "Deep learning uses neural networks to learn patterns"
```

> This demonstrates **semantic search** where the system retrieves relevant answers even if the query does not exactly match the text in the documents.

---

## Code Highlights

* **rag_pipeline.py**

  * `get_vector_store()`: Initializes Endee vector store with HuggingFace embeddings.
  * `add_sample_docs(vector_store)`: Adds sample documents to the vector store.
  * `search_docs(vector_store, query)`: Searches documents semantically using vector similarity.

* **app.py**

  * Interactive CLI for querying the RAG pipeline.
  * Handles setup, vector store initialization, and querying workflow.

* **requirements.txt**

  * Lists all dependencies, ensuring reproducibility.

---

## Achievements & Takeaways

* Integrated **state-of-the-art NLP embeddings** with a **high-performance vector database**.
* Built a **retrieval system capable of semantic similarity search**.
* Learned best practices for:

  * Environment management (`.env`, virtualenv)
  * Dependency tracking (`requirements.txt`)
  * Containerized deployment with Docker
* Ensured **clean code structure and modular design** for easy extensions.

---
## References

* [Endee Docs](https://docs.endee.io/quick-start)
* [HuggingFace Sentence Transformers](https://huggingface.co/sentence-transformers)
* [LangChain Documentation](https://www.langchain.com/docs/)






