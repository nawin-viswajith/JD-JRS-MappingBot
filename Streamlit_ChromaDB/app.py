if __name__ == "__main__":
    import streamlit as st
    import chromadb
    import os

    def main():
        # Initialize ChromaDB client
        script_dir = os.path.dirname(__file__)
        chromadb_path = os.path.join(script_dir, 'ChromaDB', 'chroma_storage')
        client = chromadb.PersistentClient(path=chromadb_path)

        # Specify the collection name
        collection_name = "jd_jrs_data"

        st.title("JD-JRS Search")

        # Get user input
        query = st.text_area("Enter your query:", "")

        if st.button("Submit"):
            try:
                collection = client.get_collection(collection_name)
                results = collection.query(
                    query_texts=[query],
                    n_results=5
                )
                for output in results['documents'][0]:
                    st.write(output)

            except ValueError as e:
                st.error(f"Failed to access collection: {e}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

    main()
