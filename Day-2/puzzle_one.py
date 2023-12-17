from cubedraw import get_cube_draw

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14


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
