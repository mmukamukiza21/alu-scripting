#!/usr/bin/python3
"""Module that prints the titles of the 10 hottest posts on a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyRedditClient/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get("data", {}).get("children", [])
    if not posts:
        print(None)
        return

    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
