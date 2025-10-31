#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests


def top_ten(subreddit):
    """Return number of subscribers if @subreddit is valid subreddit.
    if not return 0."""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://api.reddit.com/r/{}/hot.json?limit=10".format(
        subreddit
    )
    response = requests.get(
        subreddit_url,
        headers=headers,
        allow_redirects=False
    )
    if response.status_code == 200:
        json_data = response.json()
        children = json_data.get('data', {}).get('children', [])
        for child in children:
            print(child.get('data', {}).get('title'))
    else:
        print(None)
