#!/usr/bin/python3
"""
This contains the `top_ten` function for printing
the titles of the 10 hottest posts on a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    user_agent = "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    headers = {
        "User-Agent": user_agent
        }

    params = {
        "limit": 10
        }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return

    results = response.json().get("data")
    [print(child.get("data").get("title"))
     for child in results.get("children")]
