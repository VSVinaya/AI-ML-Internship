print("Send a Greeting to the AI Model")
from openai import OpenAI
client = OpenAI(api_key="YOUR_API_KEY")
response = client.responses.create(
    model="gpt-4.1-mini",
    input="Hello! How are you?"
)
print("AI:", response.output_text)


print("Continue Conversation Until User Types bye")
from openai import OpenAI
client = OpenAI(api_key="YOUR_API_KEY")
print("AI Chatbot")
print("Type 'bye' to exit.\n")
while True:
    user = input("You: ")
    if user.lower() == "bye":
        print("Bot: Goodbye!")
        break
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=user
    )
    print("Bot:", response.output_text)


print("Create a Chatbot")
from openai import OpenAI
client = OpenAI(api_key="YOUR_API_KEY")
print("AI Learning Chatbot")
print("Ask me about AI, Python, Machine Learning, or Data Science.")
print("Type 'bye' to exit.\n")
while True:
    user = input("You: ")
    if user.lower() == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    prompt = f"""
    You are an educational chatbot.
    Answer the user's question clearly and simply.
    The main topics are:
    - Artificial Intelligence
    - Python
    - Machine Learning
    - Data Science
    User question:
    {user}
    """
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    print("Bot:", response.output_text)

