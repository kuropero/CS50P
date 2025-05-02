"""
implement a program that prompts the user for a date, in month-day-year order, formatted like 9/8/1636 or September 8, 1636
output that same date in YYYY-MM-DD format. 
If the user’s input is not a valid date in either format, prompt the user again.
"""

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def main():
    mm, dd, yyyy = date_input()
    print(f"{yyyy}-{mm:02}-{dd:02}")

def date_input():
    while True:
        date = input("Please enter in month-day-year\nDate: ").strip()
        # form dates
        if '/' in date:
            parts = date.split('/')
            if not parts[0].isdigit():
                continue
        elif ' ' in date and ',' in date:
            parts = date.replace(',','').split()
        else:
            continue

        # check if date is in 3 parts
        if len(parts) != 3:
            continue

        mm_part, dd_part, yyyy_part = parts
        
        try:
            if mm_part in months:
                mm = months.index(mm_part) + 1
            else:
                mm = int(mm_part)
                if not (1 <= mm <= 12):
                    continue
        except ValueError:
            continue
            #convert dd & yyyy to int for sanitize
        try:
            dd = int(dd_part)
            yyyy = int(yyyy_part)
        except ValueError:
            continue
        
        #sanitize dd & yyyy
        if not (1 <= dd <= 31):
            continue
        if not (1500 <= yyyy <= 3000):
            continue

        return mm, dd, yyyy

if __name__ == "__main__":
    main()
