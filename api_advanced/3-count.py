#!/usr/bin/python3
"""
Recursively queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0

    if after is None:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, after)

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    try:
        data = response.json().get("data")
        after = data.get("after")
        children = data.get("children")
        for post in children:
            title = post.get("data").get("title").lower().split()
            for word in counts:
                counts[word] += title.count(word)

    except Exception:
        return

    if after is not None:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))
