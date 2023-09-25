#!/usr/bin/python3
"""
Fetch an employee's TODO list progress and save to json
"""

import json
import requests
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = f"{base_url}/{employee_id}"

    response = requests.get(user_url)
    username = response.json().get('username')

    todo_url = f"{user_url}/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    task_list = []
    for task in tasks:
        task_list.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })

    data_dict = {employee_id: task_list}

    with open(f'{employee_id}.json', 'w') as filename:
        json.dump(data_dict, filename, indent=4)

if __name__ == '__main__':
    main()
