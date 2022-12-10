from aoc import input_for
import numpy as np


def pt_1():
    puzzle_in = input_for(day=10)
    X = 1
    C = 0
    ret = 0
    rng = range(20, len(puzzle_in), 40)
    for instr in puzzle_in.splitlines():
        C += 1
        if C in rng:
            ret += C * X
        match instr.split(' '):
            case ['addx', amount]:
                C += 1
                if C in rng:
                    ret += C * X
                X += int(amount)
    return ret


def pt_2():
    puzzle_in = input_for(day=10)
    X = 1
    C = 0
    screen = []
    for instr in puzzle_in.splitlines():
        screen.append('#' if C % 40 in range(X - 1, X + 2) else '.')
        C += 1
        match instr.split(' '):
            case ['addx', amount]:
                screen.append('#' if C % 40 in range(X - 1, X + 2) else '.')
                C += 1
                X += int(amount)
    arr = np.array(screen).reshape((len(screen) // 40, 40))
    return '\n' + '\n'.join(''.join(x) for x in arr)


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())
