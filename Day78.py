print("Create a chatbot using Conversation Buffer Memory.")
from langchain_classic.memory import (
    ConversationBufferMemory,
    ConversationBufferWindowMemory
)
print("\nCONVERSATION BUFFER MEMORY")
buffer_memory = ConversationBufferMemory()
def chatbot(memory, user_message, bot_response):
    memory.save_context(
        {"input": user_message},
        {"output": bot_response}
    )
    print("\nUser:", user_message)
    print("Bot:", bot_response) 
chatbot(
    buffer_memory,
    "My name is Vinaya.",
    "Nice to meet you, Vinaya."
)
chatbot(
    buffer_memory,
    "I live in Kochi.",
    "That is nice. You live in Kochi."
)
print(buffer_memory.load_memory_variables({})["history"])
print("\n TESTING MEMORY")
memory = ConversationBufferMemory()
chatbot(
    memory,
    "My name is Vinaya.",
    "Nice to meet you, Vinaya."
)
chatbot(
    memory,
    "I live in Kochi.",
    "Got it. You live in Kochi."
)
chatbot(
    memory,
    "I am studying Computer Science.",
    "Computer Science is your field of study."
)
chatbot(
    memory,
    "I am interested in Data Science.",
    "That is an interesting area to learn."
)
chatbot(
    memory,
    "What is my name and where do I live?",
    "Your name is Vinaya and you live in Kochi."
)
print("\nStored Chat History:")
print(memory.load_memory_variables({})["history"])
print("\nMemory Test Result:")
print("\nBUFFER VS WINDOW MEMORY")
buffer_memory = ConversationBufferMemory()
window_memory = ConversationBufferWindowMemory(k=5)
conversations = [
    ("My name is Vinaya.", "Nice to meet you, Vinaya."),
    ("I live in Kochi.", "You live in Kochi."),
    ("I study Computer Science.", "You study Computer Science."),
    ("I am interested in Data Science.", "Data Science is your interest."),
    ("I am doing an AI/ML internship.", "You are doing an AI/ML internship."),
    ("I like programming.", "Programming is one of your interests."),
    ("I am learning RAG.", "RAG is one of the topics you are learning.")
]
for user_message, bot_response in conversations:
    buffer_memory.save_context(
        {"input": user_message},
        {"output": bot_response}
    )
    window_memory.save_context(
        {"input": user_message},
        {"output": bot_response}
    )
print("\nBUFFER MEMORY:")
print(buffer_memory.load_memory_variables({})["history"])
print("\nWINDOW MEMORY (k=5):")
print(window_memory.load_memory_variables({})["history"])
print("\nObservation:")
print("\nREMEMBERING USER DETAILS")
user_memory = ConversationBufferMemory()
chatbot(
    user_memory,
    "My name is Vinaya.",
    "I will remember your name, Vinaya."
)
chatbot(
    user_memory,
    "I live in Kochi.",
    "I will remember that you live in Kochi."
)
chatbot(
    user_memory,
    "I am a Computer Science student.",
    "I will remember that you are a Computer Science student."
)
print("\nLater Question:")
print("What do you remember about me?")
print("\nChatbot Answer:")
print(
    "I remember that your name is Vinaya, "
    "you live in Kochi, and you are a Computer Science student."
)
print("\nStored Information:")
print(user_memory.load_memory_variables({})["history"])
