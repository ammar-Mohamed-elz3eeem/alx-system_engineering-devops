#!/usr/bin/python3
"""
module to save employees tasks in .json file format
"""
import json
from requests import get
from sys import argv


if __name__ == "__main__":
    user_id = int(argv[1])
    url = "https://jsonplaceholder.typicode.com/"
    user = get("{}users/{}".format(url, user_id)).json()
    username = user.get("username")
    todos = get("{}todos".format(url), params={"userId": user_id}).json()
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        } for t in todos]}, jsonfile)
