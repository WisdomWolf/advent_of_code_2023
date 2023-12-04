def extract_number_lists(line):
    label, data = line.split(': ')
    winning_numbers, your_numbers = [x.split() for x in data.split(' | ')]
    return winning_numbers, your_numbers


def calculate_points(winning_numbers, your_numbers):
    point_total = 0
    for num in winning_numbers:
        if num in your_numbers:
            point_total = point_total * 2 if point_total > 0 else 1
    return point_total


def solution(lines):
    points = 0
    for line in lines:
        winning_numbers, your_numbers = extract_number_lists(line)
        points += calculate_points(winning_numbers, your_numbers)
    return points


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))
