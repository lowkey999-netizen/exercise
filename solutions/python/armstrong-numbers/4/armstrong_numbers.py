"""Function to find out if the given number is an armstrong number or not.
"""

def is_armstrong_number(number):
    """Return True if number is an Armstrong number, False otherwise."""
    str_num = str(number)
    total = 0
    for digit in str_num:
        add = int(digit) ** (len(str_num))
        total += add
    return total == number
