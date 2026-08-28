"""Function to find out if the given number is an armstrong number or not.
"""

def is_armstrong_number(number):
    """
1. Converts the recieved number into a string, as it's tehn easy to lterate over.
2. create a variable named 'total' with 0 value. This is used for adding up the single digits from the given number.
3. Loop over the string of numbers, for each digit convert it back to a number then raise to the power of the digit-count, then add to 'total'
4. return the final result.
    """
    str_num = str(number)
    total = 0
    for digit in str_num:
        add = int(digit) ** (len(str_num))
        total += add
    return total == number
