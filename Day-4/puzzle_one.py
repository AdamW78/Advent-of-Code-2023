input_array = None
with open('input', 'rt', encoding='utf8') as input_file:
    input_array = input_file.readlines()

card_totals = [0] * len(input_array)
for line_number, line in enumerate(input_array):
    line = line[line.index(': ') + 2:]
    line = line.split(' | ')
    winning_numbers = [int(x) for x in line[0].split(' ') if x]
    card_numbers = [int(x) for x in line[1].split(' ') if x]
    num_winning_numbers = 0
    for number in card_numbers:
        if number in winning_numbers:
            num_winning_numbers += 1
    card_total = 2 ** (num_winning_numbers - 1)
    if card_total >= 1:
        card_totals[line_number] = card_total
print(sum(card_totals))
