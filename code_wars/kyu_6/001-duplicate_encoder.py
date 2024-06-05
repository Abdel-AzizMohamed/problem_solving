###### Solution 1


def duplicate_encode(word):
    word = word.lower()
    words_array = list(word)
    result = ""

    for ch in word:
        if words_array.count(ch) >= 2:
            result += ")"
            continue
        result += "("

    return result
