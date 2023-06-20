# Ask the user to enter the first number, operator, and second number
first = input("Enter the first number: ")
operator = input("Enter the operator (+, -, *, /, %): ")
second = input("Enter the second number: ")

# Convert the input strings to integers
first = int(first)
second = int(second)

# Print the output message
print("The answer is:")

# Check the operator and perform the corresponding operation
if operator == "+":
    print(first + second)  # Add the two numbers
elif operator == "-":
    print(first - second)  # Subtract the second number from the first number
elif operator == "*":
    print(first * second)  # Multiply the two numbers
elif operator == "/":
    print(first / second)  # Divide the first number by the second number
elif operator == "%":
    print(first % second)  # Compute the remainder of the first number divided by the second number
else:
    print("Invalid operation")  # The entered operator is not supported

