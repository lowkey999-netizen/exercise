"""
Code to determine if a triangle is equilateral, isosceles, or scalene.
"""
def is_it_a_triangle(sides):
    """
    Validates whether the given lengths form a triangle or not.
    """
    a, b, c = sides
    if a>0 and b>0 and c>0:
        return (a + b >= c) and (b + c >= a) and (a + c >= b)
    return False

    
def equilateral(sides):
    """
    Validates whether the given lengths form a equilateral triangle or not.
    """
    a, b, c = sides
    return is_it_a_triangle(sides) and (a == b == c)        

def isosceles(sides):
    """
    Validates whether the given lengths form a isosceles triangle or not.
    """
    a, b, c = sides
    return is_it_a_triangle(sides) and ((a == b) or (b == c) or (a == c))

def scalene(sides):
    """
    Validates whether the given lengths form a scalene triangle or not.
    """
    a, b, c = sides
    return is_it_a_triangle(sides) and (a != b != c != a)
