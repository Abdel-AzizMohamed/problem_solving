###### Solution 1
def dec_to_hex(num: int) -> str:
    hex_table = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F",
    }
    return (
        hex_table[str(int((num / 256 % 1) * 16))]
        + hex_table[str(int((num / 16 % 1) * 16))]
    )


def rgb(r: int, g: int, b: int) -> str:
    r = 255 if r > 255 else 0 if r < 0 else r
    g = 255 if g > 255 else 0 if g < 0 else g
    b = 255 if b > 255 else 0 if b < 0 else b
    return f"{dec_to_hex(r)}{dec_to_hex(g)}{dec_to_hex(b)}"


###### Solution 2
def cap(num: int) -> int:
    """"""
    return min(255, max(num, 0))


def rgb(r: int, g: int, b: int) -> str:
    """"""
    return f"{cap(r):02X}{cap(g):02X}{cap(b):02X}"


###### Link:
###### Problem Link: https://www.codewars.com/kata/513e08acc600c94f01000001/train/python
