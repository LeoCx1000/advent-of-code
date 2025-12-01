import datetime
import pathlib

import requests


def get_session(dir: pathlib.Path) -> str:
    with open(dir / ".session", "r") as fp:
        return fp.read().strip()


def input_for(day: int | None = None, year: int | None = None) -> str:
    now = datetime.datetime.now()
    day = day or now.day
    year = year or now.year

    dir: pathlib.Path = pathlib.Path.cwd()
    if dir.name.isdigit():
        dir = dir.parent

    path = dir / f'aoc_cache/{year}-{day}.txt'
    if path.exists():
        return path.open().read()

    cookies = {"session": get_session(dir)}
    url = f"https://adventofcode.com/{year}/day/{day}/input"

    resp = requests.get(url, cookies=cookies)
    resp.raise_for_status()

    path.parent.mkdir(exist_ok=True, parents=True)
    path.write_text(resp.text)

    return resp.text


if __name__ == "__main__":
    import sys

    now = datetime.datetime.now()
    today = sys.argv[1] if len(sys.argv) == 2 else now.day
    year = now.year
    template = """def pt_1(puzzle_in: str):
    pass

def pt_2(puzzle_in: str):
    pass

pt_1_oneline = lambda puzzle_in: ...
pt_2_oneline = lambda puzzle_in: ...


if __name__ == "__main__":
    from aoc import input_for

    puzzle_in = input_for(day={day}, year={year})
    print("part one: ", pt_1(puzzle_in), pt_1_oneline(puzzle_in))
    print("part two: ", pt_2(puzzle_in), pt_2_oneline(puzzle_in))"""

    dir: pathlib.Path = pathlib.Path.cwd()
    if not dir.name.isdigit():
        dir = dir / str(year)

    dir.mkdir(exist_ok=True, parents=True)
    file = dir / f"day_{today:02}.py"
    
    if file.exists():
        print("A file for this day already_exists.")
    else:
        file.write_text(template.format(day=today, year=year))
        print("Created a new file for today!")

    input_for(int(today), year)
