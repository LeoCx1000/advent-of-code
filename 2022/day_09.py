from aoc import input_for
from math import dist


def get_directions(ipt: str) -> tuple[str, int]:
    direction, _, amount = ipt.partition(' ')
    return (direction, int(amount))


def move(head, tail) -> bool:
    if dist(head, tail) >= 2.0:

        if head[0] == tail[0]:
            if head[1] > tail[1]:
                tail[1] += 1
            else:
                tail[1] -= 1
        elif head[1] == tail[1]:
            if head[0] > tail[0]:
                tail[0] += 1
            else:
                tail[0] -= 1
        else:
            if head[0] > tail[0]:
                if head[1] > tail[1]:
                    tail[0] += 1
                    tail[1] += 1
                else:
                    tail[0] += 1
                    tail[1] -= 1
            else:
                if head[1] > tail[1]:
                    tail[0] -= 1
                    tail[1] += 1
                else:
                    tail[0] -= 1
                    tail[1] -= 1
        return True
    return False


def pt_1():
    puzzle_in = input_for(day=9)
    visited_positions: set[tuple[int, ...]] = {
        (0, 0),
    }
    head = [0, 0]
    tail = [0, 0]
    for direction, amount in map(get_directions, puzzle_in.splitlines()):
        for _ in range(amount):

            if direction == 'R':
                head[0] += 1
            elif direction == 'L':
                head[0] -= 1
            elif direction == 'U':
                head[1] += 1
            elif direction == 'D':
                head[1] -= 1
            else:
                print('Unknown direction %s' % direction)

            if move(head, tail):
                visited_positions.add(tuple(tail))

    return len(visited_positions)


def pt_2():
    puzzle_in = input_for(day=9)
    visited_positions: set[tuple[int, ...]] = {
        (0, 0),
    }
    snake: list[list[int]] = [[0, 0] for _ in range(10)]
    for direction, amount in map(get_directions, puzzle_in.splitlines()):
        for _ in range(amount):

            if direction == 'R':
                snake[0][0] += 1
            elif direction == 'L':
                snake[0][0] -= 1
            elif direction == 'U':
                snake[0][1] += 1
            elif direction == 'D':
                snake[0][1] -= 1
            else:
                print('Unknown direction %s' % direction)

            for i in range(8):
                move(snake[i], snake[i + 1])

            if move(snake[8], snake[9]):
                visited_positions.add(tuple(snake[9]))

    return len(visited_positions)


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())
