import csv
import requests

users = []

with open("users.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        users.append(row)

#Fetch API data
details = []

for user in users:
    url = f"https://jsonplaceholder.typicode.com/users/{user['id']}"
    response = requests.get(url)
    data = response.json()

    details.append({
        "name": data["name"],
        "username": data["username"],
        "email": data["email"],
        "city": data["address"]["city"]
    })

#Write report
with open("report.txt", "w") as f:
    for d in details:
        f.write(f"{d['name']} - {d['email']} - {d['city']}\n")
    
#Filter users by city
filtered = [d for d in details if d["city"] == "South Christy"]

print("Users from South Christy:")
for f in filtered:
    print(f["name"], "-", f["email"])

#Menu
while True:
        print("\n=== MENU ===")
        print("1. Show all users")
        print("2. Filter by city")
        print("3. Export report")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            for d in details:
                print(d["name"])

        elif choice == "2":
            filtered = [d for d in details if d["city"] == "South Elvis"]

            print("Users from South Elvis:")
            for f in filtered:
                print(f["name"], "-", f["email"])

        elif choice == "3":
            with open("report.txt", "w") as f:
                for d in details:
                    f.write(f"{d['name']} - {d['email']} - {d['city']}\n")
            print("Report saved to report.txt")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")