import nltk
import string

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Read input text file
with open("sample.txt", "r") as f:
    text = f.read()

print("\nOriginal Text:\n", text)

# 1) Tokenization
tokens = word_tokenize(text)
print("\nTokenization:\n", tokens)

# 2) Punctuation Removal
punct_removed = [w for w in tokens if w not in string.punctuation]
print("\nPunctuation Removed:\n", punct_removed)

# 3) Stop-word Removal
stop_words = set(stopwords.words("english"))
after_stopword = [w for w in punct_removed if w.lower() not in stop_words]
print("\nStop-word Removal:\n", after_stopword)

# 4) Stemming
ps = PorterStemmer()
stemming = [ps.stem(w) for w in after_stopword]
print("\nStemming:\n", stemming)

# 5) Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatization = [lemmatizer.lemmatize(w) for w in after_stopword]
print("\nLemmatization:\n", lemmatization)

print("\n---- DONE ----")
