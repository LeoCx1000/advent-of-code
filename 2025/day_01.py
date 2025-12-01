from aoc import input_for

def pt_1():
    puzzle_in = input_for(day=1, year=2025)
    count, dial = 0, 50
    for rot in puzzle_in.strip().splitlines():
        step = int(rot[1:]) * (-1 if rot[0] == "L" else 1)
        dial = (dial + step) % 100
        count += dial == 0
    return count

def pt_2():
    puzzle_in =  input_for(day=1, year=2025) # 6496
    count, dial = 0, 50
    for rot in puzzle_in.strip().splitlines():
        steps, step_count = divmod(int(rot[1:]), 100)
        step_direction = (-1 if rot[0] == "L" else 1)
        step = step_count * step_direction
        old_pos, new_pos = dial, (dial + step)
        dial = new_pos % 100
        count += steps + (dial == 0 or (new_pos != dial and old_pos != 0))

    return count


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())