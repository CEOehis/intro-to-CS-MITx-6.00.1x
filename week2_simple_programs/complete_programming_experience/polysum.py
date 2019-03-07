import math


def polysum(n, s):
    '''
    n: int, number of sides of the polygon.
    s: int, length of a side

    returns: int sum of the area and square of the perimeter of the polygon
    '''
    def area(n, s):
        return (0.25 * n * s ** 2)/(math.tan(math.pi/n))

    #return area(n,s)

    def perimeter(n, s):
        return (n * s) ** 2

    return round((area(n, s) + perimeter(n, s)), 4)
