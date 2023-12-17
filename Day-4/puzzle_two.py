"""
https://adventofcode.com/2023/day/4#part2
"""
from read_input import read

INPUT_ARR = read()
card_totals = [0] * len(INPUT_ARR)
for line_number, line in enumerate(INPUT_ARR):
    line = line[line.index(': ') + 2:]
    line = line.split(' | ')
    winning_numbers = [int(x) for x in line[0].split(' ') if x]
    card_numbers = [int(x) for x in line[1].split(' ') if x]
    NUM_WINNING_NUMBERS = 0
    for number in card_numbers:
        if number in winning_numbers:
            NUM_WINNING_NUMBERS += 1
    card_total = 2 ** (NUM_WINNING_NUMBERS - 1)
    if card_total >= 1:
        card_totals[line_number] = card_total
print(sum(card_totals))
