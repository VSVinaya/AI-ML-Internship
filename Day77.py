print("Store Documents in ChromaDB with Metadata")
import chromadb
print("METADATA FILTERING AND SOURCE CITATION")
client = chromadb.Client()
collection = client.get_or_create_collection(
    name="day77_metadata"
)
documents = [
    "The leave policy allows employees to apply for leave through the HR portal.",
    "Employees can submit travel reimbursement claims through the finance department.",
    "Employees must change their system password regularly for security.",
    "Employees should mark their attendance every working day.",
    "Students can borrow library books according to the library rules."
]
ids = [
    "doc1",
    "doc2",
    "doc3",
    "doc4",
    "doc5"
]
metadatas = [
    {
        "filename": "HR_Policy.pdf",
        "page": 5,
        "department": "HR"
    },
    {
        "filename": "Finance_Policy.pdf",
        "page": 3,
        "department": "Finance"
    },
    {
        "filename": "IT_Guide.pdf",
        "page": 7,
        "department": "IT"
    },
    {
        "filename": "HR_Attendance.pdf",
        "page": 8,
        "department": "HR"
    },
    {
        "filename": "Library_Rules.pdf",
        "page": 2,
        "department": "Library"
    }
]
collection.upsert(
    documents=documents,
    ids=ids,
    metadatas=metadatas
)
print("\nFive documents stored successfully in ChromaDB.")
question = "What is the leave policy?"
print("HR METADATA FILTERING")
results = collection.query(
    query_texts=[question],
    n_results=2,
    where={"department": "HR"}
)
print("\nQuestion:")
print(question)
print("\nRetrieved HR Documents:")
for i, document in enumerate(results["documents"][0]):
    metadata = results["metadatas"][0][i]
    print("\nDocument:")
    print(document)
    print("Department:", metadata["department"])
    print("Source:", metadata["filename"])
print("ANSWER WITH SOURCE CITATION")
results = collection.query(
    query_texts=[question],
    n_results=1,
    where={"department": "HR"}
)
answer = results["documents"][0][0]
metadata = results["metadatas"][0][0]
print("\nQuestion:")
print(question)
print("\nAnswer:")
print(answer)
print("\nSource:")
print("File:", metadata["filename"])
print("Page:", metadata["page"])
print("PRACTICAL TASK 5 - RETRIEVAL COMPARISON")
without_filter = collection.query(
    query_texts=[question],
    n_results=3
)
print("\nWITHOUT METADATA FILTERING:")
for i, document in enumerate(without_filter["documents"][0]):
    metadata = without_filter["metadatas"][0][i]
    print("\nDocument:", document)
    print("Department:", metadata["department"])
    print("Source:", metadata["filename"])
with_filter = collection.query(
    query_texts=[question],
    n_results=3,
    where={"department": "HR"}
)
print("\nWITH HR METADATA FILTERING:")
for i, document in enumerate(with_filter["documents"][0]):
    metadata = with_filter["metadatas"][0][i]
    print("\nDocument:", document)
    print("Department:", metadata["department"])
    print("Source:", metadata["filename"])
