###### Solution 1


def maps(array):
    result = []

    for item in array:
        result.append(item * 2)

    return result


###### Solution 2


def maps(array):
    return [item * 2 for item in array]


###### Solution 3


def maps(array):
    return list(map(lambda x: x * 2, array))


####### Link: https://youtu.be/AbTsySpdDKg
