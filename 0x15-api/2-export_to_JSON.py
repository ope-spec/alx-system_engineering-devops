#!/usr/bin/python3
"""
Fetch an employee's task list progress and save to JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user_response = requests.get(f"{base_url}users/{employee_id}")
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch to-do list
    todos_response = requests.get(f"{base_url}todos",
                                  params={"userId": employee_id})
    todos_data = todos_response.json()

    # Export to JSON
    json_filename = f"{employee_id}.json"
    with open(json_filename, "w") as jsonfile:
        json.dump({employee_id: [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            } for todo in todos_data]}, jsonfile, indent=4)
