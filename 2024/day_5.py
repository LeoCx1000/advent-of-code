from aoc import input_for


def parse_input(puzzle_in):
    ordering, lists = [section.splitlines() for section in puzzle_in.split('\n\n')]

    ordering_rules = [(int(rule[0]), int(rule[1])) for rule in map(lambda x: x.split('|'), ordering)]
    page_lists = [[int(x) for x in list.split(',')] for list in lists]

    return page_lists, ordering_rules


def get_rules_for(number, page_list, all_rules):
    return [r for r in all_rules if number in r and r[0] in page_list and r[1] in page_list]


def pt_1():
    page_lists, ordering_rules = parse_input(input_for(day=5, year=2024))

    ret = 0
    for page_list in page_lists:
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


def sort_page_list(page_list: list[int], ordering_rules: list[tuple[int, int]]):
    modified = False
    for number in page_list:
        rules = get_rules_for(number, page_list, ordering_rules)

        for rule in rules:
            first_idx, second_idx = map(page_list.index, rule)

            if first_idx > second_idx:
                page_list[first_idx], page_list[first_idx] = page_list[first_idx], page_list[first_idx]

                modified = True

    if modified:
        sort_page_list(page_list, ordering_rules)

    return modified


def pt_2():
    page_lists, ordering_rules = parse_input(input_for(day=5, year=2024))
    ret = 0
    for page_list in page_lists:
        if sort_page_list(page_list, ordering_rules):
            ret += page_list[len(page_list) // 2]
    return ret


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())
