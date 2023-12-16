from typing import List

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14


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
    game = line_number + 1
    for cube_draw in line:
        cubes = get_cube_draw(cube_draw.split(', '))
        if cubes.red > RED_CUBES or cubes.green > GREEN_CUBES or cubes.blue > BLUE_CUBES:
            game = 0
    games[line_number] = game
print(sum(games))
