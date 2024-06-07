import requests

def get_weather(api_key, city):
    """Fetches weather data for a given city using OpenWeatherMap API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        weather_description = data['weather'][0]['description']
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature} Kelvin")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description}")
    else:
        print("Error in the HTTP request")

# Example usage
api_key = "YOUR_API_KEY_HERE"
city = "London"
get_weather(api_key, city)