"""
A function to calculate how many steps it took for a number to lead back to 1.

Args:
    number: The positive integer to transform.

Returns:
    The number of transformation steps taken to reach 1.
"""

def steps(number):
    """
    If the given number is a positive Integer, this function returns the number of times the transformations took place to transform the given number into 1.
    """
    if isinstance(number, int) and number > 0:
        count = 0
        while number !=1:
            if number % 2 == 0:
                number = number // 2
                count += 1
            else:
                number = (number * 3) + 1
                count +=  1
        return count
    raise ValueError("Only positive integers are allowed")