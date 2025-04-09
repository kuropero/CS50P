#implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.

def main():
    modified_output = ""
    user = input("Input: ")

    #form new output
    for i in range(len(user)):
        if user[i] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:  #check if there's vowels
            modified_output += "" # cannot pop string, so replace with empty space instead
        else:
            modified_output += user[i]
    print(modified_output)


main()
