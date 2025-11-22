#!/usr/bin/python3
"""Return top 10 hot posts for a given subreddit"""
import requests


def top_ten(subreddit):
    """Print the titles of the top 10 hot posts for a subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=10" \
        .format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data')
            if data:
                children = data.get('children', [])
                for child in children:
                    title = child.get('data', {}).get('title')
                    if title:
                        print(title)
            else:
                print(None)
        else:
            print(None)
    except Exception:
        print(None)
