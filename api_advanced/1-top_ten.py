#!/usr/bin/python3
"""Return the number of subscribers of a given subreddit"""

import requests

def top_ten(subreddit):
    """Returns top ten hot posts on subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "my-reddit-script/1.0"}

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=5
        )

        if response.status_code != 200:
            print(None)
            return None

        data = response.json().get("data", {})
        children = data.get("children", [])

        for child in children:
            post_title = child.get("data", {}).get("title")

            if post_title:
                print(post_title)

    except Exception:
        print(None)
