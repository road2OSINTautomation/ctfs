import requests

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4476.0 " \
             "Safari/537.36 "
HEADERS = ({'User-Agent': user_agent,
            'Accept-Language': 'en-US, en;q=0.8'})

profile_url = "https://www.facebook.com/SilensecGroup"
response = requests.get(profile_url, headers=HEADERS)
response_string = str(response.content)

profile_id = response_string.split('entity_id":"')[1].split('"}')[0]
print("Facebook profile:\t" + profile_url)
print("ID:\t\t\t\t\t" + profile_id)
