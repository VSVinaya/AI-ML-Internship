print("Create Collection in Chromadb")
import chromadb
client = chromadb.Client()
collection = client.create_collection(
    name="college_data"
)
print("Collection created successfully.")


print("Insert Five Sample Documents")
client = chromadb.Client()
collection = client.get_or_create_collection(
    name="college_data"
)
documents = [
    "AI Internship Fee is ₹5000.",
    "The internship duration is 3 months.",
    "Students with basic Python knowledge are eligible.",
    "Hostel facilities are available for students.",
    "Placement assistance is provided after the internship."
]
ids = [
    "doc1",
    "doc2",
    "doc3",
    "doc4",
    "doc5"
]
collection.add(
    documents=documents,
    ids=ids
)
print("Five documents added successfully.")


print("Search for the Internship Duration")
question = "How long is the internship?"
results = collection.query(
    query_texts=[question],
    n_results=1
)
print("\nSearch Question:")
print(question)
print("\nRetrieved Result:")
print(results["documents"][0][0])
