

def get_diffs(seq):
    diffs = []
    for i in range(len(seq) - 1):
        diffs.append(seq[i + 1] - seq[i])
    return diffs


def calc_diff_list(seq):
    diff_list = [seq]
    diffs = seq
    while any(diffs):
        diffs = get_diffs(diffs)
        if any(diffs):
            diff_list.append(diffs)
    return diff_list
    

def calc_next_value(seq):
    diff_list = calc_diff_list(seq)
    # print(f'diff_list: {diff_list}')
    next_val = diff_list.pop()[0]
    diff_list.reverse()
    for diffs in diff_list:
        next_val = diffs[0] - next_val
        # print(next_val)
    # print(f'next_val: {next_val} | {seq}')
    return next_val


def solution(lines):
    val_list = []
    for line in lines:
        seq = [int(x) for x in line.strip().split()]
        val_list.append(calc_next_value(seq))
    return sum(val_list)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))