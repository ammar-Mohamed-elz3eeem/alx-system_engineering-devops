#!/usr/bin/python3
"""Queries the Reddit API and returns
the hottest ten posts in subreddit"""
import requests


def top_ten(subreddit):
    """return 10 hot posts in subreddit"""
    url = "https://www.reddit.com"
    res = requests\
        .get("{}/r/{}/hot.json".format(url, subreddit), {"limit": 10},
             headers={"User-Agent": "Ammar"}, allow_redirects=False)
    if res.status_code is not 200:
        print(None)
        return
    posts = res.json().get("data", {}).get("children", [])
    [print(post.get("data", {}).get("title")) for post in posts]
