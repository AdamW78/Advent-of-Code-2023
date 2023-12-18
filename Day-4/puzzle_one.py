"""
https://adventofcode.com/2023/day/4#day-desc
"""
from cards import get_card
from read_input import read

CARDS = read()

card_totals = [0] * len(CARDS)
for line_number, line in enumerate(CARDS):
    card = get_card(line)
    card_total = 2 ** (card.num_matches - 1)
    if card_total >= 1:
        card_totals[line_number] = card_total
print(sum(card_totals))
