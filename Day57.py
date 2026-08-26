print("Load the GloVe model")
import gensim.downloader as api
model = api.load("glove-wiki-gigaword-50")
print("GloVe model loaded successfully!")

print("Print the vector for king")
import gensim.downloader as api
model = api.load("glove-wiki-gigaword-50")
print(model["king"])

print("Find the top 5 similar words for computer")
import gensim.downloader as api
model = api.load("glove-wiki-gigaword-50")
print(model.most_similar("computer", topn=5))
