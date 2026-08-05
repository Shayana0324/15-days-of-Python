def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

# running = True

while(True):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Choose operator (+, -, *, /): ")

    if op == "+":
        print(f"Result:\n{num1} + {num2} = ", add(num1, num2))
    elif op == "-":
        print(f"Result:\n{num1} - {num2} = ", subtract(num1, num2))
    elif op == "*":
        print(f"Result:\n{num1} * {num2} = ", multiply(num1, num2))
    elif op == "/":
        print(f"Result:\n{num1} / {num2} = ", divide(num1, num2))
    else:
        print("Invalid operator")

    again = input("Calculate again? (yes/no): ")
    if again.lower() != "yes":
        break

print("Goodbye!")