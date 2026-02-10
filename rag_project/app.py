from rag_pipeline import get_vector_store, add_sample_docs, search_docs

def main():

    print("Starting Endee RAG Test...")

    vector_store = get_vector_store()

    add_sample_docs(vector_store)

    query = input("Ask a question: ")

    results = search_docs(vector_store, query)

    print("\nTop Results:\n")

    for r in results:
        print("-", r.page_content)

if __name__ == "__main__":
    main()
