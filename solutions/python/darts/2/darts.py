import math

def score(x, y):
    rad = math.sqrt(x**2 + y**2)
    if rad <= 1:
        return 10
    if rad <= 5:
        return 5
    if rad <= 10:
        return 1
    return 0
