#Ask for user name
#Ask for user monthly salary
#Calculate yearly salary
#Display the result

#Display a message to the user and store the input
print("Enter you name: ")
name = input()

#Display a message to the user and store the input
print("What is your monthly salary?")
monthly_salary = int(input())

#Calculate yearly salary
yearly_salary = 12*monthly_salary

#Display the result
print(f"Hello {name}")
print(f"Your yearly salary is : {yearly_salary} EUR")
