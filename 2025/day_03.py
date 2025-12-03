from operator import add
from functools import reduce
import time

def pt_1(puzzle_in: str):
    total_joltage=0
    for battery_bank in puzzle_in.splitlines():
        first_number = battery_bank.index(max(battery_bank))
        if first_number + 1 == len(battery_bank):
            second_number = max(battery_bank[:first_number])
            first_number = battery_bank[first_number]
            first_number, second_number = second_number, first_number
        else:
            second_number = max(battery_bank[first_number+1:])
            first_number = battery_bank[first_number]

        total_joltage += int(first_number + second_number)

    return total_joltage

def pt_2(puzzle_in: str):
    total_joltage = 0
    for battery_bank in puzzle_in.splitlines():
        answer = ""
        found_idx = -1
        for i in reversed(range(12)):
            search_bank = battery_bank[found_idx+1:len(battery_bank)-i]
            idx = search_bank.index(max(search_bank))
            answer = answer + max(search_bank)
            found_idx = found_idx + idx + 1
        total_joltage += int(answer)
    return total_joltage



pt_1_oneline = lambda puzzle_in: ...  # noqa: E731
pt_2_oneline = lambda puzzle_in: ...  # noqa: E731


if __name__ == "__main__":
    from aoc import input_for

    puzzle_in = input_for(day=3, year=2025)
    puzzlea_in = """987654321111111
811111111111119
234234234234278
818181911112111"""
    print("part one: ", pt_1(puzzle_in), pt_1_oneline(puzzle_in))
    print("part two: ", pt_2(puzzle_in), pt_2_oneline(puzzle_in))