from __future__ import annotations
from aoc import input_for

SizeMap = dict[str, int]


class Path:
    def __init__(self, name: str, parent: Path | None = None) -> None:
        self.name = name
        self.parent: Path | None = parent
        self.children: dict[str, Path] = {}
        self.files: list[int] = []

    def cd(self, child_name: str) -> Path:
        if child_name == "/":
            if not self.parent:
                return self
            return self.parent.cd("/")
        if child_name == "..":
            if self.parent:
                return self.parent
            raise FileNotFoundError
        if path := self.children.get(child_name):
            return path
        raise FileNotFoundError

    def add_child(self, name: str) -> None:
        if name not in self.children:
            self.children[name] = Path(name, self)

    @property
    def qualified_name(self) -> str:
        if self.parent:
            return self.parent.qualified_name + "/" + self.name
        return self.name

    def get_size(self) -> int:
        return sum(self.files) + sum([child.get_size() for child in self.children.values()])

    def get_child_sizes(self) -> dict[str, int]:
        ret: dict[str, int] = {}
        for child in self.children.values():
            ret[child.qualified_name] = child.get_size()
            ret.update(child.get_child_sizes())
        return ret


def parse_commands(input: str) -> Path:
    console_lines = input.splitlines()[1:]
    current = Path("/", parent=None)
    for line in console_lines:
        match line.split(" "):
            case ["$", "cd", path]:
                current = current.cd(path)
            case ["$", "ls"]:
                continue
            case ["dir", dir_name]:
                current.add_child(dir_name)
            case [size, filename]:
                current.files.append(int(size))
    return current.cd("/")


def pt_1():
    puzzle_in = input_for(day=7)
    root = parse_commands(puzzle_in)

    sizes: dict[str, int] = {}
    sizes[root.qualified_name] = root.get_size()
    sizes.update(root.get_child_sizes())
    return sum([x for x in sizes.values() if x <= 100_000])


def pt_2():
    puzzle_in = input_for(day=7)
    root = parse_commands(puzzle_in)

    sizes: dict[str, int] = {}
    sizes[root.qualified_name] = root.get_size()
    sizes.update(root.get_child_sizes())

    FS_SIZE = 70_000_000
    NEEDED = 30_000_000
    CURRENT = root.get_size()
    return min(num for num in sizes.values() if (FS_SIZE - CURRENT) + num >= NEEDED)


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())
