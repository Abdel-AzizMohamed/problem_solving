###### Solution 1


def abbrev_name(name: str) -> str:
    """"""
    sp = name.split(" ")
    return sp[0][0].upper() + "." + sp[1][0].upper()


###### Solution 2


def abbrev_name(name: str) -> str:
    """"""
    return ".".join([item[0].upper() for item in name.split(" ")])


###### Link: 006
