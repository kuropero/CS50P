# Instructions
# implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place.
# Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

#     x is an integer
#     y is +, -, *, or /
#     z is an integer

# For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

# Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!

def add(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def divide(a, b):
    return a / b if b != 0 else print("Error, not divisible by 0")

def mutiply(a, b):
    return a * b

def main():
    # user input broken into substring
    expression = input("Please state your arithmetic expression: ")
    x, y ,z = expression.split(" ")

    # check if inputs are within approve parameters
    if x.isnumeric() == False or z.isnumeric() == False:
        print("Please enter valid number.")
        return

    elif not y in ["+", "-", "*", "/"]:
        print("Please enter valid operator.")
        return

    # convert variables to float
    x = float(x)
    z = float(z)

    if y == "+":
        results = add(x, z)

    elif y == "-":
        results = subtraction(x, z)

    elif y == "/":
        results = divide(x, z)

    elif y == "*":
        results = mutiply(x, z)

    print(results)

main()