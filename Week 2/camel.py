#implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case.
#Assume that the user’s input will indeed be in camel case.


def main():

    modified_name = ""
    name = user_input()

#add _ behind the uppercase & lowercase
    for i in range(len(name)):
        if name[i].isupper():
            modified_name += "_" + name[i].lower()
        else:
            modified_name += name[i]
    print(modified_name)

def user_input():
    name = input("Please enter name: ")
    return name

main()
