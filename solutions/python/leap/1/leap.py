"""
Code to determine whether the given year is a leap year or not
"""

def leap_year(year: int) -> bool:
    """
    Calculates whether the given year is a leap year or not.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)