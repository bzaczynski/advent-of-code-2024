from dataclasses import dataclass
from pathlib import Path
from typing import Self


class Report:
    @staticmethod
    def check_safety(levels: list[int]) -> bool:
        deltas = [y - x for x, y in zip(levels, levels[1:])]
        magnitudes = [abs(x) for x in deltas]
        increase = all(x >= 0 for x in deltas)
        decrease = all(x <= 0 for x in deltas)
        monotonic = increase or decrease
        diffs = min(magnitudes) >= 1 and max(magnitudes) <= 3
        return monotonic and diffs

    def __init__(self, line: str) -> None:
        self.levels = [int(line) for line in line.split()]
        self.deltas = [y - x for x, y in zip(self.levels, self.levels[1:])]
        self.magnitudes = [abs(x) for x in self.deltas]

    @property
    def safe(self) -> bool:
        # if self.check_safety(self.levels):
        #     return True
        # else:
        positive = {i for i, x in enumerate(self.deltas) if x > 0}
        negative = {i for i, x in enumerate(self.deltas) if x < 0}
        zeros = {i for i, x in enumerate(self.deltas) if x == 0}

        print(f"{self.levels = }")
        print(f"{self.deltas = }")
        print(f"{self.magnitudes = }")
        print(f"{positive = }")
        print(f"{negative = }")
        print(f"{zeros = }")
        print()

            # levels = self.levels[:]
            # if len(positive) == 1:
            #     levels.pop(positive.pop() + 1)
            #     if self.check_safety(levels):
            #         return True
            #     else:
            #         pass  # TODO check another strategy? or give up?
            # elif len(negative) == 1:
            #     levels.pop(negative.pop())
            # else:
            #     pass  # No element was removed due to ..., so try again

            # return False



@dataclass(frozen=True)
class InputData:
    reports: tuple[Report, ...]

    @classmethod
    def from_file(cls, path: Path) -> Self:
        with path.open(encoding="utf-8") as file:
            return cls(tuple(map(Report, file)))

    def solve_part1(self) -> int:
        return sum(report.safe for report in self.reports)

    def solve_part2(self) -> int:
        ...
        # find the only element that has the opposite sign
        # find the only element that causes too big of a jump (min or max from mags)
        # for report in self.reports:
        #     print(report.levels)
        #     print(report.deltas)
        #     print(report.magnitudes)
        #     print()

        return 0


def main() -> None:
    data = InputData.from_file(Path("sample.txt"))

    for report in data.reports:
        report.safe

    # print(f"Part1: {data.solve_part1()}")
    # print(f"Part2: {data.solve_part2()}")
    # print(data.reports[0].safe2)


if __name__ == "__main__":
    main()
