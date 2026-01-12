from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_documents(documents, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    all_chunks = []
    for doc in documents:
        chunks = splitter.split_text(doc.page_content)
        for chunk in chunks:
            all_chunks.append(doc.__class__(page_content=chunk))
    return all_chunks
