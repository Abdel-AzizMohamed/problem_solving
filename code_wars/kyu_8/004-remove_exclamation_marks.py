###### Solution 1
def remove_exclamation_marks(s: str) -> str:
    """"""
    new_string = ""

    for ch in s:
        if ch != "!":
            new_string += ch

    return new_string


###### Solution 2
def remove_exclamation_marks(s: str) -> str:
    """"""
    return "".join([ch for ch in s if ch != "!"])


###### Solution 3
def remove_exclamation_marks(s: str) -> str:
    """"""
    return s.replace("!", "")


[1, 2, 4, 6]
