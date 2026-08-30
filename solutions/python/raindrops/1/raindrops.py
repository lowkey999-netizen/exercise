"""
Function to convert a number into its corresponding raindrop sounds.
"""
def convert(number):
    """
    Converts a given number to its corresponding raindrop sounds.
    """
    result = ""
    if number % 3 == 0:
        result = result+"Pling"
    if number % 5 == 0:
        result = result + "Plang"
    if number % 7 == 0:
        result = result + "Plong"
    if result == "":
        return str(number)
    return result