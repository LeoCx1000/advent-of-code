from aoc import input_for

def pt_1():
    puzzle_in = input_for(day=1, year=2025)
    count = 0
    dial = 50
    for rot in puzzle_in.strip().splitlines():
        step = int(rot[1:]) * (-1 if rot[0] == "L" else 1)
        dial = (dial + step) % 100
        if dial == 0:
            count += 1
    return count

def pt_2():
    puzzle_in =  input_for(day=1, year=2025) # 6496
    count = 0
    dial = 50
    for rot in puzzle_in.strip().splitlines():
        step_count = int(rot[1:])
        step_direction = (-1 if rot[0] == "L" else 1)
        step = (step_count % 100) * step_direction

        # Count all full rotations
        count += step_count // 100

        old_position = dial
        new_position = (dial + step)
        dial = new_position % 100

        if dial == 0 or (new_position != dial and old_position != 0):
            count += 1
    return count


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())