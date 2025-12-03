import re

def solve(puzzle_in, pattern):
    total = 0
    for id_range in puzzle_in.split(','):
        n1, n2 = id_range.split('-')
        for number in map(str, range(int(n1), int(n2) + 1)):
            if pattern.fullmatch(number):
                total += int(number)
    return total

def pt_1(puzzle_in: str):
    return solve(puzzle_in, re.compile(r"^(\d+)\1$"))


def pt_2(puzzle_in: str):
    return solve(puzzle_in, re.compile(r"^(\d+)\1+$"))


pt_1_oneline = lambda puzzle_in: sum(int(num) for r in puzzle_in.split(',') for num in map(str, range(*map(int, r.split('-'))) )if re.fullmatch(r"^(\d+)\1$", num))
pt_2_oneline = lambda puzzle_in: sum(int(num) for r in puzzle_in.split(',') for num in map(str, range(*map(int, r.split('-'))) )if re.fullmatch(r"^(\d+)\1+$", num))


if __name__ == "__main__":
    from aoc import input_for

    puzzle_in = input_for(day=2, year=2025)
    print("part one: ", pt_1(puzzle_in), pt_1_oneline(puzzle_in))
    print("part two: ", pt_2(puzzle_in), pt_2_oneline(puzzle_in))