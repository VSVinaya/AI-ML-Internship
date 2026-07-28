print("Create the 5-sentence dataset")
sentences = [
    ["i", "love", "ai"],
    ["ai", "is", "amazing"],
    ["i", "love", "python"],
    ["python", "is", "powerful"],
    ["ai", "and", "python", "are", "useful"]
]
print("Dataset:")
print(sentences)


print("Train the Word2Vec model")
from gensim.models import Word2Vec
sentences = [
    ["i", "love", "ai"],
    ["ai", "is", "amazing"],
    ["i", "love", "python"],
    ["python", "is", "powerful"],
    ["ai", "and", "python", "are", "useful"]
]
model = Word2Vec(
    sentences,
    vector_size=50,
    window=3,
    min_count=1
)
print("Word2Vec model trained successfully!")


print("Print a word vector")
print("\nVector for 'ai':")
print(model.wv["ai"])

print("Find similar words")
print("\nWords similar to 'ai':")
print(model.wv.most_similar("ai"))

