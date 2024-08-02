// Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
const API_KEY = 'YOUR_API_KEY';
const BASE_URL = 'https://api.openweathermap.org/data/2.5/weather';

async function getWeather(city) {
  try {
    const response = await fetch(`${BASE_URL}?q=${city}&units=metric&appid=${API_KEY}`);
    const data = await response.json();
    displayWeather(data);
  } catch (error) {
    console.error('Error fetching weather data:', error);
    displayError('Unable to fetch weather data. Please try again.');
  }
}

function displayWeather(data) {
  // Extract relevant information from the data object
  const { name, main, weather, wind } = data;
  
  // Update your UI with the weather information
  // This is just a basic example - you'll want to expand on this
  document.getElementById('city').textContent = name;
  document.getElementById('temperature').textContent = `${Math.round(main.temp)}°C`;
  document.getElementById('description').textContent = weather[0].description;
  document.getElementById('humidity').textContent = `Humidity: ${main.humidity}%`;
  document.getElementById('wind').textContent = `Wind: ${wind.speed} m/s`;
}

function displayError(message) {
  // Display error message to the user
  document.getElementById('error').textContent = message;
}

// Example usage
getWeather('Bogota');