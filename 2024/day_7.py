import re
from operator import add, mul
from itertools import product
from functools import reduce
from aoc import input_for


def parse_input():
    puzzle_in = input_for(day=7, year=2024).strip().splitlines()
    return [[int(val) for val in re.findall(r'\d+', line)] for line in puzzle_in]


def solve(ops):
    puzzle_in = parse_input()

    ret = 0
    for result, *parts in puzzle_in:
        for arrangement in product(ops, repeat=len(parts) - 1):
            val = reduce(lambda ret, x: arrangement[x[0]](ret, x[1]), enumerate(parts[1:]), parts[0])
            if val == result:
                ret += result
                break
    return ret


def pt_1():
    return solve([add, mul])


def concat_int(x: int, y: int):
    return int(f"{x}{y}")


def pt_2():
    return solve([add, mul, concat_int])


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())
