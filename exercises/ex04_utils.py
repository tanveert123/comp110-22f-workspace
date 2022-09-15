"""EX04 - 'List' Utility Functions""" 


__author__ = "730578741"


def all(ints: list[int], num: int) -> bool:
    i: int = 0

    while i < len(ints):
        if num != ints[i]:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    i: int = 0
    max_value = input[i]
    number = input[i+1]

    while i < len(input):
        if max_value < number:
            max_value = number
        i += 1
    print(max_value)


def is_equal(a: list[int], b: list[int]) -> bool:
    assert len(a) == len(b)

    i: int = 0
    while i < len(a):
        if a[i] != b[i]:
            return False
        i += 1
    else:
        return True