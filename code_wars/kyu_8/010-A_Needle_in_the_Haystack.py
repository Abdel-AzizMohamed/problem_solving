###### Solution 1
def find_needle(haystack: list):
    needle_index = -1

    for i, item in enumerate(haystack):
        if item == "needle":
            needle_index = i
            break

    return f"found the needle at position {needle_index}"


###### Solution 2 (Will throw ValueError if not found)
def find_needle(haystack: list):

    return f"found the needle at position {haystack.index('needle')}"


###### Video Link:
###### Problem Link: https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python
