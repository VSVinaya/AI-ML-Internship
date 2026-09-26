print("Create ChromaDB Collection and Convert into Retriever")
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
documents = [
    "The AI internship fee is 5000 rupees.",
    "The internship duration is 3 months.",
    "Placement assistance is available.",
    "Students will learn Python programming.",
    "The internship includes Machine Learning projects.",
    "The course covers Artificial Intelligence.",
    "Students receive a certificate after completion.",
    "The internship provides practical training.",
    "The internship is suitable for beginners.",
    "Students learn about RAG and LLMs."
]
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)
vectorstore = Chroma.from_texts(
    documents,
    embedding_model
)
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)
print("Retriever created successfully!")



print("Retrieve Top 3 Results for Five Questions")
questions = [
    "What is the internship fee?",
    "How long is the internship?",
    "Is placement assistance available?",
    "What programming language will students learn?",
    "What is included in the internship?"
]
for question in questions:
    print("\nQuestion:", question)
    docs = retriever.invoke(question)
    print("Top 3 Results:")
    for i, doc in enumerate(docs, start=1):
        print(f"{i}. {doc.page_content}")
