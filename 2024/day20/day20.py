import fileinput
from collections import deque


def read_input() -> list[str]:
    return [line.strip() for line in fileinput.input()]


def move(y: int, x: int, direction: str, steps: int) -> tuple[int, int]:
    moves = {
        "UP": (-1, 0),
        "RIGHT": (0, 1),
        "DOWN": (1, 0),
        "LEFT": (0, -1),
    }
    dy, dx = moves[direction]
    return y + dy * steps, x + dx * steps


def bfs(grid, start, end):
    q = deque([(*start, [start])])
    shortest_path = {}
    while q:
        y, x, path = q.popleft()
        if (y, x) == end:
            continue
        for direction in ["UP", "RIGHT", "DOWN", "LEFT"]:
            ny, nx = move(y, x, direction, 1)
            if grid[ny][nx] != "#" and (
                (ny, nx) not in shortest_path
                or len(shortest_path[(ny, nx)]) > len(path) + 1
            ):
                shortest_path[(ny, nx)] = path + [(ny, nx)]
                q.append((ny, nx, path + [(ny, nx)]))
    return shortest_path[end]


def get_start_end(grid):
    start, end = None, None
    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if square == "S":
                start = (y, x)
            elif square == "E":
                end = (y, x)
    return start, end


def solve_part_one(grid):
    def in_grid(y, x):
        return 0 <= y < len(grid) and 0 <= x < len(grid[0])

    start, end = get_start_end(grid)
    shortest_path = bfs(grid, start, end)

    count = sum(
        1
        for i, step in enumerate(shortest_path)
        for direction in ["UP", "RIGHT", "DOWN", "LEFT"]
        if in_grid(*move(step[0], step[1], direction, 1))
        and grid[move(step[0], step[1], direction, 1)[0]][
            move(step[0], step[1], direction, 1)[1]
        ]
        == "#"
        and (ny := move(step[0], step[1], direction, 2)) in shortest_path[i:]
        and (saving := (shortest_path.index(ny) - i) - 2) >= 100
    )

    print("number of shortcuts:", count)


def solve_part_two(grid):
    start, end = get_start_end(grid)
    shortest_path = bfs(grid, start, end)

    count = 0
    cheats = [0] * 10000
    for i, step in enumerate(shortest_path):
        for j in range(i, len(shortest_path)):
            step2 = shortest_path[j]
            step_length = abs(step[0] - step2[0]) + abs(step[1] - step2[1])
            if step_length <= 20 and j - i > step_length:
                cheats[j - i - step_length] += 1
                if j - i - step_length >= 100:
                    count += 1

    print("number of shortcuts saving 100+:", count)


def main() -> None:
    grid = read_input()
    solve_part_one(grid)
    solve_part_two(grid)


if __name__ == "__main__":
    main()
