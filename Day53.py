print("Stem the following words")
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ["Playing", "Working", "Learning", "Running"]
for word in words:
    print(word, "->", stemmer.stem(word))

print("Lemmatize the following words")
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
words = ["Cars", "Children", "Mice", "Dogs"]
for word in words:
    print(word, "->", lemmatizer.lemmatize(word))
