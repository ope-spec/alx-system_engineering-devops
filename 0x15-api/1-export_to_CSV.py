#!/usr/bin/python3
"""
Fetch an employee's task list progress and save to csv
"""
import csv
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
    todos_response = requests.get(f"{base_url}todos", params={"userId": employee_id})
    todos_data = todos_response.json()

    # Export to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            csv_writer.writerow([
                employee_id, username, todo.get("completed"), todo.get("title")])
