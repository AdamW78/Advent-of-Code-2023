import math
from typing import List



class CubeDraw:
    def __init__(self):
        self.red = -1
        self.green = -1
        self.blue = -1

    def __str__(self):
        return f"Red Cubes: {self.red}, Green Cubes: {self.green}, Blue Cubes: {self.blue}"


def get_cube_draw(drawn_cube_string: List[str]) -> CubeDraw:
    return_cube_draw = CubeDraw()
    for cube_set in drawn_cube_string:
        red_find = cube_set.rfind("red")
        green_find = cube_set.rfind("green")
        if red_find > 0:
            return_cube_draw.red = int(cube_set[:cube_set.index(" ")])
        elif green_find > 0:
            return_cube_draw.green = int(cube_set[:cube_set.index(" ")])
        else:
            return_cube_draw.blue = int(cube_set[:cube_set.index(" ")])
    return return_cube_draw


raw_data = []
with open('input', 'rt', encoding='utf8') as input_file:
    raw_data = input_file.readlines()
games = len(raw_data)*[None]
for line_number, line in enumerate(raw_data):
    line = line.rstrip('\n')
    line = line[line.index(': ') + 2:]
    line = line.split('; ')
    max_red_cubes = max_green_cubes = max_blue_cubes = -1
    for cube_draw in line:
        cubes = get_cube_draw(cube_draw.split(', '))
        max_red_cubes = max(max_red_cubes, cubes.red)
        max_green_cubes = max(max_green_cubes, cubes.green)
        max_blue_cubes = max(max_blue_cubes, cubes.blue)
    game_min_power = max_red_cubes * max_green_cubes * max_blue_cubes
    games[line_number] = game_min_power
print(sum(games))
