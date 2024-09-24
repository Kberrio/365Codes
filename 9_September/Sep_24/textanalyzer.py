import re
from collections import Counter

def analyze_text(text):
    # Convert to lowercase and remove punctuation
    clean_text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Split into words
    words = clean_text.split()
    
    # Count words
    word_count = len(words)
    
    # Count unique words
    unique_words = len(set(words))
    
    # Find most common words
    word_freq = Counter(words)
    most_common = word_freq.most_common(5)
    
    # Calculate average word length
    avg_word_length = sum(len(word) for word in words) / word_count
    
    # Count sentences
    sentence_count = len(re.findall(r'\w+[.!?]', text))
    
    return {
        'word_count': word_count,
        'unique_words': unique_words,
        'most_common': most_common,
        'avg_word_length': avg_word_length,
        'sentence_count': sentence_count
    }

# Example usage
sample_text = """
Python is an amazing programming language. It's versatile, easy to learn, and powerful.
Many developers love using Python for various projects, from web development to data analysis.
Python's simplicity doesn't compromise its ability to solve complex problems efficiently.
"""

result = analyze_text(sample_text)
print("Text Analysis Results:")
print(f"Word Count: {result['word_count']}")
print(f"Unique Words: {result['unique_words']}")
print(f"Most Common Words: {result['most_common']}")
print(f"Average Word Length: {result['avg_word_length']:.2f}")
print(f"Sentence Count: {result['sentence_count']}")