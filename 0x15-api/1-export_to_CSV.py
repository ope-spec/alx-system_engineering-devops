#!/usr/bin/python3
"""Fetch an employee's TODO list progress and export to CSV file """
import requests
import sys
import csv


def fetch_todo_list(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    if user_response.status_code != 200:
        print('User not found')
        return
    if todo_response.status_code != 200:
        print('TODO list not found')
        return

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_name = user_data.get('name')

    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task['completed'])

    print(f'Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):')
    for task in todo_data:
        if task['completed']:
            print(f'\t{task["title"]}')

    csv_filename = f'{employee_id}.csv'
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_data:
            csv_writer.writerow([employee_id, employee_name, task["completed"], task["title"]])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python3 script.py <employee_id>')
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_list(employee_id)
