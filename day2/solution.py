from collections import Counter
from functools import reduce
import re

CONFIG = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def count_colors(dataset):
    counter = Counter(red=0, blue=0, green=0)
    for color in ('red', 'blue', 'green'):
        match = re.search(f'\\d+(?=\\s{color})', dataset)
        if match:
            counter[color] += int(match.group())

    return counter


def determine_if_possible(data, config):
    sets = data.split('; ')
    for dataset in sets:
        color_counts = count_colors(dataset)
        for color, count in color_counts.items():
            if count > config[color]:
                return False
        
    return True


def calculate_cube_power(data):
    min_counter = Counter(red=1, blue=1, green=1)
    sets = data.split('; ')
    for dataset in sets:
        color_counts = count_colors(dataset)
        for color, count in color_counts.items():
            if count > min_counter[color]:
                min_counter[color] = count
    
    return reduce(lambda x,y: x*y, min_counter.values())

def extract_data(line):
     match = re.search(r'(?<=^Game\s)\d+', line)
     game_id = match.group()
     data = line.split(':')[-1].strip()
     return int(game_id), data


def solution(lines, config):
    valid_game_ids = []
    for line in lines:
        game_id, data = extract_data(line)
        if determine_if_possible(data, config):
            valid_game_ids.append(game_id)

    return sum(valid_game_ids)


def new_solution(lines):
    powers = []
    for line in lines:
        _, data = extract_data(line)
        powers.append(calculate_cube_power(data))
    
    return sum(powers)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(new_solution(lines))
