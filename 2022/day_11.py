from aoc import input_for

import re

pattern = re.compile(
    r"""Monkey \d+:
  Starting items: (?P<ITEMS>.*)
  Operation: new = (?P<OPE>.*)
  Test: divisible by (?P<TEST>\d+)
    If true: throw to monkey (?P<TRUE>\d+)
    If false: throw to monkey (?P<FALSE>\d+)"""
)


class Monkey:
    def __init__(self, starting_items: list[int], operation: str, test_op: int, true: int, false: int) -> None:
        self.items = starting_items
        self.operation = operation
        self.div_by = test_op
        self.true = true
        self.false = false
        self.inspected: int = 0


def makemonkeys(inp: str) -> list[Monkey]:
    monkeys: list[Monkey] = []
    for match in pattern.finditer(inp):
        ret = [i.strip() for i in match.group('ITEMS').split(',')]
        monkeys.append(
            Monkey(
                starting_items=list(map(int, ret)),
                true=int(match.group('TRUE')),
                false=int(match.group('FALSE')),
                test_op=int(match.group('TEST')),
                operation=match.group('OPE'),
            )
        )
    return monkeys


def pt_1():
    monkeys = makemonkeys(input_for(day=11))
    for _ in range(20):
        for m in monkeys:
            for old in m.items:  # type: ignore  # it is accessed in eval()
                m.inspected += 1
                new = int(eval(m.operation)) // 3
                if new % m.div_by == 0:
                    monkeys[m.true].items.append(new)
                else:
                    monkeys[m.false].items.append(new)
            m.items = []
    s = sorted([m.inspected for m in monkeys], reverse=True)
    return s[0] * s[1]


def pt_2():
    monkeys = makemonkeys(input_for(day=11))
    mdl = 1
    for m in monkeys:
        mdl = mdl * m.div_by
    for _ in range(10_000):
        for m in monkeys:
            for old in m.items:  # type: ignore  # it is accessed in eval()
                m.inspected += 1
                new = int(eval(m.operation)) % mdl
                if new % m.div_by == 0:
                    monkeys[m.true].items.append(new)
                else:
                    monkeys[m.false].items.append(new)
            m.items = []
    s = sorted([m.inspected for m in monkeys], reverse=True)
    return s[0] * s[1]


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())
