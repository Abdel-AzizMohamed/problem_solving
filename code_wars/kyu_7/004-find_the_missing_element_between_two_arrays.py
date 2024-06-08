###### Solution 1


def find_missing(or_arr, dup_arr):
    for item in dup_arr:
        or_arr.remove(item)

    return or_arr[0]


###### Solution 2


def find_missing(or_arr, dup_arr):
    for item in or_arr:
        if item not in dup_arr:
            return item
        dup_arr.remove(item)


####### Link: https://youtu.be/AbTsySpdDKg
