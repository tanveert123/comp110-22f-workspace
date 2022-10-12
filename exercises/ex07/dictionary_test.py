"""EX03 - Wordle.""" 


__author__ = "730578741"


from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Edge case testing for empty a. Should return '[]'."""
    a: dict[str, str] = {}
    assert invert(a) == {}


def test_invert_words_and_nums() -> None:
    """First use case testing for inverting of dictionary 'a'. Should return '{'z': 'a', 'y': 'b', 'x': 'c'}'."""
    a: dict[str, str] = {'a': 'z', 'b' : 'y', 'c': 'x'}
    assert invert(a) == {'z': 'a', 'y': 'b', 'x': 'c'}


# def test_invert_key_error() -> None:
#     """Second use case testing for KeyError. Should return 'KeyError("This function cannot handle having 2 words that are the same! Please use different word!")'."""
#     a: dict[str, str] = {'a': 'z', 'b' : 'y', 'c': 'x'}
#     assert invert(a) == {'z': 'a', 'y': 'b', 'x': 'c'}


# def test_favorite_color_empty() -> None:
#     """Edge case testing for empty n_and_f. Should return '[]'."""
#     n_and_f: dict[str, str] = {}
#     assert favorite_color(n_and_f) == {}


# def test_favorite_color_normal1() -> None:
#     """First use case testing for function called favorite_color. Should return 'blue'."""
#     a: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
#     assert favorite_color(a) == "blue"


# # def test_favorite_color_tie() -> None:
# #     """Second use case testing for function called favorite_color. Should return 'yellow'."""
# #     a: dict[str, str] = {"Marc": "yellow", "Ezri": "red", "Kris": "blue"}
# #     assert favorite_color(a) == "yellow"


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
    num_list: list[str] = ["red", "green", "red", "green"]
    assert count(num_list) == {'red': 2, 'green': 2}
