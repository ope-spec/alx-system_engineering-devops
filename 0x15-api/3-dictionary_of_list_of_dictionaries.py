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

    # Export to JSON
    json_filename = "todo_all_employees.json"
    with open(json_filename, "w") as jsonfile:
        json.dump({
            user.get("id"): [
                {
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": user.get("username")
                } for todo in requests.get(f"{base_url}todos",
                                           params={"userId": user.get("id")}).json()]
            for user in users_data
        }, jsonfile, indent=4)
