print("Create TF-IDF Vectors")
from sklearn.feature_extraction.text import TfidfVectorizer
documents = [
    "AI is amazing",
    "AI is powerful",
    "Machine learning is amazing"
]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)
print("TF-IDF Matrix:")
print(X.toarray())
print("\nVocabulary:")
print(vectorizer.get_feature_names_out())


print("Compare BoW and TF-IDF:")
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
documents = [
    "AI is amazing",
    "AI is powerful",
    "Machine learning is amazing"
]
# Bag of Words
bow_vectorizer = CountVectorizer()
bow = bow_vectorizer.fit_transform(documents)
print("Bag of Words Vocabulary:")
print(bow_vectorizer.get_feature_names_out())
print("\nBag of Words Matrix:")
print(bow.toarray())
# TF-IDF
tfidf_vectorizer = TfidfVectorizer()
tfidf = tfidf_vectorizer.fit_transform(documents)
print("\nTF-IDF Vocabulary:")
print(tfidf_vectorizer.get_feature_names_out())
print("\nTF-IDF Matrix:")
print(tfidf.toarray())
