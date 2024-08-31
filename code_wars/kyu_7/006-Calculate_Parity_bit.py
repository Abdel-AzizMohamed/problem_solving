###### Solution 1
def check_parity(parity: str, bin_str: str) -> int:
    """"""
    current_parity = "even" if bin_str.count("1") % 2 == 0 else "odd"

    return 0 if current_parity == parity else 1


###### Link: 006
