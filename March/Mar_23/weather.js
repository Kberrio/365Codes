const axios = require('axios');

// Your OpenWeatherMap API key
const apiKey = 'YOUR_API_KEY'; // Replace this with your actual API key

// Function to fetch weather data
async function getWeather(city) {
    try {
        const response = await axios.get(`http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`);
        const weatherData = response.data;
        return weatherData;
    } catch (error) {
        console.error('Error fetching weather:', error);
        return null;
    }
}

// Function to display weather information
function displayWeather(weather) {
    if (!weather) {
        console.log('Weather data not available.');
        return;
    }

    console.log(`Weather in ${weather.name}:`);
    console.log(`Temperature: ${weather.main.temp}°C`);
    console.log(`Description: ${weather.weather[0].description}`);
    console.log(`Humidity: ${weather.main.humidity}%`);
    console.log(`Wind Speed: ${weather.wind.speed} m/s`);
}

// Main function
async function main() {
    const city = 'London'; // Change this to the desired city
    const weather = await getWeather(city);
    displayWeather(weather);
}

main();
