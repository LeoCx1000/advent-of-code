def pt_1(puzzle_in: str):
    ranges, fresh = puzzle_in.strip().split("\n\n")
    fresh_ranges = [
        range(int(n1), int(n2) + 1)
        for n1, n2 in map(lambda r: r.split("-"), ranges.splitlines())
    ]

    count = 0
    for ingredient in map(int, fresh.splitlines()):
        if any(ingredient in range for range in fresh_ranges):
            count += 1
    return count


def pt_2(puzzle_in: str):
    ranges, _ = puzzle_in.strip().split("\n\n")
    ranges = [
        [int(n1), int(n2)]
        for n1, n2 in map(lambda r: r.split("-"), ranges.splitlines())
    ]
    old_length = len(ranges)
    new_length = 0
    while old_length != new_length:
        valid_ranges: list[list[int]] = []
        for start, end in ranges:
            for idx, (valid_start, valid_end) in enumerate(valid_ranges):
                if (start >= valid_start) and (end <= valid_end):
                    break  # Set is subset of valid set. (early break)
                elif start > valid_end:
                    continue  # Range ahead of current valid range.
                elif (start <= valid_start) and (end >= valid_end):
                    valid_ranges[idx] = [start, end]
                elif (start <= valid_start) and (end >= valid_end):
                    valid_ranges[idx][0] = start
                elif (start >= valid_start) and (start <= valid_end):
                    valid_ranges[idx][1] = end
                elif (start < valid_start) and (end < valid_end):
                    valid_ranges.insert(idx, [start, end])
                else:
                    raise Exception("How did we get here?")
                break
            else:
                # We are at the end of the valid ranges
                valid_ranges.append([start, end])

        old_length = new_length
        new_length = len(valid_ranges)
        ranges = valid_ranges
    return sum(stop - start + 1 for start, stop in ranges)


pt_1_oneline = lambda puzzle_in: ...
pt_2_oneline = lambda puzzle_in: ...


if __name__ == "__main__":
    from aoc import input_for

    puzzle_in = input_for(day=5, year=2025)
    print("part one: ", pt_1(puzzle_in), pt_1_oneline(puzzle_in))
    print("part two: ", pt_2(puzzle_in), pt_2_oneline(puzzle_in))
