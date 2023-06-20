# Calculator-Tutorial-Python-
# the Program - 
This code is a simple calculator program that allows 
the user to perform basic arithmetic operations.
 Let's go through it step by step.

# 1. The program starts by -
asking the user to enter the first number, 
operator, and second number. It does this by displaying messages and waiting for 
the user to input values. The first number is stored in a variable called "first", 
the operator is stored in a variable called "operator", 
and the second number is stored in a variable called "second".

# Ex - first = input("Enter the first number: ")
#     operator = input("Enter the operator (+, -, *, /, %): ")
#     second = input("Enter the second number: ")

2. Since the values entered by the user are initially stored as strings, 
we need to convert them into integers so that we can perform arithmetic operations. 
The code uses the "int()" function to convert the "first" and "second" variables from strings to integers.

#Ex - first = int(first)
#    second = int(second)

3. Next, the program prints "The Answer is :" to indicate that the result 
of the calculation will be displayed next.

# print("The answer is:")

4. Now comes the part where the actual calculation happens. 
The code uses an if-elif-else block to determine which arithmetic operation 
to perform based on the value of the "operator" variable.

If the operator is "+", it adds the "first" and "second" numbers together and prints the result.
# EX - if operator == "+":
#      print(first + second)

If the operator is "-", it subtracts the "second" number from the "first" number and prints the result.
EX - elif operator == "-":
#    print(first - second)

If the operator is "*", it multiplies the "first" and "second" numbers and prints the result.
# EX - elif operator == "*":
#      print(first * second)

If the operator is "/", it divides the "first" number by the "second" number and prints the result.
# EX - elif operator == "/":
 #    print(first / second) 

If the operator is "%", it performs the modulus operation on the "first" number with the "second" number and 
prints the result.
# EX - elif operator == "%":
#     print(first % second)  

If none of the above conditions are met, 
it means an invalid operator was entered. In that case, 
the program prints "Invalid Operation" to indicate that the operator provided is not recognized.

# EX - else:
 #    print("Invalid operation") 

and displays the result. 
Feel free to ask if you have any further 
questions or if there's anything specific you would like to understand better!
