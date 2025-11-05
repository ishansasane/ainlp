import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')

# Sample Text (you may replace with Twitter data)
text = """
Natural Language Processing is interesting.
NLP helps computers understand human language.
"""

print("\n==== ORIGINAL TEXT ====\n")
print(text)

# Tokenization
tokens = word_tokenize(text.lower())

print("\n==== TOKENS ====\n")
print(tokens)

# ----------- BIGRAMS ------------
bigrams = list(ngrams(tokens, 2))
bigram_counts = Counter(bigrams)

print("\n==== BI-GRAMS ====\n")
for token in bigrams:
    print(token)

print("\n==== BI-GRAM FREQUENCY ====\n")
for item, cnt in bigram_counts.items():
    print(item, ":", cnt)

# ----------- TRIGRAMS ------------
trigrams = list(ngrams(tokens, 3))
trigram_counts = Counter(trigrams)

print("\n==== TRI-GRAMS ====\n")
for token in trigrams:
    print(token)

print("\n==== TRI-GRAM FREQUENCY ====\n")
for item, cnt in trigram_counts.items():
    print(item, ":", cnt)
