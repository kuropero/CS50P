#implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer.
#Assume that the user will input an integer.
#c = 300000000
#    4500000000000000000

def main():
    m = int(input("m: "))
    answer = calculation(m)
    print(f"E: {answer}")

def calculation(n):
    joules = n * 300000000 ** 2
    return joules

main()
