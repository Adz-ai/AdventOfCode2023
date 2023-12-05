from common.common import get_path, path


def part_1(file):
    seeds, *maps = open(get_path("Day5", file)).read().split('\n\n')

    def lookup(val, m):
        _, *ranges = m.split('\n')
        for r in ranges:
            dst, src, n = map(int, r.split())
            if src <= val < src + n:
                return val - src + dst
        else:
            return val

    seeds = list(map(int, seeds.split()[1:]))
    min_location = float('inf')
    for seed in seeds:
        for m in maps:
            seed = lookup(seed, m)
        if seed < min_location:
            min_location = seed
    return min_location


def part_2(file):
    data = path(file, 'Day5')
    vals, *input_txt = [line.strip("\n") for line in data]
    vals = list(map(int, vals.strip("seeds: ").split()))
    ind = [i for i, x in enumerate(input_txt) if x == ""] + [-1]
    mappings = []
    for i in range(len(ind) - 1):
        mappings.append([list(map(int, line.split())) for line in input_txt[ind[i] + 2:ind[i + 1]]])
    v = [(vals[i], vals[i] + vals[i + 1] - 1) for i in range(0, len(vals), 2)]
    m = [[(s, s + r - 1, d, d + r - 1) for d, s, r in mapping] for mapping in mappings]
    for mapping in m:
        new_v = []
        q = v
        while q:
            x, y = q.pop()
            for s, t, d, e in mapping:
                if y < s or x > t:
                    continue
                if x < s:
                    q.append((x, s - 1))
                if y > t:
                    q.append((t + 1, y))
                new_v.append((max(d, d + x - s), min(d + y - s, e)))
                break
            else:
                new_v.append((x, y))
        v = new_v
    return min(v)[0]


if __name__ == '__main__':
    print(f"Part 1:{part_1('part1.txt')}")
    print(f"Part 2:{part_2('part1.txt')}")
