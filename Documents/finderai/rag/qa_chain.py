from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

def get_local_llm(model_name="mistral"):
    """
    Loads a local Ollama model.
    Make sure you have pulled the model in Ollama desktop.
    """
    llm = Ollama(model=model_name, temperature=0)
    return llm

def build_qa_chain(vectorstore, llm):
    """
    Builds a RetrievalQA chain using Ollama local model.
    """
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return qa
