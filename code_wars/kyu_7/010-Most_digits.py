###### Solution 1
def find_longest(arr):
    result = arr.pop(0)

    for item in arr:
        if len(str(item)) > len(str(result)):
            result = item

    return result


###### Link:
###### Problem Link: https://www.codewars.com/kata/58daa7617332e59593000006/train/python
