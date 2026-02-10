# Endee RAG Assignment

## Overview

This project demonstrates a **Retrieval-Augmented Generation (RAG) pipeline** using **Endee (nD) vector database** and **HuggingFace sentence embeddings**. It allows you to store documents as embeddings, and perform similarity search to answer queries efficiently.

---

## Features

- Store sample documents in **Endee vector store**  
- Use **HuggingFace sentence embeddings** for semantic search  
- Perform similarity search queries  
- Fully containerized using **Docker** (optional)  
- Easy setup with Python and virtual environment  

---

## Project Structure

rag_project/
├── app.py # Main script to run RAG pipeline
├── rag_pipeline.py # Functions for vector store, adding and searching docs
├── requirements.txt # Python dependencies
├── .env.example # Environment variables template
├── Dockerfile # Docker setup (optional)
├── README.md
└── venv/ # Python virtual environment (not pushed)


---

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/Anhu22/Endee_Assessment.git
cd Endee_Assessment/rag_project

    Create a Python virtual environment

python -m venv venv

    Activate the virtual environment

    Windows (PowerShell):

.\venv\Scripts\Activate.ps1

    macOS/Linux:

source venv/bin/activate

    Install dependencies

pip install -r requirements.txt

    Setup environment variables

    Copy .env.example to .env and fill in your tokens:

ENDEE_API_TOKEN=your_endee_api_token
HF_TOKEN=your_huggingface_token  # optional, for faster downloads

Running the Project

    Start Endee server

    Using Docker Compose:

docker-compose up -d

    Or using local binary (if built manually):

./build/ndd

    Run RAG pipeline

python app.py

    Example Output

    The program will add sample documents to the vector store, then allow you to ask a query:

Ask a question: What is machine learning?
Top Results:
- "Machine learning is a subset of Artificial Intelligence"
- "Deep learning uses neural networks to learn patterns"