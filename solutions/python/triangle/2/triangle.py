"""
Code to determine if a triangle is equilateral, isosceles, or scalene.
"""
def is_it_a_triangle(sides):
    """
    Validates whether the given lengths form a triangle or not.
    """
    side_a, side_b, side_c = sides
    if side_a>0 and side_b>0 and side_c>0:
        return (side_a + side_b >= side_c) and (side_b + side_c >= side_a) and (side_a + side_c >= side_b)
    return False

    
def equilateral(sides):
    """
    Validates whether the given lengths form a equilateral triangle or not.
    """
    side_a, side_b, side_c = sides
    return is_it_a_triangle(sides) and (side_a == side_b == side_c)        

def isosceles(sides):
    """
    Validates whether the given lengths form a isosceles triangle or not.
    """
    side_a, side_b, side_c = sides
    return is_it_a_triangle(sides) and ((side_a == side_b) or (side_b == side_c) or (side_a == side_c))

def scalene(sides):
    """
    Validates whether the given lengths form a scalene triangle or not.
    """
    side_a, side_b, side_c = sides
    return is_it_a_triangle(sides) and (side_a != side_b != side_c != side_a)
