#Responsible only for CSV and report files:
import csv
from config import USERS_CSV, REPORT_FILE

def read_users_from_csv():
    users = []
    with open(USERS_CSV, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            users.append(row)
    return users

def write_report(details):
    with open(REPORT_FILE, "w") as f:
        for d in details:
            f.write(f"{d['name']} - {d['email']} - {d['city']}\n")
