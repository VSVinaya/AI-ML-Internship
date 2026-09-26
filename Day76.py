print("Load All PDFs from the Folder")
import os
from langchain_community.document_loaders import PyPDFLoader
documents = []
folder = "Documents"
for file in os.listdir(folder):
    if file.endswith(".pdf"):
        file_path = os.path.join(folder, file)
        loader = PyPDFLoader(file_path)
        loaded_documents = loader.load()
        documents.extend(loaded_documents)
        print("Loaded:", file)
print("\nTotal pages loaded:", len(documents))


print("Split Documents and Generate Embeddings")
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
chunks = splitter.split_documents(documents)
print("Total chunks:", len(chunks))
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
print("Embeddings created successfully!")
 

print("Store Chunks in ChromaDB and Create Retriever")
from langchain_chroma import Chroma
vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="./chroma_db"
)
print("Documents stored in ChromaDB!")
retriever = vector_db.as_retriever(
    search_kwargs={"k": 3}
)
print("Retriever created successfully!")


print("Ask Questions and Check the Sources")
questions = [
    "What is the internship duration?",
    "What time does the office start?",
    "What does the leave policy say?",
    "What are the company working hours?",
    "What information is provided about employee training?"
]
for question in questions:
    print("\n================================")
    print("Question:", question)
    print("================================")
    results = retriever.invoke(question)
    for i, doc in enumerate(results, start=1):
        print(f"\nResult {i}:")
        print(doc.page_content)
        print("Source:", doc.metadata.get("source"))
        print("Page:", doc.metadata.get("page"))
