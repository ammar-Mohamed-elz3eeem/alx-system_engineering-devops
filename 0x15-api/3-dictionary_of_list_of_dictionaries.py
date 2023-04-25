#!/usr/bin/python3
"""
module to save employees tasks in .json file format
"""
import json
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = get("{}/users".format(url)).json()
    data = dict()
    for u in users:
        utasks = get("{}/todos".format(url),
                     params={"userId": u.get("id")}).json()
        data[u.get("id")] = [{
            "username": u.get("username"),
            "task": task.get("title"),
            "completed": task.get("completed")
        } for task in utasks]
    with open("todo_all_employees.json", mode="w") as jsonfile:
        json.dump(data, jsonfile)
