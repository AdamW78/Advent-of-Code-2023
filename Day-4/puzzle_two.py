"""
https://adventofcode.com/2023/day/4#part2
"""
from cards import get_card
from read_input import read

CARDS = read()

for line_number, line in enumerate(CARDS):
    CARD = None
    if line is str:
        CARD = get_card(line)
        CARDS[line_number] = CARD
    else:
        CARD = line
    for i in range(line_number + 1, line_number + CARD.num_matches + 1):
        if CARDS[i] is str:
            CARDS[i] = get_card(CARDS[i])
            CARDS[i].num_copies = 2
        else:
            CARDS[i].num_copies += 1
TOTAL_CARDS = 0
for card in CARDS:
    TOTAL_CARDS += card.num_copies
print(TOTAL_CARDS)
