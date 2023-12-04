from aoc import input_for

import re


def parse_drawing(input: str) -> dict[int, list]:
    pattern = re.compile(r"^(.{3}) ?", flags=re.MULTILINE)
    ret = {}
    while input.strip():
        *boxes, number = pattern.findall(input)
        crates = []
        for box in boxes:
            if box.strip():
                crates.append(box.strip("[]"))
        ret[int(number.strip())] = list(reversed(crates))
        crates = []
        input = pattern.sub("", input)
    return ret


def get_moves(step) -> list[int]:
    pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")
    return [int(x) for x in pattern.findall(step)[0]]


def pt_1():
    puzzle_in = input_for(day=5)
    drawing, steps = puzzle_in.split("\n\n")
    stacks = parse_drawing(drawing)
    for amt, frm, to in map(get_moves, steps.splitlines()):
        stacks[to] += reversed(stacks[frm][-amt:])
        stacks[frm] = stacks[frm][:-amt]
    return "".join([str(x[-1]) for x in stacks.values()])


def pt_2():
    puzzle_in = input_for(day=5)
    drawing, steps = puzzle_in.split("\n\n")
    stacks = parse_drawing(drawing)
    for amt, frm, to in map(get_moves, steps.splitlines()):
        stacks[to] += stacks[frm][-amt:]
        stacks[frm] = stacks[frm][:-amt]
    return "".join([str(x[-1]) for x in stacks.values()])


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())
