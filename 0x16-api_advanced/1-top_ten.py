#!/usr/bin/python3
"""
Get top ten posts in subreddit
"""
import requests


def top_ten(subreddit):
    """
    query reddit website to get top ten posts in subreddit
    """
    if subreddit is None or type(subreddit) is not str:
        return None
    headers = {"User-Agent": "Ammar"}
    params = {"limit": 10}
    url = "http://www.reddit.com/r/{}/hot/.json".format(subreddit)
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if (res.status_code == 404):
        print("None")
        return
    data = res.json().get("data", {}).get("children", [])
    mapped_data = map(lambda data: data.get("data", {}).get("title", ""), data)
    [print(row) for row in list(mapped_data)]
