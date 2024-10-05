import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie data
movies_data = {
    'title': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Forrest Gump'],
    'genre': ['Drama', 'Crime, Drama', 'Action, Crime, Drama', 'Crime, Drama', 'Drama, Romance'],
    'director': ['Frank Darabont', 'Francis Ford Coppola', 'Christopher Nolan', 'Quentin Tarantino', 'Robert Zemeckis'],
    'description': [
        'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
        'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
        'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
        'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
        'The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart.'
    ]
}

df = pd.DataFrame(movies_data)

# Combine relevant features
df['features'] = df['genre'] + ' ' + df['director'] + ' ' + df['description']

# Create TF-IDF matrix
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['features'])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get movie recommendations
def get_recommendations(title, cosine_sim=cosine_sim, df=df):
    idx = df.index[df['title'] == title].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Top 5 similar movies
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]

# Example usage
movie_title = "The Dark Knight"
recommendations = get_recommendations(movie_title)
print(f"Recommendations for '{movie_title}':")
print(recommendations)

# Function to add a new movie
def add_movie(title, genre, director, description):
    new_movie = pd.DataFrame({
        'title': [title],
        'genre': [genre],
        'director': [director],
        'description': [description],
        'features': [f"{genre} {director} {description}"]
    })
    return pd.concat([df, new_movie], ignore_index=True)

# Example: Add a new movie
new_df = add_movie(
    "Inception",
    "Action, Adventure, Sci-Fi",
    "Christopher Nolan",
    "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O."
)

# Update similarity matrix
new_tfidf_matrix = tfidf.fit_transform(new_df['features'])
new_cosine_sim = cosine_similarity(new_tfidf_matrix, new_tfidf_matrix)

# Get recommendations for the new movie
new_recommendations = get_recommendations("Inception", new_