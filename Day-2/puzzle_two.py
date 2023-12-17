"""
https://adventofcode.com/2023/day/2#part2
"""
from cubedraw import get_cube_draw


raw_data = []
with open('input', 'rt', encoding='utf8') as input_file:
    raw_data = input_file.readlines()
games = len(raw_data) * [None]
for line_number, line in enumerate(raw_data):
    line = line.rstrip('\n')
    line = line[line.index(': ') + 2:]
    line = line.split('; ')
    MAX_RED = MAX_GREEN = MAX_BLUE = -1
    for cube_draw in line:
        cubes = get_cube_draw(cube_draw.split(', '))
        MAX_RED = max(MAX_RED, cubes.red)
        MAX_GREEN = max(MAX_GREEN, cubes.green)
        MAX_BLUE = max(MAX_BLUE, cubes.blue)
    game_min_power = MAX_RED * MAX_GREEN * MAX_BLUE
    games[line_number] = game_min_power
print(sum(games))
