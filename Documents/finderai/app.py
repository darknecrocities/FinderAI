import streamlit as st
from utils.file_utils import save_uploaded_file
from loaders.pdf_loader import load_pdf
from loaders.docx_loader import load_docx
from loaders.excel_loader import load_excel
from loaders.text_loader import load_txt
from processing.cleaner import clean_text
from processing.chunker import chunk_documents
from rag.retriever import build_vectorstore
from rag.qa_chain import get_local_llm, build_qa_chain

st.set_page_config(page_title="LocalDocGPT", layout="wide")
st.title("📄 LocalDocGPT - Ask Questions on Your Documents (Windows Ollama)")

uploaded_files = st.file_uploader(
    "Upload documents (PDF, DOCX, XLSX, TXT)",
    type=["pdf", "docx", "xlsx", "csv", "txt"],
    accept_multiple_files=True
)

if uploaded_files:
    documents = []
    for file in uploaded_files:
        file_path = save_uploaded_file(file)
        if file.name.endswith(".pdf"):
            docs = load_pdf(file_path)
        elif file.name.endswith(".docx"):
            docs = load_docx(file_path)
        elif file.name.endswith((".xlsx", ".csv")):
            docs = load_excel(file_path)
        elif file.name.endswith(".txt"):
            docs = load_txt(file_path)
        else:
            continue

        # Clean and chunk
        for doc in docs:
            doc.page_content = clean_text(doc.page_content)
        chunks = chunk_documents(docs)
        documents.extend(chunks)

    st.success(f"Loaded {len(documents)} document chunks!")

    # Build vectorstore
    vectorstore = build_vectorstore(documents)
    st.success("Vectorstore built successfully!")

    # Load Ollama LLM
    llm = get_local_llm(model_name="mistral")
    qa_chain = build_qa_chain(vectorstore, llm)

    # Ask question
    question = st.text_input("Ask a question about your documents")
    if question:
        result = qa_chain.run(question)
        st.subheader("🤖 Answer:")
        st.write(result)
