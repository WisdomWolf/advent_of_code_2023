from collections import Counter
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


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines, CONFIG))
