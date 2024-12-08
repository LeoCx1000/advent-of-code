from collections import defaultdict
from itertools import combinations

from aoc import input_for


def pt_1():
    puzzle_in = input_for(day=8, year=2024).strip().splitlines()
    points: defaultdict[str, list[tuple[int, int]]] = defaultdict(list)
    [[p != '.' and points[p].append((x, y)) for x, p in enumerate(r)] for y, r in enumerate(puzzle_in)]
    antinodes = set()
    max_x = len(puzzle_in[0])
    max_y = len(puzzle_in)

    for antennas in points.values():
        for (x1, y1), (x2, y2) in combinations(antennas, 2):
            dx = x1 - x2
            dy = abs(y1 - y2)
            for anx, any in ((x1 + dx, y1 - dy), (x2 - dx, y2 + dy)):
                if (0 <= anx < max_x) and (0 <= any < max_y):
                    antinodes.add((anx, any))

    return len(antinodes)


def pt_2():
    puzzle_in = input_for(day=8, year=2024).strip().splitlines()

    points: defaultdict[str, list[tuple[int, int]]] = defaultdict(list)
    [[p != '.' and points[p].append((x, y)) for x, p in enumerate(r)] for y, r in enumerate(puzzle_in)]
    antinodes = set()
    max_x = len(puzzle_in[0])
    max_y = len(puzzle_in)

    for antennas in points.values():
        for (x1, y1), (x2, y2) in combinations(antennas, 2):
            dx = x1 - x2
            dy = abs(y1 - y2)

            while (0 <= x1 < max_x) and (0 <= y1 < max_y):
                antinodes.add((x1, y1))
                x1, y1 = x1 + dx, y1 - dy

            while (0 <= x2 < max_x) and (0 <= y2 < max_y):
                antinodes.add((x2, y2))
                x2, y2 = x2 - dx, y2 + dy

    return len(antinodes)


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())
