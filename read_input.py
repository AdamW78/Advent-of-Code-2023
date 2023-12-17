"""
Universal code to read input and return as an array
"""


def read():
    """
    Reads input, returns an array of strings (lines)
    :return: list of strings (lines)
    """
    with open('input', 'rt', encoding='utf8') as input_file:
        input_arr = input_file.readlines()
        return input_arr
