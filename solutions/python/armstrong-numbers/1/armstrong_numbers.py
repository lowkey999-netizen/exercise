def is_armstrong_number(number):
    str_num = str(number)
    total = 0
    for digit in str_num:
        add = int(digit) ** (len(str_num))
        total += add
    return total == number
