###### Solution 1
def vowel_indices(word):
    result = []

    for i, letter in enumerate(word.lower()):
        if letter in {"a", "e", "i", "o", "u", "y"}:
            result.append(i + 1)

    return result


###### Solution 2
def vowel_indices(word):
    return [
        i + 1
        for i, letter in enumerate(word.lower())
        if letter in {"a", "e", "i", "o", "u", "y"}
    ]


###### Video Link:
###### Problem Link: https://www.codewars.com/kata/5680781b6b7c2be860000036/train/python
