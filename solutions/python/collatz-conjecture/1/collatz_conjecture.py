def steps(number):
    if type(number) == int and number > 0:
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

