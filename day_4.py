from aoc import input_for


def make_pairs(pair_in: str) -> list[list[int]]:
    return [[int(z) for z in y.split("-")] for y in pair_in.split(",")]


def pt_1():
    overlapped = 0
    puzzle_in = input_for(day=4)
    mapping = map(make_pairs, puzzle_in.splitlines())
    for (start_1, end_1), (start_2, end_2) in mapping:
        if (start_1 >= start_2 and end_1 <= end_2) or (
            start_1 <= start_2 and end_1 >= end_2
        ):
            overlapped += 1
    return overlapped


def pt_2():
    overlapped = 0
    puzzle_in = input_for(day=4)
    mapping = map(make_pairs, puzzle_in.splitlines())
    for (start_1, end_1), (start_2, end_2) in mapping:
        if start_1 <= end_2 and start_2 <= end_1:
            overlapped += 1
    return overlapped


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())
