print("Load a Sample PDF")
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("sample.pdf")
documents = loader.load()
print("PDF loaded successfully!")
print("Number of pages:", len(documents))


print("Split PDF into Chunks")
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
loader = PyPDFLoader("sample.pdf")
documents = loader.load()
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(documents)
print("PDF loaded successfully!")
print("Number of pages:", len(documents))
print("Number of chunks:", len(chunks))


print("Store in ChromaDB and Search")
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
# Step 3 - Create embeddings
embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)
print("Embeddings created!")
# Step 4 - Store chunks in ChromaDB
db = Chroma.from_documents(
    chunks,
    embedding
)
print("Chunks stored in ChromaDB!")
# Step 5 - Perform similarity search
questions = [
    "What is the admission fee?",
    "What courses are available?",
    "Where is the college located?"
]
for question in questions:
    print("\nQuestion:", question)
    results = db.similarity_search(
        question,
        k=3
    )
    print("Relevant information:")
    for result in results:
        print(result.page_content[:300])
        print()
