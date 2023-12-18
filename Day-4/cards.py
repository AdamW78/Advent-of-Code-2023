"""
Used to read in cards from https://adventofcode.com/2023/day/4
"""
from collections import namedtuple


def get_card(line) -> namedtuple("Card", "num_copies num_matches"):
    """
    Parse a line, transform into Card namedtuple object
    :param line: Line to parse
    :return: Card namedtuple
    """
    Card = namedtuple("Card", "num_copies num_matches")
    line = line[line.index(': ') + 2:]
    line = line.split(' | ')
    winning_numbers = [int(x) for x in line[0].split(' ') if x]
    card_numbers = [int(x) for x in line[1].split(' ') if x]
    num_matches = 0
    for number in card_numbers:
        if number in winning_numbers:
            num_matches += 1
    return Card(0, num_matches)
