from word2number import w2n

from common.common import path


def find_number_in_string(s, reverse: bool):
    if reverse:
        s = s[::-1]
    try:
        number = w2n.word_to_num(s)
        if 0 <= number <= 9:
            return number
        else:
            return None
    except ValueError:
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                try:
                    number = w2n.word_to_num(s[i:j])
                    return number
                except ValueError:
                    continue
    return None


def part_2(file):
    num_in_str = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    rev_num_in_str = [element[::-1] for element in num_in_str]
    data = path(file, "Day1")

    def extract_numbers(element, reverse=False):
        words = rev_num_in_str if reverse else num_in_str
        temp, ram = [], ""
        for c in reversed(element) if reverse else element:
            ram += c
            if any(num in ram for num in words) or c.isnumeric():
                number = str(find_number_in_string(ram, reverse)) if not c.isnumeric() else c
                temp.append(number)
                ram = ""
        return temp

    final_numbers = []
    for element in data:
        forward_nums = extract_numbers(element)
        reverse_nums = extract_numbers(element, True)
        number_str = forward_nums[0]
        if reverse_nums or len(forward_nums) > 1:
            number_str += reverse_nums[0] if reverse_nums else forward_nums[-1]
        else:
            number_str += forward_nums[0]
        final_numbers.append(int(number_str))
    return sum(final_numbers)


def part_1(file):
    data = path(file, "Day1")

    def extract_number(element):
        nums = [c for c in element if c.isnumeric()]
        return int(nums[0] + nums[-1]) if len(nums) > 1 else int(nums[0] * 2)

    final_numbers = [extract_number(element) for element in data]
    return sum(final_numbers)


if __name__ == '__main__':
    print(f"Part 1:{part_1('day1input.txt')}")
    print(f"Part 2:{part_2('day1input.txt')}")
