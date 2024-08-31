###### Python ######
###### Solution 1
def sum_cubes(n: int) -> int:
    """"""
    result = 0

    for i in range(1, n + 1):
        result += i**3

    return result


###### Solution 2
def sum_cubes(n: int) -> int:
    """"""
    return sum(i**3 for i in range(1, n + 1))


###### Link: Video 7
