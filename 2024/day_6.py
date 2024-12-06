from itertools import cycle

from aoc import input_for
from day_4 import get


class direction:
    up = 0 - 1j
    right = 1 + 0j
    down = 0 + 1j
    left = -1 + 0j


class Tile:
    __slots__ = ('obstacle', 'coordinate', 'visited_directions', 'mock_obstacle')

    def __init__(self, tile: str, coordinate: complex):
        self.coordinate = coordinate
        self.obstacle = tile == "#"
        self.mock_obstacle = False
        self.visited_directions: list[complex] = []
        if tile == '^':
            self.visited_directions.append(direction.up)


class Guard:
    def __init__(self, position: complex):
        self.position = position
        self.direction = direction.up
        self.rotations = cycle([direction.right, direction.down, direction.left, direction.up])

    def move(self, board: list[list[Tile]]):
        position = self.position + self.direction
        next_tile = get(board, position)

        if next_tile and next_tile.obstacle:
            self.direction = next(self.rotations)
        else:
            # The guard can move out of bounds
            self.position = position

        return get(board, self.position)


def pt_1():
    puzzle_in = input_for(day=6, year=2024).strip().splitlines()
    board = [[Tile(tile, complex(x, y)) for x, tile in enumerate(row)] for y, row in enumerate(puzzle_in)]

    guard_position = '\n'.join(puzzle_in).index('^')
    guard = Guard(complex(guard_position % ((len(board[0]) + 1)), (guard_position // len(board)) - 1))

    while current_tile := guard.move(board):
        if guard.direction not in current_tile.visited_directions:
            current_tile.visited_directions.append(guard.direction)
        else:
            break  # we've reached a loop!

    return sum([sum([bool(tile.visited_directions) for tile in row]) for row in board])


def copy_board(board: list[list[Tile]]) -> list[list[Tile]]:
    return [[Tile("#" if tile.obstacle else "", tile.coordinate) for tile in row] for row in board]


def pt_2():
    puzzle_in = input_for(day=6, year=2024).strip().splitlines()
    board = [[Tile(tile, complex(x, y)) for x, tile in enumerate(row)] for y, row in enumerate(puzzle_in)]

    guard_position = '\n'.join(puzzle_in).index('^')
    guard_starting_position = complex(guard_position % ((len(board[0]) + 1)), (guard_position // len(board)) - 1)
    guard = Guard(guard_starting_position)

    current_tile = get(board, guard.position)

    while current_tile:
        # Check if adding a tile would create an infinite loop
        next_pos = guard.position + guard.direction
        new_board = copy_board(board)
        new_tile = get(new_board, next_pos)

        if new_tile and not new_tile.obstacle and not new_tile.mock_obstacle:

            new_tile.obstacle = True
            new_guard = Guard(guard_starting_position)

            while new_current_tile := new_guard.move(new_board):
                if new_guard.direction not in new_current_tile.visited_directions:
                    new_current_tile.visited_directions.append(new_guard.direction)
                else:
                    tile = get(board, next_pos)
                    if tile:
                        tile.mock_obstacle = True
                    print(sum([sum([tile.mock_obstacle for tile in row]) for row in board]), end='\r')
                    break

        current_tile = guard.move(board)
        if current_tile:
            if guard.direction not in current_tile.visited_directions:
                current_tile.visited_directions.append(guard.direction)
            else:
                break  # we've reached a loop!

    return sum([sum([tile.mock_obstacle for tile in row]) for row in board])


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())
