from aoc import input_for


def pt_1():
    puzzle_in = input_for(day=1, year=2024)

    left_list = []
    right_list = []

    for line in puzzle_in.splitlines():
        left, _, right = line.partition(' ')
        left_list.append(int(left.strip()))
        right_list.append(int(right.strip()))

    left_list.sort()
    right_list.sort()

    ret = 0
    for left, right in zip(left_list, right_list):
        ret += abs(left - right)

    return ret


def pt_2():
    puzzle_in = input_for(day=1, year=2024)

    left_list = []
    right_list = []

    for line in puzzle_in.splitlines():
        left, _, right = line.partition(' ')
        left_list.append(int(left.strip()))
        right_list.append(int(right.strip()))

    left_list.sort()
    right_list.sort()

    ret = 0
    for num in left_list:
        ret += num * right_list.count(num)

    return ret


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())
