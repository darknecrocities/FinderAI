from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def build_vectorstore(documents, model_name="sentence-transformers/all-MiniLM-L6-v2"):
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    vectorstore = FAISS.from_documents(documents, embeddings)
    vectorstore.save_local("data/vectorstore")
    return vectorstore

def load_vectorstore(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    vectorstore = FAISS.load_local("data/vectorstore", embeddings)
    return vectorstore

## Note: The above code defines functions to build and load a FAISS vectorstore