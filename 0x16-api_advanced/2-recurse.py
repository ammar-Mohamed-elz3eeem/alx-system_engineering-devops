#!/usr/bin/python3
"""Query in subreddit recursivly"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """return all hot posts in subreddit recursively"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Mero"}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    res = requests.get(url,
                       params=params,
                       headers=headers,
                       allow_redirects=False)
    if res.status_code != 200:
        return None
    data = res.json().get("data", {})
    count += data.get("dist", 0)
    after = data.get("after")
    posts = data.get("children", [])

    for post in posts:
        hot_list.append(post)
    
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
