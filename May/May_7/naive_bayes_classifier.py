class NaiveBayesClassifier:
    def __init__(self):
        self.log_prior = {}
        self.log_likelihood = {}
        self.vocabulary = []

    def train(self, data, vocabulary):
        self.vocabulary = vocabulary
        label_counts = defaultdict(int)
        word_counts = {label: defaultdict(int) for label, _ in data}

        # Count labels and words frequencies
        for text, label in data:
            label_counts[label] += 1
            for word, count in zip(vocabulary, vectorize(text, vocabulary)):
                word_counts[label][word] += count

        # Calculate log prior
        total_docs = sum(label_counts.values())
        self.log_prior = {label: np.log(count / total_docs) for label, count in label_counts.items()}

        # Calculate log likelihood
        for label in label_counts:
            total_count = sum(word_counts[label].values()) + len(vocabulary)
            self.log_likelihood[label] = {word: np.log((word_counts[label][word] + 1) / total_count)
                                          for word in vocabulary}

    def predict(self, text):
        vector = vectorize(text, self.vocabulary)
        scores = {}
        for label in self.log_prior:
            scores[label] = self.log_prior[label] + sum(vector * np.array([self.log_likelihood[label][word]
                                                                           for word in self.vocabulary]))
        return max(scores, key=scores.get)

# Training the classifier
classifier = NaiveBayesClassifier()
classifier.train(data, vocabulary)
