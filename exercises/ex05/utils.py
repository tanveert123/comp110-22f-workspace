"""EX05 - This is where function skeletons and implementations will be implemented.""" 


__author__ = "730578741"


def only_evens(num_list: list[int]) -> str:
    """Returns all the even numbers from list"""
    even_list: str = []
    i: int = 0

    while i < len(num_list):
        if num_list[i] % 2 == 0:
            even_list.append(num_list[i])
        i += 1
    return even_list


def concat(list1: list[int], list2: list[int]) -> str:
    """Returns an int list that is made by adding the values of the second list immediately to the first list"""
    if len(list1) == 0 and len(list1) == 0:
        return []
    else:
        if len(list1) == 0:
            return []
        if len(list2) == 0:
            return []

    i: int = 0
    while i < len(list2):
        list1.append(list2[i])
        i+=1
    return list1


def sub(num_list: list[int], start: int, end: int) -> int:
    """Returns a list which is a subset of the given list, between the specified start index and the end index - 1"""
    sublist: str = []

    if start < 0:
        start = 0
    if end > len(num_list):
        end = len(num_list) - 1

    if len(num_list) == 0 or start > len(num_list) or end < 0:
        return sublist
    else:
        while start < end:
            sublist.append(num_list[start])
            start+=1
        return sublist