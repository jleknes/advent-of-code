
import fileinput


def read_input() -> list[list[str]]:
    return [list(line.strip()) for line in fileinput.input()]


def count_adjacent_rolls(grid: list[list[str]], row: int, col: int) -> int:
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            if grid[r][c] == "@":
                count += 1
    return count

def solve_part_one(grid: list[list[str]]) -> int:
    return sum(
        1
        for i, row in enumerate(grid)
        for j, cell in enumerate(row)
        if cell == "@" and count_adjacent_rolls(grid, i, j) < 4
    )


def solve_part_two(grid: list[list[str]]) -> int:
    total = 0
    current_grid = [row[:] for row in grid]
    while solve_part_one(current_grid) > 0:
        new_grid = [row[:] for row in current_grid]
        for i, row in enumerate(current_grid):
            for j, cell in enumerate(row):
                if cell == "@" and count_adjacent_rolls(current_grid, i, j) < 4:
                    new_grid[i][j] = "."
                    total += 1
        current_grid = new_grid
    return total


def main() -> None:
    grid = read_input()
    print(solve_part_one(grid))
    print(solve_part_two(grid))


if __name__ == "__main__":
    main()
