from rag_pipeline import get_vector_store, add_sample_docs, add_uploaded_docs, search_docs

def main():
    vector_store = get_vector_store()

    # Optional: add sample docs
    add_sample_docs(vector_store)

    # Add real document
    file_path = input("Enter PDF or TXT file path to upload: ")
    add_uploaded_docs(vector_store, file_path)

    while True:
        query = input("\nAsk a question: ")
        results = search_docs(vector_store, query)
        print("Top Results:")
        for r in results:
            print("-", r.page_content)

if __name__ == "__main__":
    main()
