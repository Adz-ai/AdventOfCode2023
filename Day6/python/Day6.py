import math
import re

from common.common import path


def part_1(file):
    data = path(file, "Day6")
    time, distance = map(lambda td: [int(val) for val in td.split()[1:]],
                         [line for line in data if "Time:" in line or "Distance:" in line])
    return math.prod(sum(1 for x in range(1, t) if x * (t - x) > d) for t, d in zip(time, distance))


def part_2(file): # Using Quadratic Formula For Efficiency
    data = path(file, "Day6")
    time, distance = map(lambda d: int(re.sub(r"\D+", "", d)), data)
    a, b, c = -1, time, -distance
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return 0
    sqrt_discriminant = math.sqrt(discriminant)
    x1, x2 = (-b + sqrt_discriminant) / (2 * a), (-b - sqrt_discriminant) / (2 * a)
    return max(0, min(time, math.floor(max(x1, x2))) - max(1, math.ceil(min(x1, x2))) + 1)


if __name__ == '__main__':
    print(f"Part 1:{part_1('part1.txt')}")
    print(f"Part 2:{part_2('part1.txt')}")
