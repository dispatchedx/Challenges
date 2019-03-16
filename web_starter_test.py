import requests
'''parameters = {
    'lat': 5,
    'lon': 5
}'''

response = requests.get("https://www.reddit.com/dev/api#GET_subreddits_popular.json")
data = response.text
headers = response.headers


print(f'Response: {response}\nData: {data}\nHeaders: {headers}')



# utf-8