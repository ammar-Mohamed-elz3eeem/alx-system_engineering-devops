#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ return number of subscribers on subreddit """
    if subreddit is None or type(subreddit) is not str:
        return 0
    req = requests\
        .get("https://www.reddit.com/r/{}/about.json"
             .format(subreddit), headers={"User-Agent": "Ammar"})\
        .json()
    return req.get("data", {}).get("subscribers", 0)
