###### Solution 1


def to_float_array(array):
    result = []

    for num in array:
        n = int(num) if num.find(".") == -1 else float(num)
        result.append(n)

    return result


###### Solution 2
def to_float_array(array):
    return [float(item) for item in array]
