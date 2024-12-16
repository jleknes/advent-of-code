import fileinput
import copy
from collections import deque


def read_input() -> list[list[str]]:
    return [line.strip() for line in fileinput.input()]


def move(y: int, x: int, direction: str) -> tuple[int, int]:
    moves = {
        "UP": (-1, 0),
        "RIGHT": (0, 1),
        "DOWN": (1, 0),
        "LEFT": (0, -1),
    }
    dy, dx = moves[direction]
    return y + dy, x + dx


def rotate(direction: str, clockwise: int) -> str:
    directions = ["UP", "RIGHT", "DOWN", "LEFT"]
    index = directions.index(direction)
    if clockwise:
        return directions[(index + 1) % len(directions)]
    else:
        return directions[(index - 1) % len(directions)]


def solve_part_one(grid):
    start = None
    end = None
    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if square == "S":
                start = (y, x)
            elif square == "E":
                end = (y, x)
            if start and end:
                break
        if start and end:
            break

    q = deque()
    q.append((*start, "RIGHT", 0))
    visited_states = {}

    def get_next_states(y, x, direction, cost):
        next_states = []
        ny, nx = move(y, x, direction)
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] != "#":
            next_states.append((ny, nx, direction, cost + 1))
        for new_direction in (rotate(direction, True), rotate(direction, False)):
            next_states.append((y, x, new_direction, cost + 1000))
        return next_states

    while q:
        y, x, direction, cost = q.popleft()
        for ny, nx, new_direction, new_cost in get_next_states(y, x, direction, cost):
            key = f"{ny},{nx},{new_direction}"
            if key not in visited_states or visited_states[key] > new_cost:
                q.append((ny, nx, new_direction, new_cost))
                visited_states[key] = new_cost

    min_cost = min(
        visited_states.get(f"{end[0]},{end[1]},{direction}", float("inf"))
        for direction in ["UP", "DOWN", "LEFT", "RIGHT"]
    )
    print(min_cost)


def solve_part_two(grid):
    start = None
    end = None
    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if square == "S":
                start = (y, x)
            elif square == "E":
                end = (y, x)
            if start and end:
                break
        if start and end:
            break

    q = deque()
    q.append((*start, "RIGHT", 0))
    visited_states = {}
    paths = {f"{start[0]},{start[1]},RIGHT": {start}}

    def get_next_states(y, x, direction, cost, current_path):
        next_states = []
        ny, nx = move(y, x, direction)
        if grid[ny][nx] != "#":
            next_states.append((ny, nx, direction, cost + 1, current_path | {(ny, nx)}))
        for new_direction in (rotate(direction, True), rotate(direction, False)):
            next_states.append((y, x, new_direction, cost + 1000, current_path))
        return next_states

    while q:
        y, x, direction, cost = q.popleft()
        current_path = paths[f"{y},{x},{direction}"]

        for ny, nx, new_direction, new_cost, new_path in get_next_states(
            y, x, direction, cost, current_path
        ):
            key = f"{ny},{nx},{new_direction}"
            if key not in visited_states or visited_states[key] >= new_cost:
                q.append((ny, nx, new_direction, new_cost))
                if key not in visited_states or visited_states[key] > new_cost:
                    paths[key] = new_path
                elif visited_states[key] == new_cost:
                    paths[key] = paths[key] | new_path
                visited_states[key] = new_cost

    min_cost = min(
        visited_states.get(f"{end[0]},{end[1]},{direction}", float("inf"))
        for direction in ["UP", "DOWN", "LEFT", "RIGHT"]
    )
    print(min_cost)

    winning_path = None
    for direction in ["UP", "DOWN", "LEFT", "RIGHT"]:
        key = f"{end[0]},{end[1]},{direction}"
        if key in visited_states and visited_states[key] == min_cost:
            winning_path = paths[key]
            break
    print(len(winning_path))


def main() -> None:
    grid = read_input()
    solve_part_one(copy.deepcopy(grid))
    solve_part_two(copy.deepcopy(grid))


if __name__ == "__main__":
    main()
