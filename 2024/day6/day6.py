import fileinput
from typing import List, Set, Tuple


def read_input() -> Tuple[Tuple[int, int], Tuple[int, int], List[Tuple[int, int]]]:
    obstacles: List[Tuple[int, int]] = []
    lines = [line.strip() for line in fileinput.input()]
    grid_size = (len(lines), len(lines[0]) if lines else 0)
    start_pos: Tuple[int, int] = (0, 0)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "^":
                start_pos = (i, j)
            elif char == "#":
                obstacles.append((i, j))
    return grid_size, start_pos, obstacles


def rotate(direction: str) -> str:
    directions = {
        "NORTH": "EAST",
        "EAST": "SOUTH",
        "SOUTH": "WEST",
        "WEST": "NORTH",
    }
    return directions[direction]


def next_pos(pos: Tuple[int, int], direction: str) -> Tuple[int, int]:
    moves = {
        "NORTH": (-1, 0),
        "EAST": (0, 1),
        "SOUTH": (1, 0),
        "WEST": (0, -1),
    }
    move = moves[direction]
    return pos[0] + move[0], pos[1] + move[1]


def solve_part_one(
    grid_size: Tuple[int, int],
    start_pos: Tuple[int, int],
    obstacles: List[Tuple[int, int]],
) -> None:
    position = start_pos
    visited: Set[Tuple[int, int]] = {position}
    direction = "NORTH"
    while True:
        print(position, direction)
        next_position = next_pos(position, direction)
        if next_position not in obstacles:
            position = next_position
            if (position, direction) in visited:
                break
            elif 0 <= position[0] < grid_size[0] and 0 <= position[1] < grid_size[1]:
                visited.add((position, direction))
            else:
                break
        else:
            direction = rotate(direction)

    print(len(visited))


def loops(
    grid_size: Tuple[int, int],
    start_pos: Tuple[int, int],
    obstacles: Set[Tuple[int, int]],
) -> bool:
    direction = "NORTH"
    position = start_pos
    visited: Set[Tuple[int, int, str]] = {(position[0], position[1], direction)}
    while True:
        next_position = next_pos(position, direction)
        if next_position not in obstacles:
            position = next_position
            if (position[0], position[1], direction) in visited:
                return True
            elif 0 <= position[0] < grid_size[0] and 0 <= position[1] < grid_size[1]:
                visited.add((position[0], position[1], direction))
            else:
                return False
        else:
            direction = rotate(direction)


def solve_part_two(
    grid_size: Tuple[int, int],
    start_pos: Tuple[int, int],
    obstacles: List[Tuple[int, int]],
) -> None:
    sum_loops = 0
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            if (i, j) not in obstacles:
                loop_obstacles = set(obstacles)
                loop_obstacles.add((i, j))
                if loops(grid_size, start_pos, loop_obstacles):
                    sum_loops += 1
    print(sum_loops)


def print_grid(
    grid_size: Tuple[int, int],
    visited: Set[Tuple[int, int]],
    obstacles: List[Tuple[int, int]],
) -> None:
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            if (i, j) in visited:
                print("X", end="")
            elif (i, j) in obstacles:
                print("#", end="")
            else:
                print(".", end="")
        print()


def main() -> None:
    grid_size, start_pos, obstacles = read_input()
    solve_part_one(grid_size, start_pos, obstacles)
    solve_part_two(grid_size, start_pos, obstacles)


if __name__ == "__main__":
    main()
