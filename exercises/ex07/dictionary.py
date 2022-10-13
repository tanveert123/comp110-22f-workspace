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
    high: int = 0
    color = ""
    color_list: list[str] = list()

    for i in n_and_f:
        color_list.append(n_and_f[i])
    for j in color_list:
        if j not in new_dict:
            new_dict[j] = 1
        else:
            new_dict[j] += 1
        if new_dict[j] > high:
            high = new_dict[i]
            color = j
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