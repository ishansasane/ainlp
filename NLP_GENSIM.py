from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from gensim.models import Word2Vec
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

# Sample documents
documents = [
    "Natural Language Processing makes machines understand text.",
    "Text mining and NLP are key techniques in data science.",
    "Word2Vec creates vector representation of words."
]

print("\n===== INPUT DOCUMENTS =====")
for d in documents:
    print("-", d)

# ---------------------------------------------------------
# 1) Bag-of-Words (BoW)
# ---------------------------------------------------------
vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform(documents)

print("\n===== BAG OF WORDS (BoW) =====")
print("Feature names:")
print(vectorizer.get_feature_names_out())
print("\nBoW Matrix:")
print(bow_matrix.toarray())

# ---------------------------------------------------------
# 2) TF-IDF
# ---------------------------------------------------------
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

print("\n===== TF-IDF OUTPUT =====")
print("Feature names:")
print(tfidf_vectorizer.get_feature_names_out())
print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())

# ---------------------------------------------------------
# 3) Word2Vec
# ---------------------------------------------------------
# Tokenize text
tokenized_docs = [word_tokenize(doc.lower()) for doc in documents]

# Create Word2Vec model
model = Word2Vec(sentences=tokenized_docs, vector_size=50, window=5, min_count=1, workers=4)

print("\n===== WORD2VEC (VECTOR EMBEDDINGS) =====")
for word in ["natural", "text", "nlp", "words"]:
    print(f"\nVector for '{word}':")
    print(model.wv[word])

# Similarity example
print("\nSimilarity between 'text' and 'nlp':")
print(model.wv.similarity("text", "nlp"))
