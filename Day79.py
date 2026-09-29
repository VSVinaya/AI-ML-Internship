import chromadb
client = chromadb.Client()
collection = client.get_or_create_collection(
    name="day79_rag_evaluation"
)
documents = [
    "The AI ML internship duration is 3 months.",
    "The internship is conducted with live mentor sessions.",
    "The internship includes Python and Machine Learning projects.",
    "The internship includes practical tasks based on AI and Machine Learning.",
    "Interns are expected to complete the assigned tasks regularly.",
    "Python is used for data processing and machine learning activities.",
    "Machine Learning allows computers to learn patterns from data.",
    "RAG stands for Retrieval Augmented Generation.",
    "RAG retrieves relevant information before generating an answer.",
    "Source citations help users verify the information used by the system."
]
ids = [
    "doc1",
    "doc2",
    "doc3",
    "doc4",
    "doc5",
    "doc6",
    "doc7",
    "doc8",
    "doc9",
    "doc10"
]
collection.upsert(
    documents=documents,
    ids=ids
)
print("\n10 documents stored in ChromaDB successfully.")
questions = [
    "How long is the AI ML internship?",
    "Does the internship have live mentor sessions?",
    "What type of projects are included in the internship?",
    "What are interns expected to do?",
    "Which language is used for data processing?",
    "What is Machine Learning?",
    "What does RAG stand for?",
    "What does RAG do?",
    "Why are source citations useful?",
    "What is included in the practical tasks?"
]
expected_answers = [
    "3 months",
    "live mentor sessions",
    "Python and Machine Learning projects",
    "complete the assigned tasks regularly",
    "Python",
    "learn patterns from data",
    "Retrieval Augmented Generation",
    "retrieves relevant information",
    "verify the information",
    "AI and Machine Learning"
]
def check_faithfulness(answer, retrieved_documents):
    answer_words = set(answer.lower().split())
    context = " ".join(retrieved_documents).lower()
    important_words = [
        word.strip(".,?!")
        for word in answer_words
        if len(word) > 3
    ]
    matched_words = 0
    for word in important_words:
        if word in context:
            matched_words += 1
    if len(important_words) == 0:
        return "Yes"
    percentage = matched_words / len(important_words)
    if percentage >= 0.5:
        return "Yes"
    return "No"
print("10 QUESTION EVALUATION")
evaluation_results = []
for i in range(len(questions)):
    question = questions[i]
    expected = expected_answers[i]
    results = collection.query(
        query_texts=[question],
        n_results=3
    )
    retrieved_documents = results["documents"][0]
    context = " ".join(retrieved_documents).lower()
    if expected.lower() in context:
        answer = expected
        correct = "Yes"
    else:
        answer = "I don't know."
        correct = "No"
    faithful = check_faithfulness(
        answer,
        retrieved_documents
    )
    if answer == "I don't know.":
        hallucination = "No"
    elif faithful == "Yes":
        hallucination = "No"
    else:
        hallucination = "Yes"
    print("\nQuestion", i + 1)
    print("Question:", question)
    print("\nRetrieved Documents:")
    for document in retrieved_documents:
        print("-", document)
    print("\nAnswer:", answer)
    print("Correct Answer?:", correct)
    print("Hallucination?:", hallucination)
    print("Faithful?:", faithful)
    evaluation_results.append({
        "question": question,
        "documents": retrieved_documents,
        "correct": correct,
        "hallucination": hallucination,
        "faithful": faithful
    })
print("UNKNOWN QUESTION")
unknown_question = "What is the internship stipend amount?"
unknown_results = collection.query(
    query_texts=[unknown_question],
    n_results=3
)
unknown_documents = unknown_results["documents"][0]
print("\nQuestion:")
print(unknown_question)
print("\nRetrieved Documents:")
for document in unknown_documents:
    print("-", document)
stipend_found = False
for document in unknown_documents:
    if "stipend" in document.lower():
        stipend_found = True
if stipend_found:
    print("\nAnswer: Information about the stipend was found.")
else:
    print("\nAnswer: I don't know.")
    print("Observation: The requested information is not present in the documents.")
    print("The system avoided giving an unsupported answer.")
print("TOP-1 VS TOP-3 VS TOP-5")
comparison_question = "What does RAG do?"
for top_k in [1, 3, 5]:
    results = collection.query(
        query_texts=[comparison_question],
        n_results=top_k
    )
    retrieved_documents = results["documents"][0]
    print("\nTOP-", top_k)
    for document in retrieved_documents:
        print("-", document)

