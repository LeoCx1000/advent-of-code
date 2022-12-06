from aoc import input_for


def pt_1():
    puzzle_in = input_for(day=6)
    for i in range(4, len(puzzle_in)):
        packet = puzzle_in[i - 4 : i]
        if len(set(packet)) == 4:
            return i


def pt_2():
    puzzle_in = input_for(day=6)
    for i in range(14, len(puzzle_in)):
        packet = puzzle_in[i - 14 : i]
        if len(set(packet)) == 14:
            return i


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())
