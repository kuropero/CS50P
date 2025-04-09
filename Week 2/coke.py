#implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
#Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
#Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.


def main():
    debt = 50
    while debt > 0:
        print(f"Amount Due: {debt}")
        coin = int(input("Please insert coin: "))
        if coin in [5, 10, 25]:
            debt -= coin

        if debt <= 0:
            print(f"Change Owed: {-debt}")
            break


main()
