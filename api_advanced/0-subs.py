#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Returns total subscribers of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "my-reddit-script/1.0"}

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=5
        )

        if response.status_code != 200:
            return 0

        data = response.json()

        subs = data.get("data", {}).get("subscribers")

        return subs

    except Exception:
        return 0
