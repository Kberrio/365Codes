const API_KEY = 'YOUR_TMDB_API_KEY';
const BASE_URL = 'https://api.themoviedb.org/3';
const IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/w500';

const searchInput = document.getElementById('search-input');
const searchButton = document.getElementById('search-button');
const movieDetails = document.getElementById('movie-details');
const recommendationList = document.getElementById('recommendation-list');
const trendingList = document.getElementById('trending-list');

searchButton.addEventListener('click', searchMovie);

async function searchMovie() {
    const query = searchInput.value;
    if (!query) return;

    try {
        const response = await fetch(`${BASE_URL}/search/movie?api_key=${API_KEY}&query=${query}`);
        const data = await response.json();
        if (data.results.length > 0) {
            displayMovieDetails(data.results[0]);
            getRecommendations(data.results[0].id);
        } else {
            movieDetails.innerHTML = 'No movies found.';
        }
    } catch (error) {
        console.error('Error searching for movie:', error);
    }
}

function displayMovieDetails(movie) {
    movieDetails.innerHTML = `
        <h2>${movie.title}</h2>
        <img src="${IMAGE_BASE_URL}${movie.poster_path}" alt="${movie.title}" style="max-width: 200px;">
        <p>${movie.overview}</p>
        <p>Rating: ${movie.vote_average}/10</p>
        <p>Release Date: ${movie.release_date}</p>
    `;
}

async function getRecommendations(movieId) {
    try {
        const response = await fetch(`${BASE_URL}/movie/${movieId}/recommendations?api_key=${API_KEY}`);
        const data = await response.json();
        displayMovieList(data.results.slice(0, 5), recommendationList);
    } catch (error) {
        console.error('Error getting recommendations:', error);
    }
}

function displayMovieList(movies, container) {
    container.innerHTML = '';
    movies.forEach(movie => {
        const movieCard = document.createElement('div');
        movieCard.classList.add('movie-card');
        movieCard.innerHTML = `
            <img src="${IMAGE_BASE_URL}${movie.poster_path}" alt="${movie.title}">
            <h3>${movie.title}</h3>
            <p>Rating: ${movie.vote_average}/10</p>
        `;
        container.appendChild(movieCard);
    });
}

async function getTrendingMovies() {
    try {
        const response = await fetch(`${BASE_URL}/trending/movie/week?api_key=${API_KEY}`);
        const data = await response.json();
        displayMovieList(data.results.slice(0, 5), trendingList);
    } catch (error) {
        console.error('Error getting trending movies:', error);
    }
}

// Load trending movies on page load
window.addEventListener('load', getTrendingMovies);