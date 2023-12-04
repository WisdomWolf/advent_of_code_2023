import re


SYMBOL_MASK = re.compile(r'[\*/\\\!\@\#\$\%\^\&]')
DIGIT_MASK = re.compile(r'\d+')


def get_indexes(lines, pattern):
    indexes = []
    for row, line in enumerate(lines):
        matches = list(re.finditer(pattern, line))
        for match in matches:
            span = match.span()
            if span[1] - span[0] > 1:
                indexes.append((row, span))
            else:
                indexes.append((row, span[0]))

    return indexes


def find_adjacent_cells(matrix, position):
    adj = []

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            rangeX = range(0, matrix[0])
            rangeY = range(0, matrix[1])

            (newX, newY) = (position[0]+dx, position[1]+dy)

            if (
                (newX in rangeX)
                and (newY in rangeY)
                and (dx, dy) != (0,0)
            ):
                adj.append((newX, newY))
    return adj


def build_matrix(coord_list, max_rows):
    matrix = [[] for _ in range(max_rows)]
    for row, col in coord_list:
        matrix[row].append(col)


def solution():
    with open('input.txt') as f:
        lines = [l.strip() for l in f.readlines()]
    total_lines = len(lines)
    total_cols = len(lines[0])
    matrix = total_lines, total_cols

    digit_indexes = get_indexes(lines, DIGIT_MASK)
    digit_matrix = build_matrix(digit_indexes, total_lines)
    symbol_indexes = get_indexes(lines, SYMBOL_MASK)

    for index in symbol_indexes:
        adjacent_cells = find_adjacent_cells(matrix, index)
        adjacency_matrix = build_matrix(adjacent_cells, total_lines)
        for row in adjacency_matrix:
            for col in row:
                ...
