print("Load all-MiniLM-L6-v2")
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
print("Model loaded successfully!")


print("Generate Embeddings")
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
sentences = [
    "Artificial Intelligence",
    "Machine Learning",
    "Deep Learning",
    "Python Programming"
]
embeddings = model.encode(sentences)
for sentence, embedding in zip(sentences, embeddings):
    print("\nSentence:", sentence)
    print("Embedding:", embedding)
