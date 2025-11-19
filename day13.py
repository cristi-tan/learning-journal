#Catch a ValueError
try:
    age = int("abc")
except ValueError:
    print("Invalid number")

#Catch division by zero
try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero")

#Ask for user input and handel errors
user_input = input("Enter a number: ")

try:
    x = int(user_input)
    print(f"You entered number {x}")
except ValueError:
    print("Please enter a valid number")

#File not found exception
try:
    f = open("missingfile.txt")
except FileNotFoundError:
    print("File not found")

#Use else and finally
try:
    num = int("10")
except:
    print("Error")
else:
    print("Everything is ok")
finally:
    print("Finished")
    
