import math


###### Solution 1
def power_of_two(n: int) -> bool:
    """"""
    i = 0

    while 2**i <= n:
        if 2**i == n:
            return True
        i += 1
    return False


###### Solution 2 (Won't work with big numbers)
def power_of_two(n: int) -> bool:
    """"""
    if n <= 0:
        return False
    return math.log2(n) % 1 == 0


###### 08
###### Problem Link: https://www.codewars.com/kata/534d0a229345375d520006a0/train/python
