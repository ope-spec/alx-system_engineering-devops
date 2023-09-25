#!/usr/bin/python3
"""
A dictionary to store task data for all employees..
"""
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information for all employees
    users_response = requests.get(f"{base_url}users")
    users_data = users_response.json()

    employee_data = {}

    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")

        # Fetch to-do list for each employee
        todos_response = requests.get(f"{base_url}todos",
                                      params={"userId": user_id})
        todos_data = todos_response.json()

        # Store to-do list information
        employee_data[user_id] = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            } for todo in todos_data
        ]

    # Export to JSON
    json_filename = "todo_all_employees.json"
    with open(json_filename, "w") as jsonfile:
        json.dump(employee_data, jsonfile, indent=4)
