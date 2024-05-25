###### Solution 1


def invert(lst):
    result = []

    for item in lst:
        result.append(-item)

    return result


###### Solution 2


def invert(lst):
    return [-item for item in lst]


###### Solution link: https://youtu.be/-Fy7tovit9A
