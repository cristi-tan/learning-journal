#Ask for 2 numbers from user
#Ask for an math operation
#Use try/except to handle non-numeric input, division by zero
#Continue until user types "exit"
print("Type 'exit' anytime to quit.\n")

while True:
    #Ask for the first number
    num1_input = input("Enter a number: ")
    if num1_input.lower() == "exit":
        break
    try:
        num1 = float(num1_input)
    except ValueError:
        print("Invalud number!")
        continue
    
    #Ask for second number
    num2_input = input("Enter a number: ")
    if num2_input.lower() == "exit":
        break
    try:
        num2 = float(num2_input)
    except ValueError:
        print("Invalid number!")
        continue

    #Ask for math operations
    operation = input("Enter operation(+, -, *, /): ")
    if operation.lower() == "exit":
        break

    #Perform calculation safely
    try:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            print("Invalid operator")
            continue
        print(f"Result is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    
