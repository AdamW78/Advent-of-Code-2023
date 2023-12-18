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


def example_read():
    """
    Reads example input, returns an array of strings (lines)
    :return: list of strings (lines)
    """
    with open('example_input', 'rt', encoding='utf8') as example_input_file:
        example_input_arr = example_input_file.readlines()
        return example_input_arr
