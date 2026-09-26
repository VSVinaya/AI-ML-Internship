print("prompt template")
from langchain.prompts import PromptTemplate
template = """
You are a helpful AI assistant.
Context:
{context}
Question:
{question}
Answer:
"""
prompt = PromptTemplate(
input_variables=["context", "question"],
template=template
)

