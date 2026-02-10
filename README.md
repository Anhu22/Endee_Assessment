# Endee RAG Assignment

## Overview

This project demonstrates a **Retrieval-Augmented Generation (RAG)** system powered by the **Endee (nD) vector database** and **HuggingFace sentence embeddings**. It allows storing documents as semantic embeddings and performing **similarity search** for dynamic queries. Users can upload **PDF or TXT files**, which are automatically converted into embeddings for retrieval.

The project showcases a practical application of **vector databases**, enabling AI to find relevant information efficiently without relying on traditional keyword search.

---

## Features

* Store sample documents and user-uploaded PDFs/TXTs in the Endee vector store
* Use **HuggingFace embeddings** for semantic understanding
* Perform similarity search queries over document embeddings
* Demonstrates **RAG workflow**: retrieve relevant content + generate informed responses
* Fully containerized (optional) using **Docker**
* Easy setup using Python virtual environment
* Clean and modular project structure for extensibility

---

## Project Structure

```
rag_project/
├── app.py               # Main script to run the RAG pipeline
├── rag_pipeline.py      # Functions for vector store, adding, and searching docs
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
├── Dockerfile           # Docker setup (optional)
├── README.md            # Project documentation
└── venv/                # Python virtual environment (not pushed)
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Anhu22/Endee_Assessment.git
cd Endee_Assessment/rag_project
```

### 2. Create a Python virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

* **Windows (PowerShell):**

```bash
.\venv\Scripts\Activate.ps1
```

* **macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Setup environment variables

Copy `.env.example` to `.env` and fill in your tokens:

```
ENDEE_API_TOKEN=your_endee_api_token
HF_TOKEN=your_huggingface_token  # optional, for faster downloads
```

---

## Running the Project

### 1. Start Endee server

* Using Docker Compose:

```bash
docker-compose up -d
```

* Or using local binary (if built manually):

```bash
./build/ndd
```

### 2. Run the RAG pipeline

```bash
python app.py
```

### 3. Upload documents (dynamic testing)

When prompted, enter the path to a PDF or TXT file to add it to the vector store. Example:

```
Enter PDF or TXT file path to upload: "C:\Users\Anhupama N E\Documents\40-Gate\Subject-wise Notes\CN Notes.pdf"
```

### 4. Ask a query

After uploading documents, the system allows you to ask queries based on the uploaded content:

```
Ask a question: What is machine learning?
Top Results:
- "Machine learning is a subset of Artificial Intelligence"
- "Deep learning uses neural networks to learn patterns"
```

---

## Core Vector Database Usage

This project leverages **Endee vector database** to store and retrieve embeddings:

* Each document is converted into a **dense semantic vector** using HuggingFace embeddings
* Queries are transformed into vectors and compared using **cosine similarity**
* This allows **semantic search**, retrieving content based on meaning rather than exact keywords
* Uploading dynamic documents (PDF/TXT) ensures the RAG system adapts and responds to new data

---

## Optional: Docker

* Build and run using Docker for easier deployment:

```bash
docker build -t endee-rag .
docker run -p 8080:8080 endee-rag
```

---

## Notes

* Only PDF and TXT files are supported for uploads
* Ensure the Endee server is running before executing the pipeline
* HuggingFace embeddings may require an API token for faster downloads
