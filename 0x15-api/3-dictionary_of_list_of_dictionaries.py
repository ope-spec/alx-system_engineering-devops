#!/usr/bin/python3
"""Fetch and display an employee's TODO list progress and
a dictionary to store task data for all employees
"""
import requests
import sys
import json


def fetch_all_employee_todo_lists():
    base_url = 'https://jsonplaceholder.typicode.com'
    users_url = f'{base_url}/users'
    users_response = requests.get(users_url)

    if users_response.status_code != 200:
        print('Unable to fetch user data')
        return

    users_data = users_response.json()

    # Create a dictionary to store task data for all employees
    all_employee_tasks = {}

    for user in users_data:
        employee_id = user['id']
        username = user['username']

        todo_url = f'{base_url}/todos?userId={employee_id}'
        todo_response = requests.get(todo_url)

        if todo_response.status_code != 200:
            print(f'TODO list not found for user {username}')
            continue

        todo_data = todo_response.json()

        employee_tasks = []

        for task in todo_data:
            task_data = {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            employee_tasks.append(task_data)

        all_employee_tasks[employee_id] = employee_tasks

    json_filename = 'todo_all_employees.json'
    with open(json_filename, mode='w') as json_file:
        json.dump(all_employee_tasks, json_file, indent=4)

if __name__ == "__main__":
    fetch_all_employee_todo_lists()
