#This is the orchestrator:
from data_utils import read_users_from_csv, write_report
from api_utils import get_user_details

def build_details_list():
    users = read_users_from_csv()
    details = []
    for user in users:
        d = get_user_details(user["id"])
        details.append(d)
    return details

def filter_by_city(details, city: str):
    return [d for d in details if d["city"] == city]

def main():
    details = build_details_list()
    write_report(details)
    print("Initial report generated.\n")

    while True:
        print("\nMenu:")
        print("1. Show all users")
        print("2. Filter by city")
        print("3. Regenerate report")
        print("4. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            for d in details:
                print(f"{d['name']} - {d['email']} - {d['city']}")
        elif choice == "2":
            city = input("City: ").strip()
            filtered = filter_by_city(details, city)
            for f in filtered:
                print(f"{f['name']} - {f['email']}")
        elif choice == "3":
            details = build_details_list()
            write_report(details)
            print("Report regenerated.")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
