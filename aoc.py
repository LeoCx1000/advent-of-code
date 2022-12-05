import requests, datetime


def get_session() -> str:
    with open(".session", "r") as fp:
        return fp.read().strip()


def input_for(day: int | None = None) -> str:
    day = day or datetime.datetime.now().day
    cookies = {"session": get_session()}
    url = f"https://adventofcode.com/2022/day/{day}/input"
    resp = requests.get(url, cookies=cookies)
    resp.raise_for_status()
    return resp.text


if __name__ == "__main__":
    import os

    today = datetime.datetime.now().day
    template = """from aoc import input_for

def pt_1():
    puzzle_in = input_for(day={day})

def pt_2():
    puzzle_in = input_for(day={day})

if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())"""
    with open(f"day_{today}.py", "w") as file:
        file.write(template.format(day=today))
    print("Created a new file for today!")
