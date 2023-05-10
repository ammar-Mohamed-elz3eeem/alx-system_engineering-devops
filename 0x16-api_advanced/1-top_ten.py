#!/usr/bin/python3
"""Queries the Reddit API and returns hot 10 posts"""
import requests


def top_ten(subreddit):
    """return 10 hot posts in subreddit"""
    url = "https://www.reddit.com"
    headers = {"User-Agent": "Ammar"}
    res = requests.get("{}/r/{}/hot/.json".format(url, subreddit),
                       params={"limit": 10},
                       headers=headers,
                       allow_redirects=False)
    if res.status_code == 404:
        print(None)
        return
    posts = res.json().get("data").get("children")
    [print(post.get("data").get("title")) for post in posts]
