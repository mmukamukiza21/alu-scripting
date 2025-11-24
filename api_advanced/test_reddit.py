#!/usr/bin/python3
import requests

headers = {
    'User-Agent': 'linux:com.example.myredditapp:v1.0.0 (by /u/mmukamukiza21)'
}
url = "https://www.reddit.com/r/programming/hot.json"
params = {'limit': 10}

response = requests.get(url, headers=headers, params=params, timeout=10)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text[:200]}")
