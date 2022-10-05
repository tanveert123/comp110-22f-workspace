"""EX05 - Unit Tests.""" 


__author__ = "730578741"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Edge case testing for empty num_list. Should return []."""
    num_list: list[int] = []
    assert only_evens(num_list) == []


def test_only_evens_odds_only() -> None:
    """First use case testing for num_list with only odd numbers. Should return []."""
    num_list: list[int] = [1, 3, 5, 7, 9, 11, 13, 15]
    assert only_evens(num_list) == []


def test_only_evens_both() -> None:
    """Second use case testing for num_list with numbers 1-10. Should return [2,4,6,8,10]."""
    num_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert only_evens(num_list) == [2, 4, 6, 8, 10]


def test_sub_empty() -> None:
    """Edge case testing for empty num_list. Should return []."""
    num_list: list[int] = []
    assert sub(num_list, 1, 3) == []


def test_sub_first_normal1() -> None:
    """First use case testing to make sure that 'sub' function works correctly. Should return [20, 30]."""
    num_list = [10, 20, 30, 40]
    assert sub(num_list, 1, 3) == [20, 30]


def test_sub_second_normal() -> None:
    """Second use case testing to make sure that 'sub' function works correctly. Should return [10, 20, 30]."""
    num_list = [10, 20, 30, 40]
    assert sub(num_list, -1, 3) == [10, 20, 30]


def test_concat_empty() -> None:
    """Edge case testing for 2 empty num_list. Should return []."""
    list1 = []
    list2 = []
    assert concat(list1, list2) == []


def test_concat_normal1() -> None:
    """First use case testing to make sure that 'conact' function works correctly. Should return [1, 2, 3, 4, 5, 6]."""
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    assert concat(list1, list2) == [1, 2, 3, 4, 5, 6]


def test_concat_normal2() -> None:
    """Second use case testing to make sure that 'conact' function works correctly. Should return [40, 50, 60]."""
    list1 = []
    list2 = [40, 50, 60]
    assert concat(list1, list2) == [40, 50, 60]