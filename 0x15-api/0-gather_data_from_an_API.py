#!/usr/bin/python3

"""Fetch and display an employee's task list progress"""

import requests
import sys

if __name__ == "__main__":
     employee_id = sys.argv[1]
     url = f"https://jsonplaceholder.typicode.com/"
     user = requests.get(f"{url}users/{employee_id}").json()
     todos = requests.get(f"{url}todos", params={"userId": employee_id}).json()

completed = [t.get("title") for t in todos if t.get("completed") is True]
print(f"Employee {user.get('name')} is done with tasks({len(completed)}/{len(todos)}):")
for task in completed:
    print(f"\t{task}")
