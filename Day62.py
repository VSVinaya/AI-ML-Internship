print("Tokenization")
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
text = "Artificial Intelligence is changing the world."
tokens = word_tokenize(text)
print("Tokens:", tokens)


print("Remove Stop Words")
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
text = "I want to book a train ticket to Delhi."
tokens = word_tokenize(text)
stop_words = set(stopwords.words("english"))
filtered_words = []
for word in tokens:
    if word.lower() not in stop_words:
        filtered_words.append(word)
print("After removing stop words:", filtered_words)


print("Apply Stemming")
import nltk
from nltk.stem import PorterStemmer
nltk.download('punkt')
stemmer = PorterStemmer()
words = ["Playing", "Running", "Reading", "Learning"]
for word in words:
    print(word, "->", stemmer.stem(word.lower()))


print("Build an NLP Chatbot")
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
print("AI College Chatbot")
print("Type 'bye' to exit.")
while True:
    user = input("You: ").lower()
    if user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    tokens = word_tokenize(user)
    if "fee" in tokens or "fees" in tokens:
        print("Bot: The course fee is ₹15,000.")
    elif "duration" in tokens:
        print("Bot: The course duration is 3 months.")
    elif "eligibility" in tokens:
        print("Bot: Students who have completed Higher Secondary education are eligible.")
    elif "contact" in tokens:
        print("Bot: You can contact us at 9876543210.")
    elif "location" in tokens:
        print("Bot: Our college is located in Kochi, Kerala.")
    else:
        print("Bot: Sorry! I couldn't understand.")
