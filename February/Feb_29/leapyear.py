def is_leap_year(year):
    """
    Function to check if a year is a leap year.
    Leap years are divisible by 4, except for years that are divisible by 100 but not by 400.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

if __name__ == "__main__":
    main()
