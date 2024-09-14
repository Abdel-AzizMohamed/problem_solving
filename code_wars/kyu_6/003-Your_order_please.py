###### Python ######
###### Solution 1


def order(sentence: str) -> str:
    """"""
    if not sentence:
        return ""

    words_split = sentence.split(" ")
    result = [None] * len(words_split)

    for word in words_split:
        for ch in word:
            if ch.isdigit():
                result[int(ch) - 1] = word
                break

    return " ".join(result)


######
