###### Solution 1
def count_sheeps(sheep):
    result = 0

    for item in sheep:
        if not item:
            continue
        result += item

    return result


###### Solution 2
def count_sheeps(sheep):
    return sum(item for item in sheep if item)
