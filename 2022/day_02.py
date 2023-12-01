from aoc import input_for

puzzle_in = input_for(2)

LOSS = 0
DRAW = 3
WIN = 6


def calculate_outcome(his, mine):
    if his == mine:
        return DRAW
    if (his + 1) % 3 == mine:
        return WIN
    return LOSS


def pt_1():
    scores = []

    for ipt in puzzle_in.splitlines():

        # fmt: off
        answer_mapping = { 
            'A': 0, 'X': 0,  # Rock
            'B': 1, 'Y': 1,  # Paper
            'C': 2, 'Z': 2}  # Scissors
        # fmt: on

        _his, _, _mine = ipt.partition(" ")
        his, mine = answer_mapping[_his], answer_mapping[_mine]

        outcome = calculate_outcome(his, mine)
        scores += [outcome + mine + 1]

    return sum(scores)


def pt_2():
    scores = []

    answer_mapping = {
        "A": 0,  # Rock
        "B": 1,  # Paper
        "C": 2,  # Sciccors
        "X": 2,  # Loss \
        "Y": 0,  # Draw  > For the math
        "Z": 1,  # Win  /
    }

    for ipt in puzzle_in.splitlines():
        _his, _, _out = ipt.partition(" ")
        his, needed_outcome = answer_mapping[_his], answer_mapping[_out]
        mine = (his + needed_outcome) % 3
        outcome = calculate_outcome(his, mine)
        scores += [outcome + mine + 1]

    return sum(scores)


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())
