import math

###### Solution 1


def is_square(n: int):
    if n <= 0:
        return True if n == 0 else False
    return True if math.sqrt(n) % 1 == 0 else False


####### Link: 005
