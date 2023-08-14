#!/usr/bin/python3
"""
Get top ten posts in subreddit
"""
import requests


def count_words(subreddit, word_list, after="", d={}):
    """
    query reddit website to get top ten posts in subreddit
    """
    if not d:
        for word in word_list:
            lower_word = word.lower()
            if lower_word not in d:
                d[lower_word] = 0
    if after is None:
        dSorted = sorted(d.items(), key=lambda entry: (-entry[1], entry[0]))
        for word in dSorted:
            if word[1]:
                print("{}: {}".format(word[0], word[1]))
        return None
    headers = {"User-Agent": "Ammar"}
    params = {
        "after": after,
        "limit": 100
    }
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        return None

    results = res.json().get("data")
    after = results.get("after")
    posts = results.get("children")
    for post in posts:
        title = post.get("data").get("title")
        words = [word.lower() for word in title.split(" ")]
        for word in d.keys():
            d[word] += words.count(word)
    count_words(subreddit, word_list, after, d)
