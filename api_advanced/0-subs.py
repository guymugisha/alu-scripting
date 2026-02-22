#!/usr/bin/python3
# Author: Guy De Jesus
"""Return the number of subscribers of a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """function that fetches number_of_subscribers"""
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    HEADERS = {"User-Agent": "GuyDeJesus-Reddit-Script/1.0"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        return RESPONSE.json().get("data").get("subscribers")

    except Exception:
        return 0
