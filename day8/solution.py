from math import lcm


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
    starting_nodes = [
        x
        for x in nodes.keys()
        if x.endswith('A')
    ]
    step_counts = []
    
    for node in starting_nodes:
        total_steps = 0
        is_solved = False
        while not is_solved:
            for step in steps:
                total_steps += 1
                node = nodes[node][direction_map[step]]
                if node.endswith('Z'):
                    step_counts.append(total_steps)
                    is_solved = True
                    break

    return lcm(*step_counts)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))