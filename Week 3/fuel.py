"""
implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer,
and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains,
output F instead to indicate that the tank is essentially full.
If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.)
Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""
def main():
    x = get_frac() #user input
    perc = divide(x) #division + roundup + convertion %
    if perc <= 1:
        print("E")
    elif perc >= 99:
        print("F")
    else:
        print(f"{int(perc)}%")

def get_frac():
    while True:
         try:
            frac = input("Please enter: ")
            x = int(frac[:frac.find("/")]) # numerator
            y = int(frac[frac.find("/")+1:]) # denominator
            if y == 0 or x > y:
                False
            else:
                return x, y
         except ValueError:
             print("Please enter valid fraction.")

def divide(fraction): # handle calculation
    x = int(fraction[0])
    y = int(fraction[-1])
    return round(x/y,2) * 100

if __name__ == "__main__":
    main()