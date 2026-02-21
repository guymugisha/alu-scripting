#!/usr/bin/python3
"""
This recursive function that queries the Reddit API, 
parses the title of all hot articles, and prints a sorted count of given keywords
"""

import requests

def count_words(subreddit, word_list, after=None, counts=None, frequency=None):
    if counts is None:
        counts = {}
        frequency = {}

        for word in word_list:
            word = word.lower()
            frequency[word] = frequency.get(word, 0) + 1
            counts[word] = 0

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "my-reddit-script/1.0"}
    params = {"after": after} if after else {}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False,
        timeout=5
    )

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])

    for child in children:
        post_title = child.get("data", {}).get("title", "").lower()
        words = post_title.split()

        for word in words:
            if word in counts:
                counts[word] += 1

    after = data.get("after")

    if after is None:
        return count_words(subreddit, word_list, after, counts, frequency)

    final_results = {}

    for word in counts:
        total = counts[word] * frequency[word]
        if total > 0:
            final_results[word] = total

    sorted_results = sorted(
        final_results.items(),
        key=lambda x: (-x[1], x[0])
    )

    for word, count in sorted_results:
        print(f"{word}: {count}")

    return None
