# implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂
# and any :( converted to 🙁 . All other text should be returned unchanged.
# Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result.
def main():
     user_input = input("Please input: ")
     convert(user_input) #pass on variable to convert()

def convert(new): #convert will have its own parameter but taken as a variable from main()
    emoticon = new.replace(":)", "🙂").replace(":(", "🙁")
    print(emoticon)

main()
