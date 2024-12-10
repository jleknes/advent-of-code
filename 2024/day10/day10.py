import fileinput
from typing import List, Set, Tuple
from collections import deque


def read_input() -> List[List[int]]:
    return [[int(x) for x in line.strip()] for line in fileinput.input()]


def move(y: int, x: int, direction: str) -> Tuple[int, int]:
    moves = {
        "NORTH": (-1, 0),
        "EAST": (0, 1),
        "SOUTH": (1, 0),
        "WEST": (0, -1),
    }
    dy, dx = moves[direction]
    return y + dy, x + dx


def score(grid: List[List[int]], start_point: Tuple[int, int], part: str) -> int:
    q = deque([start_point])
    score = 0
    targets_reached: Set[Tuple[int, int]] = set()

    while q:
        y, x = q.popleft()
        if grid[y][x] == 9:
            targets_reached.add((y, x))
            score += 1
        else:
            for direction in ["NORTH", "EAST", "SOUTH", "WEST"]:
                ny, nx = move(y, x, direction)
                if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
                    if grid[ny][nx] == grid[y][x] + 1:
                        q.append((ny, nx))

    return len(targets_reached) if part == "ONE" else score


def get_start_points(grid):
    start_points = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                start_points.append((y, x))
    return start_points


def solve_part_one(grid):
    start_points = get_start_points(grid)
    print(sum(score(grid, start_point, "ONE") for start_point in start_points))


def solve_part_two(grid):
    start_points = get_start_points(grid)
    print(sum(score(grid, start_point, "TWO") for start_point in start_points))


def main() -> None:
    grid = read_input()
    solve_part_one(grid)
    solve_part_two(grid)


if __name__ == "__main__":
    main()
