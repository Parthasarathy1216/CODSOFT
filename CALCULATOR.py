def calculator():
    print("Simple Calculator")
    print("Operations: + for addition, - for subtraction, * for multiplication, / for division")

    try:
        num1 = float(input("Enter the first number: "))
        op = input("Enter an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            result = num1 / num2
        else:
            return "Invalid operation."

        return f"Result: {num1} {op} {num2} = {result}"
    except ValueError:
        return "Invalid input. Please enter numeric values."

# Run the calculator
output = calculator()
print(output)
