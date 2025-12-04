def get_cell(puzzle_in: list[str], pos: complex):
    x, y = int(pos.real), int(pos.imag)
    if (x < 0) or (y < 0):
        return None
    try:
        return puzzle_in[y][x]
    except IndexError:
        return None


def get_surrounding(puzzle_in: list[str], x: int, y: int):
    position = complex(x, y)
    directions = [-1 - 1j, -1 + 0j, -1 + 1j, 0 - 1j, 0 + 1j, 1 - 1j, 1 + 0j, 1 + 1j]
    return [get_cell(puzzle_in, position + d) for d in directions]


def get_movable_locations(puzzle_in: list[str]) -> list[tuple[int, int]]:
    movable = []
    for y, line in enumerate(puzzle_in):
        for x, char in enumerate(line):
            if char == "@":
                surrounding = get_surrounding(puzzle_in, x, y)
                if sum(c == "@" for c in surrounding) < 4:
                    movable.append((x, y))
    return movable


def pt_1(puzzle_in_: str):
    puzzle_in = puzzle_in_.splitlines()
    return len(get_movable_locations(puzzle_in))


def pt_2(puzzle_in_: str):
    puzzle_in = puzzle_in_.splitlines()
    locations = get_movable_locations(puzzle_in)
    count = 0

    while locations:
        for x, y in locations:
            puzzle_in[y] = puzzle_in[y][0:x] + "." + puzzle_in[y][x + 1 :]

        count += len(locations)
        locations = get_movable_locations(puzzle_in)

    return count


pt_1_oneline = lambda puzzle_in: ...
pt_2_oneline = lambda puzzle_in: ...


if __name__ == "__main__":
    from aoc import input_for

    puzzle_in = input_for(day=4, year=2025)
    print("part one: ", pt_1(puzzle_in), pt_1_oneline(puzzle_in))
    print("part two: ", pt_2(puzzle_in), pt_2_oneline(puzzle_in))
