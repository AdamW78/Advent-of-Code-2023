"""
https://adventofcode.com/2023/day/4#part2
"""
from cards import get_card
from read_input import read

CARDS = read()

for line_number, line in enumerate(CARDS):
    card = get_card(line)
    CARDS[line_number] = card
    for i in range(line_number + 1, line_number + card.num_matches + 1):
        if CARDS[i] is str:
            CARDS[i] = get_card(CARDS[i])
            CARDS[i].num_copies = 1
        else:
            CARDS[i].num_copies += 1
