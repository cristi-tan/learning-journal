class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def info(self):
        print(self.name, self.salary, self.department)

    def annual_salary(self):
        return self.salary*12

employees = [
        Employee("Cristi", 100000, "CEO"),
        Employee("John", 50000, "Marketing"),
        Employee("Alex", 40000, "Technical")
    ]

#Display employees info
for emp in employees:
    emp.info()

#Display employees annual salary
for emp in employees:
    print(f"{emp.name}'s Annual Salary: {emp.annual_salary()}")
