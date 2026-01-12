from langchain.document_loaders import Docx2txtLoader

def load_docx(file_path):
    loader = Docx2txtLoader(file_path)
    return loader.load()
