###### Solution 1
def pig_it(text: str) -> str:
    result = []

    for word in text.split(" "):
        if word[0] in {"!", ".", ",", "?"}:
            result += word
            continue
        result.append(word[1:] + word[0] + "ay")

    return " ".join(result)


###### Solution 2
def pig_it(text: str) -> str:
    pun = {"!", ".", ",", "?"}
    return " ".join(
        [
            f"{word[1:]}{word[0]}ay" if word not in pun else word
            for word in text.split(" ")
        ]
    )


###### Problem Link: https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
