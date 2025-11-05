import spacy
from spacy import displacy

# Load English model
nlp = spacy.load("en_core_web_sm")

text = "Apple was founded by Steve Jobs in California."

doc = nlp(text)

# Print dependencies
print("\n== DEPENDENCY RELATIONS ==")
for token in doc:
    print(token.text, " --> ", token.dep_, " --> ", token.head.text)

# Visualize dependency tree in browser
displacy.serve(doc, style="dep")
