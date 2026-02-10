import os
from dotenv import load_dotenv

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from endee_langchain import EndeeVectorStore

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


def search_docs(vector_store, query):

    results = vector_store.similarity_search(query, k=2)

    return results
