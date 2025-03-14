"""
implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.
 If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##.
 And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

convert() is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float.
For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
 """

def main():
    # user input and split time into hour and mins
    mealtime = input("What time is it?\n")

# breakfast = 7:00 and 8:00
    if 7 <= convert(mealtime) <= 8:
        print("breakfast time")
# lunch = 12:00 and 13:00
    elif 12 <= convert(mealtime) <= 13:
        print("lunch time")
# dinner = 18:00 and 19:00
    elif 18 <= convert(mealtime) <= 19:
        print("dinner time")

def convert(time):
    hour, mins = time.split(":")
    convert_mins = float(mins) / 60
    return round(int(hour) + convert_mins, 2)

if __name__ == "__main__":
    main()
