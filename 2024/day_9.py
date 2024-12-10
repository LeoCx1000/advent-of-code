from functools import reduce
from itertools import chain

from aoc import input_for


def pt_1():
    puzzle_in = map(int, input_for(day=9, year=2024).strip())
    array = list(chain(*[[('.' if idx % 2 else str(idx // 2))] * n for idx, n in enumerate(puzzle_in)]))

    lhs, rhs = 0, len(array) - 1
    while lhs < rhs:
        if array[lhs] != '.':
            lhs += 1
        if array[rhs] == '.':
            rhs -= 1
        if array[lhs] == '.' and array[rhs] != '.':
            array[lhs], array[rhs] = array[rhs], array[lhs]

    array = array[: array.index('.')]

    return reduce(lambda x, y: x + (int(y[1]) * y[0]), enumerate(array), 0)


def pt_2():
    puzzle_in = list(map(int, input_for(day=9, year=2024).strip()))
    array = list(chain(*[[('.' if idx % 2 else str(idx // 2))] * n for idx, n in enumerate(puzzle_in)]))

    current_num = '.'
    starting_idx = len(array) - 1

    for idx, num in reversed(list(enumerate(array))):
        if num == current_num:
            continue

        if current_num != '.':
            span = starting_idx - idx

            found_idx = None
            for i in range(0, idx + span):
                if array[i] == '.':
                    if not found_idx:
                        found_idx = i
                    if i - found_idx + 1 == span:
                        break
                else:
                    found_idx = None
            else:
                found_idx = None

            if found_idx:
                current = slice(idx + 1, idx + span + 1)
                new = slice(found_idx, found_idx + span)
                array[current], array[new] = array[new], array[current]

        current_num = num
        starting_idx = idx

    return reduce(lambda x, y: x + (int(y[1] if y[1] != '.' else 0) * y[0]), enumerate(array), 0)


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())
