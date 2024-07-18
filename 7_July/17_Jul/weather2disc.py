import requests
import discord
from discord.ext import tasks

WEATHER_API_KEY = 'your_weather_api_key'
DISCORD_TOKEN = 'your_discord_bot_token'
CITY = 'New York'

client = discord.Client()

@tasks.loop(hours=1)
async def check_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_API_KEY}"
    response = requests.get(url).json()
    
    if response['weather'][0]['main'] in ['Thunderstorm', 'Rain', 'Snow']:
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(f"Severe weather alert in {CITY}: {response['weather'][0]['description']}")

@client.event
async def on_ready():
    check_weather.start()

client.run(DISCORD_TOKEN)
#Changes may be subject to APIs