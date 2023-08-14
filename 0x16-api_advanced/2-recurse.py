#!/usr/bin/python3
"""
Get top ten posts in subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    query reddit website to get top ten posts in subreddit
    """
    headers = {"User-Agent": "Ammar"}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        return None
    results = res.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    [hot_list.append(row.get("data").get("title"))
     for row in results.get("children")]
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return len(hot_list)
