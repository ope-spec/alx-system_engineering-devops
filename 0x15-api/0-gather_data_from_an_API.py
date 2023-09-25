#!/usr/bin/python3
"""Fetch and display an employee's task list progress"""
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    # Fetch user information
    user_response = requests.get(f"{base_url}users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch to-do list
    todos_response = requests.get(f"{base_url}todos", params={"userId": employee_id})
    todos_data = todos_response.json()

    # Filter completed tasks
    completed_tasks = [task.get("title") for task in todos_data if task.get("completed")]

    # Print information
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(todos_data)}):")
    for task in completed_tasks:
        print(f"\t {task}")
