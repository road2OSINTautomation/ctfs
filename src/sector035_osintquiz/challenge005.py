import requests
import datetime

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4476.0 " \
             "Safari/537.36 "
HEADERS = ({'User-Agent': user_agent,
            'Accept-Language': 'en-US, en;q=0.8'})

tiktok_url = "https://www.tiktok.com/@aizhana_or/video/6754400110869859590"

response = requests.get(tiktok_url, headers=HEADERS)
response_string = str(response.content)
create_time = response_string.split('createTime":')[1].split(",")[0]

print("Tiktok url:\t\t\t\t\t\t\t" + tiktok_url)
print("CreateTime (UNIX Timestmap):\t\t" + create_time)
print("CreateTime (humanreadable):\t\t\t" +
      datetime.datetime.fromtimestamp(int(create_time)).strftime('%Y-%m-%d %H:%M:%S'))
