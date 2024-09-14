###### Solution 1
def is_pangram(st):
    letters = [chr(i) for i in range(ord("a"), ord("z") + 1)]
    st = {*st.lower()}

    for letter in letters:
        if letter not in st:
            return False
    return True


###### Solution 2
def is_pangram(st):
    letters = {chr(i) for i in range(ord("a"), ord("z") + 1)}
    st = {*st.lower()}

    return letters.issubset(st)


###### Video Link:
###### Problem Link: https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
