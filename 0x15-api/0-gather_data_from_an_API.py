#!/usr/bin/python3
"""
module to make http requests to jsonplaceholder
api to get employees tasks
"""
from requests import get, status_codes
from sys import argv


def get_users(emp_id=None):
    if isinstance(emp_id, int):
        data = get("https://jsonplaceholder.typicode.com/users/{}"
                   .format(emp_id))
        return data


def get_users_tasks(emp_id=None):
    if isinstance(emp_id, int):
        data = get("https://jsonplaceholder.typicode.com/users/{}/todos"
                   .format(emp_id))
        return data


if __name__ == "__main__":
    empid = int(argv[1])
    user_info = get_users(empid).json()
    task_list = get_users_tasks(empid).json()
    completed_tasks = list(filter(lambda x: x["completed"] is True, task_list))
    print("Employee {} is done with tasks({}/{}):"
          .format(user_info["name"], len(completed_tasks), len(task_list)))
    [print("\t {}".format(task["title"])) for task in completed_tasks]
