from collections import defaultdict

CATEGORIES = (
    'seed_to_soil',
    'soil_to_fertilizer',
    'fertilizer_to_water',
    'water_to_light',
    'light_to_temperature',
    'temperature_to_humidity',
    'humidity_to_location'
)


def extract_map_args(lines):
    map_args = defaultdict(list)
    for line in lines:
        if 'map' in line:
            var_name = line.split()[0].replace('-', '_')
        elif ':' in line:
            var_name, arg_string = line.split(': ')
            map_args[var_name] = [int(x) for x in arg_string.split()]
        elif line[0] == '\n':
            continue
        else:
            map_args[var_name].append([int(x) for x in line.split()])
    return map_args


def build_maps(map_args):
    maps = defaultdict(list)
    for map_name, args_list in map_args.items():
        if '_' in map_name:
            for args in args_list:
                dest_start, src_start, length = args
                new_tuple = (src_start, src_start + length, dest_start)
                maps[map_name].append(new_tuple)
                maps[map_name].sort()
    return maps


def get_location_for_seed(seed, category_maps):
    result = seed
    for key in CATEGORIES:
        # print(f'calculating {key} for: {result}')
        mapper_ranges = category_maps[key]
        for start, end, dest in mapper_ranges:
            # print(f'mapper range: {start}, {end}, {dest}')
            if start <= result < end:
                offset = result - start
                # print('offset:', offset)
                result = dest + offset
                # print('result found in range')
                break
        else:
            ...
            # print('result not found in any range')
        # print(f'Result: {result}')
    
    return result


def solution(lines):
    locations = []
    map_args = extract_map_args(lines)
    category_maps = build_maps(map_args)
    for seed in map_args['seeds']:
        locations.append(get_location_for_seed(seed, category_maps))
    return sorted(locations)[0]


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))
