#!/usr/bin/python3
"""Fetch and display an employee's task list progress"""
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    # Fetch user information
    user = requests.get(f"{base_url}users/{employee_id}")
    user_data = user.json()
    employee_name = user_data.get("name")

    # Fetch to-do list
    todos_response = requests.get(f"{base_url}todos",
                                  params={"userId": employee_id})
    todos_data = todos_response.json()

    # Filter completed tasks
    completed_tasks = [task.get("title")
                       for task in todos_data if task.get("completed")]

    # Print information
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), len(todos_data)))
    for task in completed_tasks:
        print(f"\t {task}")
