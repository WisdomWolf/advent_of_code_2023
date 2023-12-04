from collections import defaultdict


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


def calculate_card_total(card_totals, game_number, winning_numbers, your_numbers):
    card_totals[game_number] = card_totals[game_number] + 1
    for _ in range(card_totals[game_number]):
        next_card = game_number + 1
        for num in winning_numbers:
            if num in your_numbers:
                card_totals[next_card] += 1
                next_card += 1


def new_solution(lines):
    card_totals = defaultdict(int)
    for i, line in enumerate(lines, start=1):
        winning_numbers, your_numbers = extract_number_lists(line)
        calculate_card_total(card_totals, i, winning_numbers, your_numbers)
    # print(card_totals)
    return sum(card_totals.values())


def solution(lines):
    points = 0
    for line in lines:
        winning_numbers, your_numbers = extract_number_lists(line)
        points += calculate_points(winning_numbers, your_numbers)
    return points


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(new_solution(lines))
