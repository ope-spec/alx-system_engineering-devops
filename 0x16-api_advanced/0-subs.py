#!/usr/bin/python3
"""
The `number_of_subscribers` function for querying the Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    user_agent = '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'
    headers = {'User-Agent': user_agent}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
