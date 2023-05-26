#!/usr/bin/python3
""" A script that uses  REST API to return information about a given employee's TODO list progress"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    name = requests.get("{}users/{}".format(url, sys.argv[1])).json()
    tasks = requests.get("{}users/{}/todos".format(url, sys.argv[1])).json()
    c_tasks = [task for task in tasks if task.get("completed") is True]
    titles = [task.get("title") for task in tasks
              if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(name.get("name"), len(c_tasks), len(tasks)))
    for title in titles:
        print("\t {}".format(title))
