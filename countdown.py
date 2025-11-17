#Ask for a user input: a number
user_number = int(input("Enter a number: "))

for i in range(1, user_number):
    
    if i % 2 == 0:
        continue
    if i == 15:
        break
    print(i)
