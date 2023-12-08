direction_map = {'L': 0, 'R': 1}

def extract_parts(lines):
    steps = None
    nodes = {}
    for i, line in enumerate(lines):
        line = line.strip()
        if i == 0:
            steps = [l for l in line]
        elif line != '':
            key, coord_str = line.split(' = ')
            coords = tuple(coord_str.strip('()').split(', '))
            nodes[key] = coords
    return steps, nodes


def solution(lines):
    total_steps = 0
    steps, nodes = extract_parts(lines)
    steps = steps * 100
    node = 'AAA'
    for step in steps:
        total_steps += 1
        node = nodes[node][direction_map[step]]
        if node == 'ZZZ':
            break
    return total_steps


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))