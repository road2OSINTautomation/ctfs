import requests
username = "micro_bar"
url = "https://www.instagram.com/web/search/topsearch/?context=blended&query=" + username
response = requests.get(url)
response_json = response.json()

for entry in response_json["users"]:
    if entry["user"]["username"] == username:
        print(entry["user"]["pk"])