Certainly! Here's a simple Python program that determines whether a given year is a leap year or not:

```python
# Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Get the year from the user
year = int(input("Enter a year: "))

# Check and display the result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
```

This program defines a function `is_leap_year` that checks the leap year conditions. It then takes a year as input from the user and uses the function to determine and print whether it's a leap year or not.
