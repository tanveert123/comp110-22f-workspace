"""EX03 - Wordle.""" 


__author__ = "730578741"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of [str, str], invert should return a dict[str, str] that inverts the keys and the values."""
    new_dict: dict[str, str] = {}

    for i in a:
        if a[i] in new_dict:
            raise KeyError("Argument is empty dictionary, making this a KeyError.")
        new_key: str = a[i]
        new_value: str = i 
        new_dict[new_key] = new_value
    return new_dict


def favorite_color(n_and_f: dict[str, str]) -> str:
    """Given a dictionary of [str, str] of names and favorite colors, favorite_color should return a string which is the color that appears most frequently."""
    new_dict = {}

    for i in n_and_f:
        if n_and_f[i] not in new_dict:
            new_dict[n_and_f[i]] = 1
        else:
            new_dict[n_and_f[i]] += 1
    
    high: int = 0
    second_high: int = 0
    color: str = ""

    for j in new_dict:
        num = new_dict[j]
        if num > high:
            second_high = high
            high = num
            color = j
        if second_high == high:
            for k in new_dict:
                if new_dict[k] == high:
                    color = k
            return color
        else:
            return color
    

def count(str_list: list[str]) -> dict[str, int]:
    """Given a list[str], count will produce a dictionary of [str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    input_dict = {}
    i: int = 0

    while i < len(str_list):
        if str_list[i] not in input_dict:
            input_dict[str_list[i]] = 1
        else:
            input_dict[str_list[i]] += 1
        i += 1
    return input_dict