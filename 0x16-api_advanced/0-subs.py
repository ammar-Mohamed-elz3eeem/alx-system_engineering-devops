#!/usr/bin/python3
"""
Get SubReddit info
"""
import requests


def number_of_subscribers(subreddit):
    """
    query reddit website to get number of subscribers
    to sub redit
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    headers = {"User-Agent": "Ammar"}
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    data = requests.get(url, headers=headers)
    return data.json().get("data", {}).get("subscribers", 0)
