###### Solution 1
def reverse_number(n: int) -> int:
    result = ""
    sign = -1 if n < 0 else 1

    for digit in str(abs(n)):
        result = digit + result

    return sign * int(result)


###### Solution 2
def reverse_number(n: int) -> int:
    return int((n < 0) * "-" + str(abs(n))[::-1])


###### Video Link:
###### Problem Link: https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5/train/python
