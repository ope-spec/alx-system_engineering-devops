#!/usr/bin/python3
"""
This module contains the `count_words` function for querying
the Reddit API recursively and counting keywords in post titles.
"""

import requests


def count_words(subreddit, word_list, after='', word_dict=None):
    """
    Queries the Reddit API, parses the titles of hot articles,
    and prints a sorted count of given keywords.
    """

    if word_dict is None:
        word_dict = {word.lower(): 0 for word in word_list}

    if after is None:
        sorted_word_dict = sorted(word_dict.items(),
                                  key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_dict:
            if count > 0:
                print(f'{word}: {count}')
        return

    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    headers = {'user-agent': 'redquery'}
    parameters = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers,
                            params=parameters, allow_redirects=False)

    if response.status_code != 200:
        return

    try:
        data = response.json()['data']
        posts = data['children']
        after = data['after']

        for post in posts:
            title = post['data']['title'].lower()
            for word in word_dict:
                word_dict[word] += title.split(' ').count(word)

    except Exception:
        return

    count_words(subreddit, word_list, after, word_dict)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        keywords = sys.argv[2:]
        count_words(subreddit, keywords)
