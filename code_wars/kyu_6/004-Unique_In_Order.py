###### Solution 1
def unique_in_order(sequence):
    unique_seq = []

    for prev, item in enumerate(sequence):
        if prev == 0 or sequence[prev - 1] != item:
            unique_seq.append(item)

    return unique_seq


###### Solution 2
def unique_in_order(sequence):
    return [
        item
        for prev, item in enumerate(sequence)
        if prev == 0 or sequence[prev - 1] != item
    ]


###### 08
###### Problem Link: https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
