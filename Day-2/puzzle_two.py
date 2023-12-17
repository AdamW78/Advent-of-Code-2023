from cubedraw import get_cube_draw

raw_data = []
with open('input', 'rt', encoding='utf8') as input_file:
    raw_data = input_file.readlines()
games = len(raw_data) * [None]
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
