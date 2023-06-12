# Addition Function
def add(n1, n2):
    return n1 + n2

# Subtraction function
def subtract(n1, n2):
    return n1 - n2

# Multiply Function
def multiply(n1, n2):
    return n1 * n2

# Divide Function
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What is the first number?: "))

for key in operations:
    print(key)

operation_symbol = input("Please enter a operation from the line above: ")
num2 = int(input("What is the second number?: "))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(answer)