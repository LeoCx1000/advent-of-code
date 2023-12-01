from aoc import input_for
from string import ascii_letters


def pt_1():
    puzzle_in = input_for(3)

    in_common = []
    for rucksack in puzzle_in.splitlines():
        it_amt = len(rucksack)
        cpt_1, cpt_2 = set(rucksack[: it_amt // 2]), set(rucksack[it_amt // 2 :])
        in_common += cpt_1 & cpt_2

    return sum(map(lambda x: ascii_letters.index(x) + 1, in_common))


def pt_2():
    puzzle_in = input_for(3)
    badges = []
    rucks = puzzle_in.splitlines()
    for i in range(0, len(rucks), 3):
        r1, r2, r3 = rucks[i : i + 3]
        badges += set(r1) & set(r2) & set(r3)

    return sum(map(lambda x: ascii_letters.index(x) + 1, badges))


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())
