#!/usr/bin/python3
"""Python API Advanced using Reddit API."""

import requests

def recurse(subreddit, hot_list=[], after=None):
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
        post_title = child.get("data", {}).get("title", "")
        if post_title:
            hot_list.append(post_title)

    after = data.get("after")

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
