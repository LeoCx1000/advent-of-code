from aoc import input_for


def get_rules_for(number, page_list, all_rules):
    return [r for r in all_rules if number in r and r[0] in page_list and r[1] in page_list]


def pt_1():
    puzzle_in = input_for(day=5, year=2024)
    ordering, lists = [section.splitlines() for section in puzzle_in.split('\n\n')]
    ordering_rules = [[int(part) for part in rule.split('|')] for rule in ordering]

    ret = 0
    for page_list in [list(map(int, l.split(','))) for l in lists]:
        ordered = True
        for number in page_list:
            if not ordered:
                break
            rules = get_rules_for(number, page_list, ordering_rules)
            for rule in rules:
                first, second = rule
                if page_list.index(first) > page_list.index(second):
                    # Ordering broke!
                    ordered = False

        if ordered:
            ret += page_list[len(page_list) // 2]

    return ret


def sort_page_list(page_list, ordering_rules):
    modified = False
    for number in page_list:
        rules = get_rules_for(number, page_list, ordering_rules)

        for rule in rules:
            first, second = rule
            if (fidx := page_list.index(first)) > (sidx := page_list.index(second)):
                page_list[fidx], page_list[sidx] = page_list[sidx], page_list[fidx]
                modified = True
    if modified:
        sort_page_list(page_list, ordering_rules)

    return modified


def pt_2():
    puzzle_in = input_for(day=5, year=2024)
    ordering, lists = [section.splitlines() for section in puzzle_in.split('\n\n')]
    ordering_rules = [[int(part) for part in rule.split('|')] for rule in ordering]

    ret = 0
    for page_list in [list(map(int, l.split(','))) for l in lists]:
        if sort_page_list(page_list, ordering_rules):
            ret += page_list[len(page_list) // 2]
    return ret


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())
