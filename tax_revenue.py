#Ask for user input: salary
salary = int(input("Enter your salary: "))
net_salary = 0

#Check what tax should apply to the salary
if salary < 3000:
    net_salary = salary - ((salary*10)/100)
elif salary >= 3000 and salary <= 7000:
    net_salary = salary - ((salary*20)/100)
else:
    net_salary = salary - ((salary*35)/100)

print(f"Your net salary is: {net_salary}")
