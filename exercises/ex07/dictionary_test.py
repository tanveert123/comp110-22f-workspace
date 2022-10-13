"""EX03 - Wordle.""" 


__author__ = "730578741"


from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


def test_invert_empty() -> None:
    """Edge case testing for empty a. Should return '[]'."""
    a: dict[str, str] = {}
    assert invert(a) == {}


def test_invert_words_and_nums1() -> None:
    """First use case testing for inverting of dictionary 'a'. Should return '{'z': 'a', 'y': 'b', 'x': 'c'}'."""
    a: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(a) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_words_and_nums2() -> None:
    """First use case testing for inverting of dictionary 'a'. Should return '{'cat': 'apple'}'."""
    a: dict[str, str] = {'apple': 'cat'}
    assert invert(a) == {'cat': 'apple'}


def test__invert_multiple_keys() -> None:
    """Tests with multilpe key values, should return KeyError."""
    with pytest.raises(KeyError):
        a = {'kris': 'jordan', 'michael': 'jordan'}
        invert(a)


def test_favorite_color_empty() -> None:
    """Edge case testing for empty n_and_f. Should return ' '' '."""
    n_and_f: dict[str, str] = {}
    assert favorite_color(n_and_f) == ''


def test_favorite_color_normal1() -> None:
    """First use case testing for function called favorite_color. Should return 'green'."""
    n_and_f: dict[str, str] = {"Marc": "green", "Ezri": "green", "Kris": "blue"}
    assert favorite_color(n_and_f) == "green"


def test_favorite_color_normal2() -> None:
    """Second use case testing for function called favorite_color. Should return 'red'."""
    n_and_f: dict[str, str] = {"Marc": "red", "Ezri": "red", "Kris": "blue"}
    assert favorite_color(n_and_f) == "red"


def test_count_empty() -> None:
    """Edge case testing for empty a. Should return '[]'."""
    num_list: list[str] = []
    assert count(num_list) == {}


def test_count_normal1() -> None:
    """First use case testing for function called count. Should return '{'yellow': 1, 'blue': 1}'."""
    num_list: list[str] = ["yellow", "blue"]
    assert count(num_list) == {'yellow': 1, 'blue': 1}


def test_count_normal2() -> None:
    """Second use case testing for function called count. Should return '{'red': 2, 'green': 2}'."""
    num_list: list[str] = ["red", "red", "green"]
    assert count(num_list) == {'red': 2, 'green': 1}