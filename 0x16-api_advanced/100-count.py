#!/usr/bin/python3
"""count keywords in hot post titles in subreddit"""
import re
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


def count_words(subreddit, word_list, obj={}):
    """return dict with how many times every word repeated in title"""
    posts = recurse(subreddit, [], "", 0)
    if posts is None or len(posts) <= 0:
        return None
    posts = list(map(lambda post: post.get("data", {}).get("title"), posts))
    all_titles = " - ".join(posts)
    final = obj
    occurances = len(re.findall(word_list[0], all_titles, re.IGNORECASE))
    if occurances > 0:
        final[word_list[0].lower()] = occurances

    if (len(word_list) > 1):
        return count_words(subreddit, word_list[1:], final)
    print_dictionary_ordered(final)


def print_dictionary_ordered(final):
    [print("{}: {}".format(word, count)) for
     (word, count) in sorted(final.items(),
                             key=lambda post: post[1],
                             reverse=True)]
