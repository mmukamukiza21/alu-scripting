#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    
    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )
        
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if posts:
                for post in posts:
                    print(post.get('data', {}).get('title'))
            else:
                print(None)
        else:
            print(None)
    except Exception:
        print(None)
