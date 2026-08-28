def square(number):
    """This function finds the number of grains on a given square.
    """
    if 1 <= number <= 64:
        return 2 ** (number - 1)
    raise ValueError("square must be between 1 and 64")

def total():
    """
    Finds the total grains on the whole chess board.
    """
    total_grains = 0
    for num in range(1, 65):
        total_grains += square(num)
    return total_grains
