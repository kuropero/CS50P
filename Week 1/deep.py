# implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes
# if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

x = input("What is Answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

if x == str(42) or x == "forty-two" or x == "forty two":
    print("Yes")

else:
    print("No")
