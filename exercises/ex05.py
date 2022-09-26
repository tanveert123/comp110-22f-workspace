"""EX04 - 'List' Utility Functions.""" 


__author__ = "730578741"


def only_evens(num_list: list[int]) -> str:
    """Returns all thhe even numbers from list"""
    even_list: str = []
    i: int = 0

    while i < len(num_list):
        if num_list[i] % 2 == 0:
            even_list.append(num_list[i])
        i += 1
    
    print(even_list)


def concat(list1: list[int], list2: list[int]) -> str:
    """Returns an int list that is made by adding the values of the second list immediately to the first list"""
    print(list1 + list2)


def sub(num_list: list[int], start: int, end: int) -> int:
    sublist: str = []

    if start < 0:
        start = 0

    if end > len(num_list):
        end = len(num_list) - 1
    
    if len(num_list) == 0 or start > len(num_list) or end < 0:
        print(sublist)

    while start < end:
        sublist.append(num_list[start])
        start+=1
    print(sublist)
    
    
