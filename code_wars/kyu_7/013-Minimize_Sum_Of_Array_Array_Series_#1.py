###### Solution 1
def min_sum(arr: list) -> int:
    result = 0
    sort_arr = sorted(arr)

    for i, item in enumerate(sort_arr[: len(arr) // 2]):
        result += item * sort_arr[-(i + 1)]

    return result


###### Solution 2
def min_sum(arr: list) -> int:
    sort_arr = sorted(arr)
    return sum(
        item * sort_arr[-(i + 1)]
        for i, item in enumerate(sort_arr[: len(sort_arr) // 2])
    )


###### Video Link:
###### Problem Link: https://www.codewars.com/kata/5a523566b3bfa84c2e00010b/train/python
