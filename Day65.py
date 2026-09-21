print("Create a Conversation List")
conversation = [
    "Hello",
    "My name is Rahul",
    "I am from Kerala",
    "I am learning Python",
    "I want to learn AI"
]
print(conversation)

 
print("Modify Chatbot to Save Messages")
from openai import OpenAI
client = OpenAI(api_key="YOUR_API_KEY")
conversation = []
print("AI Chatbot with Memory")
print("Type 'bye' to exit.")
while True:
    user = input("You: ")
    if user.lower() == "bye":
        print("Bot: Goodbye!")
        break
    conversation.append({
        "role": "user",
        "content": user
    })
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=conversation
    )
    answer = response.output_text
    print("Bot:", answer)
    conversation.append({
        "role": "assistant",
        "content": answer
    })
