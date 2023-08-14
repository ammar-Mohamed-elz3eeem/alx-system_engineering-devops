#!/usr/bin/python3
"""
Get top ten posts in subreddit
"""
import requests


def top_ten(subreddit):
    """
    query reddit website to get top ten posts in subreddit
    """
    headers = {"User-Agent": "Ammar"}
    params = {"limit": 10}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if (res.status_code == 404):
        print("None")
        return
    data = res.json().get("data").get("children")
    [print(row.get("data").get("title")) for row in data]
