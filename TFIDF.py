import math
import nltk
from nltk.corpus import brown
from nltk.tokenize import word_tokenize
from collections import defaultdict

class TFIDF:
    def __init__(self, corpus) -> None:
        self.corpus = corpus
        self.doc_freq = defaultdict(int)
        
    def compute_doc_freq(self):
        for doc in self.corpus:
            for word in set(doc):
                self.doc_freq[word] = self.doc_freq.get(word, 0) + 1
    
    def tf(self, word, doc):
        return doc.count(word) / len(doc)

    def idf(self, word):
        return math.log(len(self.corpus) / (self.doc_freq.get(word, 0) + 1))
    
    def tf_idf(self, word, doc):
        return self.tf(word, doc) * self.idf(word)


# Preprocess the Brown Corpus
nltk.download('brown')
brown_corpus = [word_tokenize(doc.lower()) for doc in brown.sents()]

# Instantiate TF-IDF class with the preprocessed Brown Corpus
tfidf = TFIDF(brown_corpus)

# Example query
query = "government"

# Calculate TF-IDF for the query in each document
for doc_id, doc in enumerate(brown_corpus):
    score = tfidf.tf_idf(query, doc)
    print(f"TF-IDF score for '{query}' in document {doc_id}: {score}")