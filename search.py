import re
STOP_WORDS = {"the", "a", "an", "and", "on", "in", "of", "to", "is", "it"}

def stem(word):
    for suffix in ("ing", "ed", "es", "s"):
                if word.endswith(suffix) and len(word) - len(suffix) >= 3:
                              return word[:-len(suffix)]
    return word
       
def tokenize(text):
    text = text.lower()
    words = re.findall(r"[a-z0-9]+", text)
    words = [w for w in words if w not in STOP_WORDS]
    words = [stem (w) for w in words]
    return words

def build_index(docs):
    index = {}
    for doc_id, text in docs.items():
        words = tokenize(text)
        for word in words:
            if word not in index:
                index[word] = []
            if doc_id not in index[word]:
                index[word].append(doc_id)
    return index

def search(index, query):
    terms = tokenize(query)
    if not terms:
        return []
    results = set(index.get(terms[0], []))
    for term in terms[1:]:
        results = results & set(index.get(term, []))
    return sorted(results)

docs = {
    1: "the cat sat on the mat",
    2: "the dog sat on the log",
    3: "cats and dogs",
}

index = build_index(docs)
print(stem("cats"), stem("walking"), stem("walked"), stem("bus"), stem("glasses"))
print(search(index, "cat"))
print(search(index, "dog"))