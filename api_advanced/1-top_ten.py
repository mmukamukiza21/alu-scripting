#!/usr/bin/python3
"""Script that fetches the top 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the 10 hottest posts on a given subreddit.
    If an invalid subreddit is given, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get("data", {}).get("children", [])
    for post in posts:
        print(post.get("data", {}).get("title"))
