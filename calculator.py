# Function to perform the chosen operation
def calculate(n, m, operation):
    if operation == '1':
        return n + m
    elif operation == '2':
        return n - m
    elif operation == '3':
        return n * m
    elif operation == '4':
        return n / m if m != 0 else "undefined (division by zero)"
    elif operation == '5':
        return n // m if m != 0 else "undefined (division by zero)"
    elif operation == '6':
        return n % m if m != 0 else "undefined (division by zero)"
    elif operation == '7':
        return n ** m
    else:
        return "Invalid operation"
n = float(input("Enter the first number: "))
m = float(input("Enter the second number: "))
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Floor Division (//)")
print("6. Modulus (%)")
print("7. power(^)")
operation = input("Enter your choice (1-7): ")
answer = calculate(n, m, operation)
print("The answer after calculation is:", answer)
