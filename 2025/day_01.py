from functools import reduce


def pt_1(puzzle_in: str):
    count, dial = 0, 50
    for rot in puzzle_in.strip().splitlines():
        step = int(rot[1:]) * (-1 if rot[0] == "L" else 1)
        dial = (dial + step) % 100
        count += dial == 0
    return count


def pt_2(puzzle_in: str):
    count, dial = 0, 50
    for rot in puzzle_in.strip().splitlines():
        steps, step_count = divmod(int(rot[1:]), 100)
        step_direction = -1 if rot[0] == "L" else 1
        step = step_count * step_direction
        old_pos, new_pos = dial, (dial + step)
        dial = new_pos % 100
        count += steps + (dial == 0 or (new_pos != dial and old_pos != 0))
    return count

pt_1_oneline = lambda puzzle_in: reduce(lambda tup, step: (tup[0] + ((new_step:= (tup[1] + step) % 100) == 0), new_step), ((int(rot[1:]) * (-1 if rot[0] == "L" else 1)) for rot in puzzle_in.splitlines()), (0, 50))[0]
pt_2_oneline = lambda puzzle_in: reduce(lambda tup, step: (tup[0] + (step[0] // 100) + (((new_dial:= (tup[1] + ((step[0] % 100) * step[1]))) % 100 == 0) or (tup[1] != 0 and (new_dial != (new_dial % 100)))), new_dial % 100), ((int(rot[1:]), (-1 if rot[0] == "L" else 1)) for rot in puzzle_in.strip().splitlines()), (0, 50))[0]

if __name__ == "__main__":
    from aoc import input_for
    puzzle_in = input_for(day=1, year=2025).strip()
    print("part one: ", pt_1(puzzle_in), pt_1_oneline(puzzle_in))
    print("part two: ", pt_2(puzzle_in), pt_2_oneline(puzzle_in))
