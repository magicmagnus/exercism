def equilateral(sides):
    a, b, c = sides
    if is_valid_triangle(a, b, c):
        return a == b and b == c
    return False
    


def isosceles(sides):
    a, b, c = sides
    if is_valid_triangle(a, b, c):
        return a == b or a == c or b == c
    return False

def scalene(sides):
    a, b, c = sides
    if is_valid_triangle(a, b, c):
        return a != b and a != c and b != c
    return False

def is_valid_triangle(a, b, c):
    if a + b < c or b + c < a or a + c < b or a == 0 or b == 0 or c == 0: # not valid triangle
        return False
    return True
    
