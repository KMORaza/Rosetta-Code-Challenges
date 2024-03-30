# Leap year
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
year1 = 2022
if is_leap_year(year1):
    print(f"{year1} is a leap year.")
else:
    print(f"{year1} is not a leap year.")
year2 = 2023
if is_leap_year(year2):
    print(f"{year2} is a leap year.")
else:
    print(f"{year2} is not a leap year.")
year3 = 2024
if is_leap_year(year3):
    print(f"{year3} is a leap year.")
else:
    print(f"{year3} is not a leap year.")