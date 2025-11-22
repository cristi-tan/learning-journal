#Ask the user to choose:
#1. View first 10 users
#2. View posts from a specific user
#3. Create new post
#4. Delete a post

#Use GET/POST/DELETE to interact with: https://jsonplaceholder.typicode.com

#Print data nicely formatted: This simulates a real API client, just like in automation testing.

import requests

while True:
    print("\n=== MENU ===")
    print("1. View first 10 users")
    print("2. View posts from a specific user")
    print("3. Create new post")
    print("4. Delete a post")
    print("5. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        users = response.json()

        print("\n=== First 10 users ===")
        for user in users[:10]:          # only first 10
            print(f"ID: {user['id']}")
            print(f"Name: {user['name']}")
            print(f"Username: {user['username']}")
            print(f"Email: {user['email']}")
            print("-" * 40)
    elif choice == 2:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        posts = response.json()

        user_id = int(input("Enter the user id: "))

        found = False
        for post in posts:
            if post["userId"] == user_id:
                found = True
                print(f"Title: {post['title']}")
                print(f"Body: {post['body']}")
                print("-" * 40)

        if not found:
            print("No posts found for this user.")
    elif choice == 3:
        title = input("Enter post title: ")
        body = input("Enter post body: ")
        user_id = int(input("Enter user id: "))

        payload = {"title": title, "body": body, "userId": user_id}
        response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)

        print("\nCreated post (fake, API is mock):")
        print(response.json())
    elif choice == 4:
        post_id = int(input("Enter post id to delete: "))
        response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
        print("\nDELETE status:", response.status_code)
    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.")
        

