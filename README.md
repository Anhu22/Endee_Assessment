## Endee RAG Assignment

## Overview

This project demonstrates a Retrieval-Augmented Generation (RAG) pipeline using Endee (nD) vector database and HuggingFace sentence embeddings. It allows you to store documents as embeddings, and perform semantic similarity search to answer queries efficiently.
The system supports uploading real PDF and TXT files, making it dynamic and interactive.

## Features

* Store sample documents in Endee vector store
* Upload real PDF or TXT files and add them to the vector store
* Use HuggingFace embeddings for semantic search
* Perform similarity search queries on uploaded documents
* Fully containerized using Docker (optional)
* Clean setup using Python and virtual environment

## Project Structure
```bash
rag_project/
├── app.py                 # Main script to run RAG pipeline
├── rag_pipeline.py        # Functions for vector store, adding and searching docs
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variables template
├── Dockerfile             # Docker setup (optional)
├── README.md
└── venv/                  # Python virtual environment (not pushed)
```

## Setup Instructions

1.Clone the repository:

```bash
git clone https://github.com/Anhu22/Endee_Assessment.git
cd Endee_Assessment/rag_project
```


2.Create a Python virtual environment:

```bash
python -m venv venv
```

3.Activate the virtual environment:
* Windows (PowerShell):
```bash
.\venv\Scripts\Activate.ps1
```

* macOS/Linux:
```bash
source venv/bin/activate
```

4.Install dependencies:
```bash
pip install -r requirements.txt
```

5.Setup environment variables:
```bash
cp .env.example .env
```

Fill in your tokens:
```bash
ENDEE_API_TOKEN=your_endee_api_token
HF_TOKEN=your_huggingface_token  # optional, for faster HuggingFace downloads
```
## Running the Project

1.Start Endee server:

* Using Docker Compose:
```bash
docker-compose up -d
```

* Or using local binary (if built manually):
```bash
./build/ndd
```

2.Run the main script:
```bash
python app.py
```

You can upload a PDF or TXT file and then ask queries.

## Example Output
```bash
Enter PDF or TXT file path to upload: C:\Users\Anhupama N E\OneDrive\Documents\40-Gate\Subject-wise Notes\Programming and DS Notes.pdf
Added 44 documents from C:\Users\Anhupama N E\OneDrive\Documents\40-Gate\Subject-wise Notes\Programming and DS Notes.pdf to vector store

Ask a question: Name types of data structures
Top Results:
- GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK  Design Against Static Load
5.1 1  DATA TYPES AND OPERATORS
1.1   Data Types
1.1.1 Primitive Data Type
(a) Integer Types:
✓ short int, unsigned short int
✓ int, unsigned int
✓ long int, unsigned long int
✓ long long int, unsigned long long int
...
- GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK  C Programming
5.27 6  TYPES OF DATA STRUCTURE , ARRAY & LINKED LIST
6.1.1 Linear  data structure
Every element can have almost 2 neighbours. Ex. arrays, linked list, stack, queue.
6.1.2 Non -Linear data structure
Element can have more than 2 neighbours. Ex. Tree, graph.
6.2 Arrays
6.2.1 1-D array
Theoretically index can start from any integer value. Let A be a 1-D array of n elements...
```

This demonstrates that the RAG system can dynamically ingest real documents and return relevant sections based on your query.

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
