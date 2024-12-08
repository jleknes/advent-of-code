import fileinput
import itertools
from typing import Tuple, Dict, List

def read_input() -> Tuple[Tuple[int, int], Dict[str, List[Tuple[int, int]]]]:
    lines = [line.strip() for line in fileinput.input()]
    grid_size = (len(lines), len(lines[0]) if lines else 0)
    antennas = {}

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != ".":
                antennas.setdefault(char, []).append((i, j))

    return grid_size, antennas

def solve_part_one(grid_size: Tuple[int, int], antennas: Dict[str, List[Tuple[int, int]]]) -> None:
    antinodes = set()
    for key, positions in antennas.items():
        for pair in itertools.combinations(positions, 2):
            dy, dx = pair[0][0] - pair[1][0], pair[0][1] - pair[1][1]
            new_antinodes = [(pair[0][0] + dy, pair[0][1] + dx), (pair[1][0] - dy, pair[1][1] - dx)]
            antinodes.update(
                antinode for antinode in new_antinodes
                if 0 <= antinode[0] < grid_size[0] and 0 <= antinode[1] < grid_size[1]
            )
    print(len(antinodes))

def solve_part_two(grid_size: Tuple[int, int], antennas: Dict[str, List[Tuple[int, int]]]) -> None:
    antinodes = set()
    for key, positions in antennas.items():
        for pair in itertools.combinations(positions, 2):
            dy, dx = pair[0][0] - pair[1][0], pair[0][1] - pair[1][1]
            new_antinodes = {
                (pair[0][0] + i * dy, pair[0][1] + i * dx) for i in range(grid_size[0])
            }.union(
                (pair[1][0] - i * dy, pair[1][1] - i * dx) for i in range(grid_size[0])
            )
            antinodes.update(
                antinode for antinode in new_antinodes
                if 0 <= antinode[0] < grid_size[0] and 0 <= antinode[1] < grid_size[1]
            )
    print(len(antinodes))

def main() -> None:
    grid_size, antennas = read_input()
    solve_part_one(grid_size, antennas)
    solve_part_two(grid_size, antennas)

if __name__ == "__main__":
    main()
