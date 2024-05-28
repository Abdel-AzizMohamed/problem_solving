###### Solution 1
def sequence_sum(begin_number: int, end_number: int, step: int) -> int:
    """"""
    result = 0

    for i in range(begin_number, end_number + 1, step):
        result += i

    return result


###### Solution 2
def sequence_sum(begin_number: int, end_number: int, step: int) -> int:
    """"""
    return sum(range(begin_number, end_number + 1, step))


###### Solution link: https://youtu.be/8nyMycfVSzE
