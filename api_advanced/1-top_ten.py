#!/usr/bin/python3
"""Return top 10 hot posts for a given subreddit"""
import requests


def top_ten(subreddit):
    """Print the titles of the top 10 hot posts for a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {'limit': 10}
    
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get('data')
        children = data.get('children')
        for child in children:
            print(child.get('data').get('title'))
    else:
        print(None)
