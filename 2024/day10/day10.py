import fileinput
from typing import List, Tuple
from collections import deque as queue


def read_input() -> List[List[int]]:
    grid = []
    for line in fileinput.input():
        grid.append([int(x) for x in line.strip()])
    return grid


def move(y, x, direction: str) -> Tuple[int, int]:
    moves = {
        "NORTH": (-1, 0),
        "EAST": (0, 1),
        "SOUTH": (1, 0),
        "WEST": (0, -1),
    }
    dy, dx = moves[direction]
    return y + dy, x + dx


def score(grid, start_point):
    q = queue()
    q.append(start_point)

    score = 0
    while len(q) > 0:
        print(q)
        y, x = q.popleft()
        if grid[y][x] == 9:
            print(y, x, grid[y][x])
            score += 1
        else:
            for direction in ["NORTH", "EAST", "SOUTH", "WEST"]:
                pos = move(y, x, direction)
                # print(y, x, direction, pos)
                if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]):
                    height = grid[pos[0]][pos[1]]
                    # print("height:", height)
                    if height == grid[y][x] + 1:
                        q.append(pos)

        # print("y,x", y, x)
    return score
    # if y > 0 and grid[y-1][x] > grid[y][x]:


def solve_part_one(grid):
    start_points = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                start_points.append((y, x))
    print(grid)
    print(start_points)
    print(score(grid, start_points[0]))
    # for start_point in start_points:
    # print(start_point)
    # print(score(grid, start_point))


def main() -> None:
    grid = read_input()
    solve_part_one(grid)
    # solve_part_two(disk_map)


if __name__ == "__main__":
    main()
