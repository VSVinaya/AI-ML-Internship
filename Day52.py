#Text preprocessing

print("Tokenize")
text = "I love Machine Learning"
tokens = text.split()
print(tokens)

print("Convert to lowercase")
text = "HELLO WORLD"
print(text.lower())

print("Remove punctuation")
import string
text = "Python!!! is Awesome???"
clean_text = text.translate(str.maketrans('', '', string.punctuation))
print(clean_text)

print("Clean the sentence")
import re
text = "AI 2025 is AMAZING!!!"
text = text.lower()
text = re.sub(r'[^a-zA-Z\s]', '', text)
print(text)


