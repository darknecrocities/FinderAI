import pandas as pd
from langchain.docstore.document import Document

def load_excel(file_path):
    df = pd.read_excel(file_path)
    docs = []
    for i, row in df.iterrows():
        content = "\n".join([f"{col}: {row[col]}" for col in df.columns])
        docs.append(Document(page_content=content))
    return docs
