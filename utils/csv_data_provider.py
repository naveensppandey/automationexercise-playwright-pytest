import csv
import os

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
