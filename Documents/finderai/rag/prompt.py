def get_prompt(context, question):
    return f"""
You are a helpful AI assistant.
Answer ONLY using the context provided.

Context:
{context}

Question:
{question}

If the answer is not found in the context, say: "I cannot find this information in the uploaded documents."
"""
