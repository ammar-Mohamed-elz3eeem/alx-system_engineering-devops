#!/usr/bin/python3
"""
Queries the Reddit API and returns
the hottest ten posts in subreddit
"""
import requests


def top_ten(subreddit):
    if subreddit is None or type(subreddit) is not str:
        print(None)
        return
    url = "https://www.reddit.com"
    posts = requests\
        .get("{}/r/{}/hot.json".format(url, subreddit), {"limit": 10},
             headers={"User-Agent": "Ammar"}, allow_redirects=False)\
        .json().get("data", {}).get("children", [])
    [print(post.get("data", {}).get("title")) for post in posts]
