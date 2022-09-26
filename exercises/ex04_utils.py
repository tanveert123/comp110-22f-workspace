"""EX04 - 'List' Utility Functions.""" 


__author__ = "730578741"


def all(ints: list[int], num: int) -> bool:
    """Returns a bool indicating whether or not all the ints in the list are the same as the given int."""
    if len(ints) == 0:
        return False
    
    i: int = 0

    while i < len(ints):
        if num != ints[i]:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Given a list of ints, this function returns the largest value (max) in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    i: int = 0
    max_value = input[i]
    
    while i < len(input):
        if input[i] > max_value:
            max_value = input[i]
        i += 1
    return max_value


def is_equal(a: list[int], b: list[int]) -> bool:
    """Given two lists of int values, function returns True if every element at every index is equal in both lists."""    
    if len(a) == 0 and len(b) == 0:
        return True
    else:
        if len(a) == 0:
            return False
        if len(b) == 0:
            return False
    if len(a) != len(b):
        return False
    
    i: int = 0
    while i < len(a):
        if a[i - 1] != b[i - 1]:
            return False
        i += 1
    else:
        return True