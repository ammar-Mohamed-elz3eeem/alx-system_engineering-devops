#!/usr/bin/python3
"""
module to save employees tasks in .csv file format
"""
import json
from sys import argv
import urllib.request


def get_emp(empid=None):
    if isinstance(empid, int):
        fd = urllib.request.urlopen(
            "https://jsonplaceholder.typicode.com/users/{}"
            .format(empid))
        with fd:
            return json.loads(fd.read())


def get_emp_tasks(empid=None):
    if isinstance(empid, int):
        fd = urllib.request.urlopen(
            "https://jsonplaceholder.typicode.com/users\
/{}/todos".format(empid))
        with fd:
            return json.loads(fd.read())


if __name__ == "__main__":
    empid = int(argv[1])
    empinfo = get_emp(empid)
    emptodos = get_emp_tasks(empid)
    file = open("{}.csv".format(empid), "a+")
    data = list(map(lambda x: file.write(
        "\"{}\",\"{}\",\"{}\",\"{}\"\n"
        .format(
            x["userId"],
            empinfo["username"],
            str(x["completed"]).capitalize(),
            x["title"]
        )), emptodos))
