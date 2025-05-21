import json
import os

DATA_FILE = 'employees.json'

def load_employees():
    if not os.path.exists(DATA_FILE):
        return []
    
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("⚠️ Error: JSON file is corrupted or empty. Starting fresh.")
        return []

def save_employee(data):
    try:
        with open(DATA_FILE,'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"❌ Error saving data: {e}")
