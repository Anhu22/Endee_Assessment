import os
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from endee_langchain import EndeeVectorStore

# For PDF reading
from PyPDF2 import PdfReader

load_dotenv()

def get_vector_store():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = EndeeVectorStore.from_params(
        embedding=embeddings,
        api_token=os.getenv("ENDEE_API_TOKEN"),
        index_name="student_docs_384",
        dimension=384,
        precision="float32",
        space_type="cosine"
    )
    return vector_store

def add_sample_docs(vector_store):
    docs = [
        Document(page_content="Machine learning is a subset of Artificial Intelligence"),
        Document(page_content="Deep learning uses neural networks to learn patterns"),
        Document(page_content="Vector databases store embeddings for similarity search")
    ]
    vector_store.add_documents(docs)

def add_uploaded_docs(vector_store, file_path):
    """
    Upload and add a PDF or TXT file to the vector store
    """
    docs = []

    if file_path.lower().endswith(".pdf"):
        reader = PdfReader(file_path)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                docs.append(Document(page_content=text))

    elif file_path.lower().endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
            docs.append(Document(page_content=text))
    else:
        raise ValueError("Unsupported file type. Only PDF and TXT are allowed.")

    if docs:
        vector_store.add_documents(docs)
        print(f"Added {len(docs)} documents from {file_path} to vector store")
    else:
        print(f"No text found in {file_path}")

def search_docs(vector_store, query, k=2):
    """
    Perform a similarity search on the vector store
    """
    results = vector_store.similarity_search(query, k=k)
    return results
