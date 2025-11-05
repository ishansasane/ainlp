import spacy
import string

nlp = spacy.load("en_core_web_sm")

# Read input text
with open("sample.txt", "r") as f:
    text = f.read()

print("\nOriginal Text:\n", text)

doc = nlp(text)

# 1) Tokenization
tokens = [token.text for token in doc]
print("\nTokenization:\n", tokens)

# 2) Punctuation Removal
punct_removed = [token.text for token in doc if token.text not in string.punctuation]
print("\nPunctuation Removed:\n", punct_removed)

# 3) Stop word removal
stop_removed = [token.text for token in doc if not token.is_stop]
print("\nStop-word Removal:\n", stop_removed)

# 4) Lemmatization
lemmas = [token.lemma_ for token in doc]
print("\nLemmatization:\n", lemmas)

# 5) Stemming (spaCy doesn't support directly → optional: use NLTK)
from nltk.stem import PorterStemmer
import nltk
nltk.download("punkt")

stemmer = PorterStemmer()
stemming = [stemmer.stem(token.text) for token in doc]
print("\nStemming:\n", stemming)

print("\n---- DONE ----")
