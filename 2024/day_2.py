from aoc import input_for
from operator import gt, lt
from itertools import pairwise


def are_levels_valid(numbers):
    is_ordered = gt if numbers[0] > numbers[1] else lt
    is_valid_distance = lambda n1, n2: 1 <= abs(n1 - n2) <= 3

    for n0, n1 in pairwise(numbers):
        if not is_ordered(n0, n1) or not is_valid_distance(n0, n1):
            return False
    else:
        return True


def pt_1():
    puzzle_in = input_for(day=2, year=2024)

    safe_count = 0

    for line in puzzle_in.splitlines():
        numbers = list(map(int, line.split()))
        safe_count += are_levels_valid(numbers)

    return safe_count


def pt_2():
    puzzle_in = input_for(day=2, year=2024)

    safe_count = 0

    for line in puzzle_in.splitlines():
        numbers = list(map(int, line.split()))
        if are_levels_valid(numbers):
            safe_count += 1
            continue

        for i in range(len(numbers)):
            if are_levels_valid(numbers[:i] + numbers[i + 1 :]):
                safe_count += 1
                break

    return safe_count


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())
