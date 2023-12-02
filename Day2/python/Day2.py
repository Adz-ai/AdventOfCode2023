import os
import re
from pathlib import Path


def path(file):
    base_path = os.path.dirname(Path(__file__).parent)
    data = read_file(os.path.join(base_path, "PuzzleInputFiles", file))
    return data


def read_file(file: str) -> list:
    data = open(file, "r").read().splitlines()
    open(file, "r").close()
    return data


def setup(file):
    data = path(file)
    cleaned_data = [re.sub(r"Game \d+: ", "", game) for game in data]
    counter = 0
    power = 0
    tracker = []
    return cleaned_data, counter, power, tracker


def part_1(file):
    cleaned_data, counter, power, tracker = setup(file)
    for element in cleaned_data:
        counter += 1
        game_set = str(element).split(";")
        p = 0
        for game in game_set:
            g = str(game).split(",")
            checkcase = 0
            for c in g:
                a = str(c).strip().split(" ")
                if a[1] == 'red' and int(a[0]) < 13:
                    checkcase += 1
                if a[1] == 'green' and int(a[0]) < 14:
                    checkcase += 1
                if a[1] == 'blue' and int(a[0]) < 15:
                    checkcase += 1
                if checkcase == len(g):
                    p += 1
            if p == len(game_set):
                tracker.append(counter)
    return sum(tracker)


def part_2(file):
    cleaned_data, counter, power, tracker = setup(file)
    for element in cleaned_data:
        counter += 1
        game_set = str(element).split(";")
        max_red = 0
        max_green = 0
        max_blue = 0
        for game in game_set:
            g = str(game).split(",")
            for c in g:
                a = str(c).strip().split(" ")
                if a[1] == 'red' and int(a[0]) > max_red:
                    max_red = int(a[0])
                if a[1] == 'green' and int(a[0]) > max_green:
                    max_green = int(a[0])
                if a[1] == 'blue' and int(a[0]) > max_blue:
                    max_blue = int(a[0])
        power += max_red * max_green * max_blue
    return power


if __name__ == '__main__':
    print(f"Part 1:{part_1('part1.txt')}")
    print(f"Part 2:{part_2('part1.txt')}")
