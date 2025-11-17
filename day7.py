#Write a code that requests for user to input their age and after that it outputs if he is adult or teenager.
#ask for input
print("Enter your age: ")

#store it in a variable
age = int(input())

#Check what condition meets the variable
if age < 18:
    print("You are a teenager")
else:
    print("You are an adult")


#Code that it checks the grade
grade = int(input("Enter your grade: "))

if grade >= 9:
    print("Excelent")
elif grade >= 7:
    print("Good")
else:
    print("Bad")

#Temperature check
temperature = int(input("Enter the temperature: "))

if temperature > 30:
    print("It is hot today")
else:
    print("it is cold today")


#Hardcode username and password
user = "admin"
password = "1234"

user_input = input("Enter username: ")
password_input = input("Enter password: ")

if user_input == user and password_input == password:
    print("You are logged in")
else:
    print("incorrect username or password.")








