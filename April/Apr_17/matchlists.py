import requests
from requests.auth import HTTPBasicAuth

# Authentication
auth = HTTPBasicAuth('your_access_id', 'your_access_key')

# Get all match lists
response = requests.get('https://api.us2.sumologic.com/api/sec/v1/match-lists', auth=auth)
match_lists = response.json()

# Update each match list
for match_list in match_lists:
    update_response = requests.put(
        f'https://api.us2.sumologic.com/api/sec/v1/match-lists/{match_list["id"]}',
        auth=auth,
        json={
            "name": match_list["name"] + " Updated",
            "description": match_list["description"] + " Updated",
            "entries": match_list["entries"]
        }
    )
    print(update_response.status_code)
