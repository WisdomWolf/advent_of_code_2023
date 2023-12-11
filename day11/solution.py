import itertools
import string

import pandas as pd
import numpy as np


def excel_cols():
    n = 1
    while True:
        yield from (''.join(group) for group in itertools.product(string.ascii_uppercase, repeat=n))
        n += 1


def build_df(lines):
    dict_list = []
    for line in lines:
        dict_list.append({i: c for i, c in enumerate(line.strip())})
    df = pd.DataFrame(dict_list)
    return df


def get_empty_cols(df):
    empty_cols = []
    for col in df.columns:
        values = df[col]
        if all([x == '.' for x in values]):
            empty_cols.append(col)
    return empty_cols

def get_empty_rows(df):
    empty_rows = []
    for row in df.itertuples():
        if all([x == '.' for x in row[1:]]):
            empty_rows.append(row[0])
    return empty_rows


def expand_rows(df, row_list):
    for row in row_list:
        df.loc[row + .5] = ['.'] * df.shape[1]
    df = df.sort_index().reset_index(drop=True)
    return df


def expand_cols(df, col_list):
    offset = 1
    df = df.copy()
    for col in col_list:
        pos = col + offset
        df.insert(pos, col + .5, ['.'] * df.shape[0])
        offset += 1

    col_map = {col: i for i, col in enumerate(df.columns)}
    df = df.rename(columns=col_map)

    return df


def expand_df(df):
    empty_cols = get_empty_cols(df)
    df = expand_cols(df, empty_cols)

    empty_rows = get_empty_rows(df)
    df = expand_rows(df, empty_rows)

    return df


def get_galaxy_coords(df):
    coords = []
    for row in df.itertuples():
        arr = np.array(row)
        if '#' in arr:
            y = row[0]
            for x in np.where(arr == '#')[0]:
                coords.append(np.array((x, y)))
    return coords


def calc_distance(point_one, point_two):
    return np.sum(np.abs(point_one - point_two))


def calc_total_distances(coord_list):
    total_distance = 0
    coords = coord_list.copy()
    while coords:
        point_one = coords.pop()
        for point_two in coords:
            total_distance += calc_distance(point_one, point_two)
    return total_distance


def solution(lines):
    df = build_df(lines)
    df = expand_df(df)
    coords = get_galaxy_coords(df)
    total_sum = calc_total_distances(coords)
    
    return total_sum


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))
