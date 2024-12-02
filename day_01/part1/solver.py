from pathlib import Path
from typing import NamedTuple, Self


class InputData(NamedTuple):
    left: list[int]
    right: list[int]

    @classmethod
    def from_file(cls, path: Path) -> Self:
        with path.open(encoding="utf-8") as file:
            return cls(*zip(*(map(int, line.split()) for line in file)))

    def solve_part1(self) -> int:
        return sum(
            abs(x - y)
            for x, y in zip(
                sorted(self.left),
                sorted(self.right)
            )
        )

    def solve_part2(self) -> int:
        return sum(
            number * self.right.count(number)
            for number in self.left
        )


def main() -> None:
    data = InputData.from_file(Path("input.txt"))
    print(f"Part1: {data.solve_part1()}")
    print(f"Part2: {data.solve_part2()}")


if __name__ == "__main__":
    main()
