"""
implement a program that enables a user to place an order, prompting them for items, one per line,
until the user inputs control-d (which is a common way of ending one’s input to a program).
After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places.
Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.
implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).
After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places.
Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.
"""

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    memory = 0
    while True:
        try:
            entree = take_order()
            memory += float(entree)
            bill = "{:.2f}".format(memory) # print format $#.##
            print(f"${bill}")
        except TypeError:
            break

def take_order():
    while True:
        try:
            item = input("Item: ")
            item_title = item.title()
            if item_title in menu:
                order = menu.get(item_title) #need to return error, currently return None
                return order
        except EOFError:
            break

if __name__ == "__main__":
    main()
