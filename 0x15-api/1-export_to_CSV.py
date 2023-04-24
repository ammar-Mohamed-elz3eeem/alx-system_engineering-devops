#!/usr/bin/python3
"""
module to save employees tasks in .csv file format
"""
import csv
import json
from requests import get
from sys import argv


if __name__ == "__main__":
    empid = int(argv[1])
    url = "https://jsonplaceholder.typicode.com/"
    empinfo = get("{}users/{}".format(url, empid)).json()
    emptodos = get("{}todos".format(url), {"userId":empid}).json()
    with open("{}.csv".format(empid), "w", newline="") as fd:
        writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
        [writer.writerow([row.get("userId"),
                          empinfo.get("username"), row.get("completed"), row.get("title")])
         for row in emptodos]
