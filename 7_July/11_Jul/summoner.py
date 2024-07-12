import requests
import os

# Set up your API key
API_KEY = os.environ.get('RIOT_API_KEY')  # Store your API key as an environment variable for security

# Base URLs
BASE_URL = "https://na1.api.riotgames.com"  # Change region as needed
SUMMONER_URL = f"{BASE_URL}/lol/summoner/v4/summoners/by-name/"
MATCH_URL = f"{BASE_URL}/lol/match/v5/matches/by-puuid/"

def get_summoner_info(summoner_name):
    url = SUMMONER_URL + summoner_name
    headers = {"X-Riot-Token": API_KEY}
    response = requests.get(url, headers=headers)
    return response.json()

def get_recent_matches(puuid, count=5):
    url = MATCH_URL + f"{puuid}/ids?count={count}"
    headers = {"X-Riot-Token": API_KEY}
    response = requests.get(url, headers=headers)
    return response.json()

def main():
    summoner_name = input("Enter summoner name: ")
    summoner_info = get_summoner_info(summoner_name)
    
    if 'status' in summoner_info and summoner_info['status']['status_code'] == 404:
        print(f"Summoner '{summoner_name}' not found.")
        return
    
    print(f"Summoner Info for {summoner_name}:")
    print(f"Level: {summoner_info['summonerLevel']}")
    print(f"Account ID: {summoner_info['accountId']}")
    
    recent_matches = get_recent_matches(summoner_info['puuid'])
    print(f"\nRecent Matches for {summoner_name}:")
    for match_id in recent_matches:
        print(match_id)

if __name__ == "__main__":
    main()