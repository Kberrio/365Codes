import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import pairwise_distances_argmin

class KMeans:
    def __init__(self, n_clusters=3, max_iter=100, random_state=None):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.random_state = random_state
        self.centroids = None

    def initialize_centroids(self, X):
        np.random.seed(self.random_state)
        random_idx = np.random.permutation(X.shape[0])
        centroids = X[random_idx[:self.n_clusters]]
        return centroids
    
    def assign_clusters(self, X):
        return pairwise_distances_argmin(X, self.centroids)
    
    def update_centroids(self, X, labels):
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(self.n_clusters)])
        return new_centroids
    
    def fit(self, X):
        self.centroids = self.initialize_centroids(X)
        for i in range(self.max_iter):
            labels = self.assign_clusters(X)
            new_centroids = self.update_centroids(X, labels)
            if np.all(self.centroids == new_centroids):
                break
            self.centroids = new_centroids
        self.labels = labels

def main():
    # Load Iris dataset
    iris = load_iris()
    X = iris.data
    
    # Initialize and fit KMeans
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(X)
    
    # Output the results
    print("Centroids:")
    print(kmeans.centroids)
    print("\nFirst 10 labels:")
    print(kmeans.labels[:10])

if __name__ == "__main__":
    main()
