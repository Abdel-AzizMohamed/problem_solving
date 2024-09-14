###### Solution 1 (Takes a lot of time)
def triangular(n: int) -> int:
    if n <= 0:
        return 0
    result = 0

    for i in range(1, n + 1):
        result += i

    return result


###### Solution 2 (Takes a lot of time)
def triangular(n: int) -> int:
    if n <= 0:
        return 0

    return sum(i for i in range(1, n + 1))


###### Solution 3
def triangular(n: int) -> int:
    if n <= 0:
        return 0

    return n * (n + 1) // 2


###### 09
###### Problem Link: https://www.codewars.com/kata/525e5a1cb735154b320002c8/train/python
