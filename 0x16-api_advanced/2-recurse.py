#!/usr/bin/python3
"""
This includes the'recurse' method for retrieving
a list of all hot post titles on a specific subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Returns a list of titles of all hot posts on a specific subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    user_agent = "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    headers = {
        "User-Agent": user_agent
        }

    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for child in results.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
