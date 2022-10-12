def count(str_list: list[str]) -> dict[str, int]:
    """Given a list[str], count will produce a dictionary of [str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    input_dict = {}
    
    for i in str_list:
        if str_list[i] not in input_dict:
            input_dict[str_list[i]] = 1
        else:
            input_dict[str_list[i]] += 1
    return input_dict
