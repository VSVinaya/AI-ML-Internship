print("Create a chatbot")
print("AI Assistant")
print("Type 'bye' to exit.\n")
while True:
    user = input("You: ").lower()
    if user == "hello":
        print("Bot: Hello! How can I help you?")
    elif user == "hi":
        print("Bot: Hi! Welcome.")
    elif user == "your name":
        print("Bot: I'm an AI Chatbot.")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")


print("College Enquiry Chatbot")
faq = {
    "fees": "The course fee is ₹15,000.",
    "duration": "The course duration is 3 years.",
    "location": "Our college is located in Kochi.",
    "admission": "Admissions are currently open.",
    "contact": "You can contact us at 9876543210."
}
while True:
    user = input("You: ").lower()
    if user == "bye":
        print("Bot: Thank you! Have a nice day.")
        break
    found = False
    for key in faq:
        if key in user:
            print("Bot:", faq[key])
            found = True
            break
    if not found:
        print("Bot: Sorry! Please contact the college office.")


print("Use a Python Dictionary")
responses = {
    "hello": "Hello!",
    "hi": "Hi!",
    "how are you": "I'm fine.",
    "your name": "I'm AI Bot."
}
user = input("You: ").lower()
print(responses.get(user, "Sorry! I don't understand."))


print("Add Keyword Matching")
user = input("You: ").lower()
if "hello" in user:
    print("Bot: Hello!")
elif "fees" in user:
    print("Bot: The course fee is ₹15,000.")
else:
    print("Bot: Sorry! I don't understand.")
