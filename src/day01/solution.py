"""Advent of Code 2025 - Day 01 Solution"""


def solve_part1(input_data: str) -> int:
    """Solve part 1 of the puzzle."""
    # TODO: Implement solution for part 1
    raise NotImplementedError("Part 1 not implemented yet")


def solve_part2(input_data: str) -> int:
    """Solve part 2 of the puzzle."""
    # TODO: Implement solution for part 2
    raise NotImplementedError("Part 2 not implemented yet")


if __name__ == "__main__":
    import sys
    from pathlib import Path

    # Default to input.txt in the same directory as this script
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
    else:
        input_path = Path(__file__).parent / "input.txt"

    data = input_path.read_text()

    print(f"Part 1: {solve_part1(data)}")
    print(f"Part 2: {solve_part2(data)}")
