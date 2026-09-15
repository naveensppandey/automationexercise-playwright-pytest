import csv
import os
import random

def read_csv_data(filename):
    """
    Simple function to read a CSV file and return rows as a list of dictionaries.
    Example output: [{'username': 'a@gmail.com', 'password': '123', 'expectedResult': 'success'}]
    """
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(project_root, filename)
    
    rows = []
    with open(filepath, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows

def get_random_valid_user(filename="test_data/login_data.csv"):
    """Reads CSV file and returns a randomly selected valid user dictionary."""
    rows = read_csv_data(filename)
    valid_users = [row for row in rows if row.get("expectedResult") == "success"]
    return random.choice(valid_users)

