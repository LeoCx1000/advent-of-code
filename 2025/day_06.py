import re
from functools import reduce
from operator import add, mul

def pt_1(puzzle_in: str):
    problems = zip(*[re.split(r"\s+", line.strip()) for line in puzzle_in.splitlines()])
    return sum(reduce([add, mul][vals[-1] == '*'], map(int, vals[:-1])) for vals in problems)


def pt_2(puzzle_in):
    puzzle_in = puzzle_in.splitlines()
    lines = [line + ' ' for line in puzzle_in]
    # Add a white space to avoid a last-element special-case
    total = 0
    numbers = []
    operator = " "
    for *column, op in zip(*lines):
        if all(n==" " for n in column):
            total += reduce([add, mul][operator == '*'], numbers)
            numbers = []
            continue
        if op != ' ':
            operator = op
        numbers.append(int("".join(column)))
    
    return total


pt_1_oneline = lambda puzzle_in: sum(reduce([add, mul][vals[-1] == '*'], map(int, vals[:-1])) for vals in zip(*[re.split(r"\s+", line.strip()) for line in puzzle_in.splitlines()]))
pt_2_oneline = lambda puzzle_in: ...


if __name__ == "__main__":
    from aoc import input_for

    puzzle_in = input_for(day=6, year=2025)
    print("part one: ", pt_1(puzzle_in), pt_1_oneline(puzzle_in))
    print("part two: ", pt_2(puzzle_in), pt_2_oneline(puzzle_in))
