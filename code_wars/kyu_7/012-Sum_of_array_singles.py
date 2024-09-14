###### Solution 1
def repeats(arr: list) -> int:
    result = 0

    for num in arr:
        if arr.count(num) == 1:
            result += num

    return result


###### Solution 2
def repeats(arr: list) -> int:
    return sum(num for num in arr if arr.count(num) == 1)


###### Solution 3 (Only works if the max duplication = 2)
def repeats(arr: list) -> int:
    return 2 * sum(set(arr)) - sum(arr)


###### Video Link:
###### Problem Link: https://www.codewars.com/kata/59f11118a5e129e591000134/train/javascript
