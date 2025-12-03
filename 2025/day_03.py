def solve(puzzle_in: str, length: int):
    total_joltage = 0
    for battery_bank in puzzle_in.splitlines():
        answer = ""
        found_idx = -1
        for i in reversed(range(length)):
            search_bank = battery_bank[found_idx+1:len(battery_bank)-i]
            idx = search_bank.index(max(search_bank))
            answer = answer + max(search_bank)
            found_idx = found_idx + idx + 1
        total_joltage += int(answer)
    return total_joltage

def pt_1(puzzle_in: str):
    return solve(puzzle_in, 2)

def pt_2(puzzle_in: str):
    return solve(puzzle_in, 12)


pt_1_oneline = lambda puzzle_in: ...  # noqa: E731
pt_2_oneline = lambda puzzle_in: ...  # noqa: E731


if __name__ == "__main__":
    from aoc import input_for

    puzzle_in = input_for(day=3, year=2025)
    print("part one: ", pt_1(puzzle_in), pt_1_oneline(puzzle_in))
    print("part two: ", pt_2(puzzle_in), pt_2_oneline(puzzle_in))