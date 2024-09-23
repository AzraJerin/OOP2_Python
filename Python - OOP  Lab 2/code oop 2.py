# Taking input from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Performing operations
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b if b != 0 else "undefined (division by zero)"

# Displaying the results
print(f"Addition of {a} and {b} is {addition}")
print(f"Subtraction of {a} and {b} is {subtraction}")
print(f"Multiplication of {a} and {b} is {multiplication}")
print(f"Division of {a} by {b} is {division}")
