###### Solution 1


def to_camel_case(text: str):
    """"""
    if not text:
        return ""

    sp_words = text.split("-")
    words = []
    result = ""

    for word in sp_words:
        if word.find("_") != -1:
            [words.append(w) for w in word.split("_")]
        else:
            words.append(word)

    for i, word in enumerate(words):
        if i == 0:
            result += word
        else:
            result += word[0].upper() + word[1:]

    return result


####### Link: 005
