#!/usr/bin/python3
"""
Fetch an employee's TODO list progress and save to csv
"""

import requests
import sys
import csv


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

    with open(f'{employee_id}.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([
            "USER_ID", "USERNAME",
            "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            csv_writer.writerow([
                employee_id,
                username,
                task.get('completed'),
                task.get('title')])

if __name__ == '__main__':
    main()
