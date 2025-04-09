"""
    “All vanity plates must start with at least two letters.”
    “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate;
    "AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    “No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not.
Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not.
Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
"""
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (char_check(s) and zero_check(s) and numbers_check(s) and punctuations(s))

def char_check(s):
    return 2 <= len(s) <= 6 #no. of char check

def zero_check(s):
    try:
        x = s.index("0")
        if s[x-1].isnumeric():
            return True
    except ValueError:
        return True

def numbers_check(s):
    if s[0].isnumeric(): #first index cannot be a number
        return False
    elif s[-1].isnumeric() and s[-2].isalpha() and s[-3].isnumeric(): #prevent number,alpha,number combi
        return False
    if s[-2:].isnumeric(): # return True when digits are at last 2 or more index
        return True
    if s[-2:].isalpha(): #capture last 2 index to be alphabet
        return True

def punctuations(s): #No periods, spaces, or punctuation marks
    return s.isalnum()