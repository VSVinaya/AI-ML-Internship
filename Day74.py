print("Load a PDF")
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("sample.pdf")
documents = loader.load()
print("PDF loaded successfully!")
print("Number of pages:", len(documents))
print("\nFirst page:")
print(documents[0].page_content)


print("Split the PDF into Chunks")
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
loader = PyPDFLoader("sample.pdf")
documents = loader.load()
print("PDF loaded successfully!")
print("Number of pages:", len(documents))
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(documents)
print("Number of chunks:", len(chunks))


print("Store Chunks in ChromaDB and Create Retriever")
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
loader = PyPDFLoader("sample.pdf")
documents = loader.load()
print("PDF loaded!")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(documents)
print("Number of chunks:", len(chunks))
embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)
print("Embeddings created!")
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding
)
print("Chunks stored in ChromaDB!")
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)
print("Retriever created successfully!")


print("Retrieve Top 3 Results for Five Questions")
questions = [
    "What is the admission fee?",
    "What is the eligibility?",
    "How long is the course?",
    "What courses are available?",
    "Where is the college located?"
]
for question in questions:
    print("\n==============================")
    print("Question:", question)
    print("==============================")
    docs = retriever.invoke(question)
    print("Top 3 relevant chunks:")
    for i, doc in enumerate(docs, start=1):
        print(f"\n{i}.")
        print(doc.page_content)
