import re

import regex

NUMBER_MAP = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def extract_number(line):
    digits = regex.findall('(\d|one|two|three|four|five|six|seven|eight|nine)', line, overlapped=True)
    first = digits[0] if digits[0].isdigit() else NUMBER_MAP[digits[0]]
    second = digits[-1] if digits[-1].isdigit() else NUMBER_MAP[digits[-1]]
    number = int(f'{first}{second}')
    print(f'Parsed: {line} | Digits: {digits} | Result: {number}')
    return number


def extract_numbers(line):
    digits = re.findall('(\d|one|two|three|four|five|six|seven|eight|nine)', line)
    first = digits[0] if digits[0].isdigit() else NUMBER_MAP[digits[0]]
    second = digits[-1] if digits[-1].isdigit() else NUMBER_MAP[digits[-1]]
    number = int(f'{first}{second}')
    print(f'Parsed: {line} | Digits: {digits} | Result: {number}')
    return number


def extract_digit_number(line):
    digits = re.findall('\d', line)
    number = int(f'{digits[0]}{digits[-1]}')
    return number


def run():
    numbers = []
    digital_numbers = []
    with open('input.txt') as f:
        for line in f.readlines():
            numbers.append(extract_number(line))
            digital_numbers.append(extract_digit_number(line))

    print(f'Digital Number: {sum(digital_numbers)}')
    return sum(numbers)


if __name__ == '__main__':
    print(run())
