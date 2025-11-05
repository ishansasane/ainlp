import spacy

# Load English NLP model (small model)
nlp = spacy.load("en_core_web_sm")

# Sample Input Text
text = """
Apple Inc. was founded by Steve Jobs and Steve Wozniak in California. 
It is one of the biggest tech companies in the world. 
In 2023, Apple reached a market value of 3 trillion dollars.
"""

# Process the text
doc = nlp(text)

print("\n===== INPUT TEXT =====")
print(text)

print("\n===== NAMED ENTITIES DETECTED =====")
for ent in doc.ents:
    print(f"{ent.text:30} ---> {ent.label_}")
