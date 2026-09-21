print("College admission chatbot")
knowledge_base = {
    "admission": "Admissions are open for students.",
    "courses": "The college offers undergraduate and postgraduate courses.",
    "fees": "The course fee depends on the programme. Please contact the college office for exact fee details.",
    "documents": "Students need their qualifying examination certificate, mark list, ID proof and passport-size photographs.",
    "contact": "Students can contact the college admission office for more information."
}
print("College Admission Chatbot")
print("Type 'bye' to exit.\n")
while True:
    question = input("You: ").lower().strip()
    if question == "bye":
        print("Bot: Thank you! Goodbye!")
        break
    found = False
    for key, answer in knowledge_base.items():
        if key in question:
            print("Bot:", answer)
            found = True
            break
    if not found:
        print("Bot: Sorry, I could not find an answer in my knowledge base.")

