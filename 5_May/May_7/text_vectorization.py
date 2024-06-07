from collections import defaultdict
import numpy as np

def build_vocabulary(data):
    vocabulary = set()
    for text, _ in data:
        words = preprocess(text).split()
        vocabulary.update(words)
    return sorted(vocabulary)

def vectorize(text, vocabulary):
    text = preprocess(text)
    words = text.split()
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1
    return np.array([word_counts[word] for word in vocabulary])

vocabulary = build_vocabulary(data)
