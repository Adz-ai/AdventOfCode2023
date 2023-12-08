from math import lcm

from common.common import path
import itertools


def setup(file):
    data = path(file=file, day="Day8")
    directions = [char for element in data if element and all(char in 'LR' for char in element) for char in element]
    mapping = [element.replace('(', '').replace(')', '').split() for element in data if
               element and not all(char in 'LR' for char in element)]
    return directions, mapping


def part_1(file):
    directions, mapping = setup(file)
    dict_mapping = {row[0]: row[2:] for row in mapping}
    counter = 0
    nxt_element = ""
    for direction in itertools.cycle(directions):
        if counter == 0:
            c = dict_mapping.get("AAA")
            if direction == "L":
                nxt_element = c[0].replace(',', '')
            else:
                nxt_element = c[1]
        elif nxt_element == "ZZZ":
            break
        else:
            c = dict_mapping.get(nxt_element)
            if direction == "L":
                nxt_element = c[0].replace(',', '')
            else:
                nxt_element = c[1]
        counter += 1
    return counter


def part_2(file):
    directions, mapping = setup(file)
    d = {row[0]: (row[2].strip(','), row[3]) for row in mapping}
    results = []
    for key in [k for k in d.keys() if k.endswith("A")]:
        for i, command in enumerate(itertools.cycle(directions), 1):
            key = d[key][command == "R"]
            if key.endswith("Z"):
                results.append(i)
                break
    return lcm(*results)


if __name__ == '__main__':
    print(f"Part 1:{part_1('day8input.txt')}")
    print(f"Part 2: {part_2('day8input.txt')}")
