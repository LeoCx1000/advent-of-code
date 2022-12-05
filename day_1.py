from aoc import input_for


def pt_1():
    puzzle_in = input_for(day=1)

    gnomes = [list(map(int, gnome.splitlines())) for gnome in puzzle_in.split("\n\n")]
    return max(map(sum, gnomes))


def pt_2():
    puzzle_in = input_for(day=1)
    gnomes = [list(map(int, gnome.splitlines())) for gnome in puzzle_in.split("\n\n")]
    all_sums = sorted(list(map(sum, gnomes)), reverse=True)
    return sum(all_sums[:3])


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())
