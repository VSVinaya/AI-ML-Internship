print("Create a ChromaDB Collection")
import chromadb
client = chromadb.Client()
collection = client.create_collection(name="internship_documents")
documents = [
    "The AI internship fee is 5000 rupees.",
    "The AI internship duration is 3 months.",
    "Placement assistance is available for students.",
    "The internship covers Artificial Intelligence.",
    "Students will learn Machine Learning concepts.",
    "Python programming is included in the internship.",
    "The internship includes practical projects.",
    "Students receive a certificate after completion.",
    "The internship provides hands-on training.",
    "The internship focuses on AI and Machine Learning."
]
collection.add(
    documents=documents,
    ids=[str(i) for i in range(10)]
)
print("10 documents stored successfully!")



print("Perform Similarity Searches")
questions = [
    "What is the internship fee?",
    "How long is the internship?",
    "Is placement assistance available?"
]
for question in questions:
    print("\nQuestion:", question)
    results = collection.query(
        query_texts=[question],
        n_results=3
    )
    print("Retrieved documents:")
    for document in results["documents"][0]:
        print("-", document)



print("Change n_results")
question = "How long is the internship?"
for number in [1, 3, 5]:
    print("\n----------------------")
    print("n_results =", number)
    print("----------------------")
    results = collection.query(
        query_texts=[question],
        n_results=number
    )
    for document in results["documents"][0]:
        print("-", document)



print("User Query and Top 3 Results")
import chromadb
client = chromadb.Client()
collection = client.create_collection(name="documents")
documents = [
    "The AI internship fee is 5000 rupees.",
    "The AI internship duration is 3 months.",
    "Placement assistance is available for students.",
    "The internship covers Artificial Intelligence.",
    "Students will learn Machine Learning concepts.",
    "Python programming is included in the internship.",
    "The internship includes practical projects.",
    "Students receive a certificate after completion.",
    "The internship provides hands-on training.",
    "The internship focuses on AI and Machine Learning."
]
collection.add(
    documents=documents,
    ids=[str(i) for i in range(10)]
)
query = input("Enter your question: ")
results = collection.query(
    query_texts=[query],
    n_results=3
)
print("\nTop 3 Similar Documents:")
for i, document in enumerate(results["documents"][0], start=1):
    print(f"{i}. {document}")
