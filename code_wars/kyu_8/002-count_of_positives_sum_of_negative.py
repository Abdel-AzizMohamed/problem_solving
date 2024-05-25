###### Solution 1


def count_positives_sum_negative(arr):
    if len(arr) == 0:
        return []

    result = [0, 0]

    for item in arr:
        if item > 0:
            result[0] += 1
        else:
            result[1] += item

    return result


###### Solution 2


def count_positives_sum_negative(arr):
    if not arr:
        return []

    positive_count = len([item for item in arr if item > 0])
    negative_sum = sum(item for item in arr if item < 0)

    return [positive_count, negative_sum]


###### Solution link: https://youtu.be/-Fy7tovit9A
