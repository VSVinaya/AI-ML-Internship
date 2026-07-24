print("Implement CountVectorizer")
from sklearn.feature_extraction.text import CountVectorizer
sentences = [
    "AI is powerful",
    "AI is amazing"
]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)
print("Vocabulary:")
print(vectorizer.get_feature_names_out())
print("\nBoW Matrix:")
print(X.toarray())

print("Generate BoW vectors for 5 sentences")
from sklearn.feature_extraction.text import CountVectorizer
sentences = [
    "I love AI",
    "AI is powerful",
    "Machine Learning is fun",
    "Python is easy",
    "AI and Python are useful"
]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)
print("Vocabulary:")
print(vectorizer.get_feature_names_out())
print("\nBoW Matrix:")
print(X.toarray())

