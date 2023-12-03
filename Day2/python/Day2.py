import re

from common.common import path


def setup(file):
    data = path(file,"Day2")
    cleaned_data = [re.sub(r"Game \d+: ", "", game) for game in data]
    counter = 0
    power = 0
    tracker = []
    return cleaned_data, counter, power, tracker


def part_1(file):
    cleaned_data, counter, power, tracker = setup(file)
    color_thresholds = {'red': 13, 'green': 14, 'blue': 15}
    for index, element in enumerate(cleaned_data, start=1):
        game_set = [game.split(",") for game in element.split(";")]
        if all(
                all(int(value) < color_thresholds.get(color, float('inf')) for value, color in
                    (c.strip().split() for c in game))
                for game in game_set
        ):
            tracker.append(index)
    return sum(tracker)


def part_2(file):
    cleaned_data, counter, power, tracker = setup(file)
    for element in cleaned_data:
        counter += 1
        game_set = [game.split(",") for game in str(element).split(";")]
        colors = {'red': 0, 'green': 0, 'blue': 0}
        for game in game_set:
            for c in game:
                value, color = map(str.strip, c.split())
                if color in colors:
                    colors[color] = max(colors[color], int(value))
        power += colors['red'] * colors['green'] * colors['blue']
    return power


if __name__ == '__main__':
    print(f"Part 1:{part_1('part1.txt')}")
    print(f"Part 2:{part_2('part1.txt')}")
