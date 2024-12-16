import fileinput
from typing import List, Tuple
import copy

def read_input() -> Tuple[List[List[str]], str]:
    grid = []
    iterator = fileinput.input()
    for line in iterator:
        if line.strip() == "":
            break
        grid.append(list(line.strip()))

    moves = "".join(line.strip() for line in iterator)
    return grid, moves

def move(y: int, x: int, direction: str) -> Tuple[int, int]:
    moves = {
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
    }
    dy, dx = moves[direction]
    return y + dy, x + dx

def solve_part_one(grid: List[List[str]], moves: str) -> None:
    pos = next((y, x) for y, row in enumerate(grid) for x, square in enumerate(row) if square == "@")
    grid[pos[0]][pos[1]] = "."

    for instruction in moves:
        ny, nx = move(*pos, instruction)
        if grid[ny][nx] == ".":
            pos = (ny, nx)
        elif grid[ny][nx] == "O":
            box_y, box_x = ny, nx
            while grid[box_y][box_x] == "O":
                box_y, box_x = move(box_y, box_x, instruction)
            if grid[box_y][box_x] == ".":
                grid[box_y][box_x] = "O"
                grid[ny][nx] = "."
                pos = (ny, nx)

    gps_sum = sum(y * 100 + x for y, row in enumerate(grid) for x, square in enumerate(row) if square == "O")
    for row in grid:
        print("".join(row))
    print(gps_sum)

def solve_part_two(grid: List[List[str]], moves: str) -> None:
    # change map 
    new_grid = []
    for y, row in enumerate(grid):
        new_grid.append([])
        for x, square in enumerate(row):
            if square in ["#", "."]:
                new_grid[y].append(square)
                new_grid[y].append(square)
            elif square=="@":
                new_grid[y].append(square)
                new_grid[y].append(".")
            elif square=="O":
                new_grid[y].append("[")
                new_grid[y].append("]")
    grid = new_grid
    for instruction in moves:
        ny, nx = move(*pos, instruction)
        if grid[ny][nx] == ".":
            pos = (ny, nx)
        elif grid[ny][nx] in ["[","]"]:
            box_y, box_x = ny, nx
            if instruction in [">","<"]
                while grid[box_y][box_x] in ["[","]"]:
                    box_y, box_x = move(box_y, box_x, instruction)
                    if grid[box_y][box_x] == ".":
                        #grid[box_y][box_x] = "O"
                        # move all boxes one step in direction
                        for i in range(abs(box_x-pos[1])):
                            grid[ny][]=move(box_y, box_x, instruction)
                            grid[]
                        grid[ny][nx] = "."
                        pos = (ny, nx)
            else:
                # TODO: implement
                
                continue


    for row in new_grid:
        print("".join(row))



    # follow same procedure as in part one, but handle larger boxes
    # moves left and right will be almost the same as part one


def main() -> None:
    grid, moves = read_input()
    solve_part_one(copy.deepcopy(grid), moves)
    solve_part_two(copy.deepcopy(grid), moves)

if __name__ == "__main__":
    main()