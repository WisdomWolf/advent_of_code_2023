import itertools

def match(records, nums):
    return nums == [
        sum(1 for _ in grouper)
        for key, grouper in itertools.groupby(records)
        if key == "#"
    ]

def calc_arrangements(records, nums):
    gen = ("#." if letter == "?" else letter for letter in records)
    return sum(match(candidate, nums) for candidate in itertools.product(*gen))


def solution(lines):
    total = 0
    for line in lines:
        records, num_str = line.strip().split()
        nums = [int(x) for x in num_str.split(',')]
        total += calc_arrangements(records, nums)
    return total


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))
