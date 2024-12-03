import re

from aoc import input_for


def pt_1():
    puzzle_in = input_for(day=3, year=2024)
    data = re.findall(r"mul\((-?\d+),(-?\d+)\)", puzzle_in)
    return sum(map(lambda x: int(x[0]) * int(x[1]), data))


def pt_2():
    puzzle_in = input_for(day=3, year=2024)
    data = re.findall(r"mul\((-?\d+),(-?\d+)\)|(don't\(\))|(do\(\))", puzzle_in)

    state = True
    ret = 0

    for entry in data:
        if entry[2]:
            state = False
        elif entry[3]:
            state = True
        elif state:
            ret += int(entry[0]) * int(entry[1])

    return ret


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())
