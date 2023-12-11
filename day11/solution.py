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


def expand_rows(df, row_list, multiplier=1):
    df = df.copy()
    for row in row_list:
        base_increment = 1 / (multiplier + 1)
        increment = base_increment
        # print(f'Increment: {increment}')
        for i in range(multiplier):
            # print(f'pass: {i}/{multiplier}')
            # print(f'Inserting new row at {row + increment}')
            df.loc[row + increment] = ['.'] * df.shape[1]
            increment = base_increment + increment
    df = df.sort_index().reset_index(drop=True)
    return df


def build_empty_col_df(row_length, start, multiplier):
    dict_list = []
    for _ in range(row_length):
        dict_list.append({i: '.' for i in range(start, start + multiplier)})
    df = pd.DataFrame(dict_list)
    return df

def expand_cols(df, col_list, multiplier=1):
    df_list = []
    last = -1
    offset = 0
    for col in col_list:
        base_df = df.iloc[:, last + 1:col]
        df_list.append(rename_df(base_df, offset))
        start = col + offset
        new_df = build_empty_col_df(df.shape[0], start, multiplier)
        df_list.append(new_df)
        last = col
        offset = new_df.columns[-1] - last
    base_df = df.iloc[:, last + 1:]
    df_list.append(rename_df(base_df, offset))
    result_df = pd.concat(df_list, axis=1)
    return result_df


def rename_df(df, offset):
    col_map = {
        orig: new 
        for orig, new in zip(
            df.columns,
            [c + offset for c in df.columns]
        )
    }
    return df.rename(columns=col_map)


def expand_df(df, multiplier=1):
    empty_cols = get_empty_cols(df)
    df = expand_cols(df, empty_cols, multiplier)

    empty_rows = get_empty_rows(df)
    df = expand_rows(df, empty_rows, multiplier)

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


def solution(lines, multiplier=1):
    df = build_df(lines)
    df = expand_df(df, multiplier)
    coords = get_galaxy_coords(df)
    total_sum = calc_total_distances(coords)
    
    return total_sum


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))
