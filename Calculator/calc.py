def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

print("Select Your Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

try:
    method = int(input("Enter Your Method (1-4): "))
    num_1 = float(input("Enter Your First Number: "))
    num_2 = float(input("Enter Your Second Number: "))

    if method == 1:
        result = add(num_1, num_2)
    elif method == 2:
        result = sub(num_1, num_2)
    elif method == 3:
        result = multiply(num_1, num_2)
    elif method == 4:
        result = divide(num_1, num_2)
    else:
        result = "Invalid Method! Please choose between 1-4."

except ValueError:
    result = "Invalid Input! Please enter numbers only."

print(f"Your Calculator Result: {result}")
