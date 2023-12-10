import math


direction_map = {
    '|': ((-1, 0), (1, 0)),
    '-': ((0, -1), (0, 1)),
    'L': ((-1, 0), (0, 1)),
    'J': ((0, -1), (-1, 0)),
    '7': ((0, -1), (1, 0)),
    'F': ((0, 1), (1, 0))
}


def calc_offset(start, end):
    return (end[0] - start[0], end[1] - start[1])


def calc_next_coord(start, offset):
    return (start[0] + offset[0], start[1] + offset[1])


def calc_last_coord(end, offset):
    return (end[0] - offset[0], end[1] - offset[1])


def traverse(lines, y, x):
    return lines[y][x]


def get_start_pos(lines):
    for i, line in enumerate(lines):
        if 'S' in line:
            return (i, line.index('S'))

def solution(lines):
    paths = []
    start_pos = get_start_pos(lines)
    
    possible_paths = [
        calc_next_coord(start_pos, (1, 0)),
        calc_next_coord(start_pos, (0, 1))
    ]

    for next_coord in possible_paths:
        paths.append(calc_max_steps(lines, start_pos, next_coord))

    return max(paths)


def calc_max_steps(lines, start, next_coord):
    steps = 1
    last_pos = start
    while next_coord != start:
        next_pipe = traverse(lines, *next_coord)
        print(f'coord: {next_coord} | pipe: {next_pipe}')
        try:
            directions = direction_map[next_pipe]
            if last_pos == calc_next_coord(next_coord, directions[0]):
                last_pos = next_coord
                next_coord = calc_next_coord(last_pos, directions[1])
            elif last_pos == calc_next_coord(next_coord, directions[1]):
                last_pos = next_coord
                next_coord = calc_next_coord(last_pos, directions[0])
            else:
                print(f'FUCK! | last: {last_pos} | next: {next_coord} | {directions}')
                return 0
        except KeyError:
            print('OH NO!')
            return 0
        steps += 1
    return math.ceil(steps / 2)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))