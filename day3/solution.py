import re


SYMBOL_MASK = re.compile(r'[\*/\\\!\@\#\$\%\^\&\+\-\_\=]')
DIGIT_MASK = re.compile(r'\d+')


def get_indexes(lines, pattern):
    indexes = []
    for row, line in enumerate(lines):
        matches = list(re.finditer(pattern, line))
        for match in matches:
            span = match.span()
            indexes.append((row, span))

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
    return matrix


def solution(lines):
    part_number_coords = set()
    part_numbers = []

    total_lines = len(lines)
    total_cols = len(lines[0])
    matrix = total_lines, total_cols

    digit_indexes = get_indexes(lines, DIGIT_MASK)
    print('digit_indexes:', digit_indexes)
    digit_matrix = build_matrix(digit_indexes, total_lines)
    print('digit_matrix:', digit_matrix)
    symbol_indexes = get_indexes(lines, SYMBOL_MASK)
    symbol_indexes = [(row, span[0]) for row, span in symbol_indexes]

    print('symbol_indexes:', symbol_indexes)

    for index in symbol_indexes:
        adjacent_cells = find_adjacent_cells(matrix, index)
        adjacency_matrix = build_matrix(adjacent_cells, total_lines)
        for row_number, row in enumerate(adjacency_matrix):
            for col in row:
                possible_adjacent_digits = digit_matrix[row_number]
                # print('poss adj digits:', possible_adjacent_digits)
                for span_start, span_end in possible_adjacent_digits:
                    if span_start <= col <= span_end:
                        part_number_coords.add((row_number, (span_start, span_end)))
    
    for row_number, span in part_number_coords:
        start, end = span
        part_number_str = lines[row_number][start:end]
        part_numbers.append(int(part_number_str))
    print('part_numbers:', part_numbers)
    return sum(part_numbers)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))

