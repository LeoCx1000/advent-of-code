import itertools
from typing import Literal

from aoc import input_for


def get(matrix: list[list[str]], pos: complex):
    x = int(pos.real)
    y = int(pos.imag)
    if (x < 0) or (y < 0):
        return None
    try:
        return matrix[y][x]
    except IndexError:
        return None


def checked_neighbours(pos: complex) -> list[complex]:
    if not (pos.real or pos.imag):
        return [x for x in map(lambda v: complex(*v), itertools.product([0, 1, -1], [0, 1, -1])) if x]
    return [
        complex(
            pos.real + (pos.real and (1 if pos.real > 0 else -1)),
            pos.imag + (pos.imag and (1 if pos.imag > 0 else -1)),
        )
    ]


def check_surroundings(matrix: list[list[str]], position: complex, relative: complex, check_for: str) -> int:
    current = get(matrix, position + relative)

    if current != check_for:
        return 0

    if (current := get(matrix, position + relative)) == "S" and check_for == "S":
        return 1

    return sum(
        check_surroundings(matrix, position, coord, "XMAS"["XMAS".index(check_for) + 1])
        for coord in checked_neighbours(relative)
    )


def pt_1():
    puzzle_in = [list(x) for x in input_for(day=4, year=2024).splitlines()]

    count = 0
    for y in range(len(puzzle_in)):
        for x in range(len(puzzle_in[y])):
            count += check_surroundings(puzzle_in, complex(x, y), 0 + 0j, check_for="X")

    return count


def get_corners(matrix: list[list[str]], coord: complex) -> list[str] | Literal[False]:
    corners = [get(matrix, coord) for coord in [coord - 1 + 1j, coord + 1 + 1j, coord - 1 - 1j, coord + 1 - 1j]]
    return all(corners) and corners  # type: ignore  # type checker is dumb!!


def pt_2():
    puzzle_in = [list(x) for x in input_for(day=4, year=2024).splitlines()]

    count = 0
    for y in range(len(puzzle_in)):
        for x in range(len(puzzle_in[y])):
            position = complex(x, y)

            if get(puzzle_in, position) != 'A':
                continue

            corners = get_corners(puzzle_in, position)
            if not corners:
                continue

            if ''.join(corners) in ['MSMS', 'MMSS', 'SMSM', 'SSMM']:
                count += 1

    return count


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())
