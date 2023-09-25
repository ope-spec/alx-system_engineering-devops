#!/usr/bin/python3
"""
A dictionary to store task data for all employees
"""

import json
import requests
import sys


def main():
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    users = response.json()

    employee_data = {}
    
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        
        user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
        response = requests.get(user_url)
        tasks = response.json()
        
        employee_data[user_id] = []
        
        for task in tasks:
            employee_data[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    
    with open('todo_all_employees.json', 'w') as file:
        json.dump(employee_data, file, indent=4)

if __name__ == '__main__':
    main()
