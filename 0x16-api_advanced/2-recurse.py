#!/usr/bin/python3
"""Queries the Reddit API and returns
the hottest ten posts in subreddit"""
import requests


def recurse(subreddit, hot_list=[]):
    """return all hot posts in subreddit recursively"""
    url = "https://www.reddit.com"
    headers = {"User-Agent": "Ammar"}
    res = requests.get("{}/r/{}/hot.json".format(url, subreddit),
                       {"limit": 10, "after": len(hot_list)},
                       headers=headers,
                       allow_redirects=False)
    if res.status_code != 200:
        print(None)
        return
    posts = res.json().get("data", {}).get("children", [])
    if len(posts) > 0:
        return recurse(subreddit, hot_list + posts)
    else:
        return posts
