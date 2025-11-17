#Will contain 4 functions, addition, subtraction, multiplication, division, ask for user input for 2 numbers, ask for desired math operation, call the correct function, display the result

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    if b != 0:
      return a / b

first_num = int(input("Input first number: "))
second_num = int(input("Input second number: "))
operation = input("Input the desired operation: ")

if operation == "addition":
    print(addition(first_num,second_num))

if operation == "subtraction":
    print(subtraction(first_num,second_num))

if operation == "multiply":
    print(multiply(first_num,second_num))

if operation == "division":
    print(division(first_num,second_num))




    
