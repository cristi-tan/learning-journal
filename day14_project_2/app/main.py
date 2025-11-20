from .arithmetic import add, subtract, multiply, divide
from .text import capitalize_text, count_characters, check_word


def main():
    print(">>> Program started")  # debug line so we SEE it's running

    while True:
        print("\n=== MENU ===")
        print("1. Add numbers")
        print("2. Multiply numbers")
        print("3. Uppercase text")
        print("4. Search text")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", add(a, b))

        elif choice == "2":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", multiply(a, b))

        elif choice == "3":
            text = input("Enter text: ")
            print("Uppercase:", capitalize_text(text))

        elif choice == "4":
            text = input("Enter text: ")
            word = input("Enter word to search for: ")
            exists = check_word(text, word)
            print("Found!" if exists else "Not found.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    # This will run when the module is executed as a script
    main()
