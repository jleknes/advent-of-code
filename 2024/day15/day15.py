import fileinput
import copy


def read_input() -> tuple[list[list[str]], str]:
    grid = []
    iterator = fileinput.input()
    for line in iterator:
        if line.strip() == "":
            break
        grid.append(list(line.strip()))

    moves = "".join(line.strip() for line in iterator)
    return grid, moves


def move(y: int, x: int, direction: str) -> tuple[int, int]:
    moves = {
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
    }
    dy, dx = moves[direction]
    return y + dy, x + dx


def solve_part_one(grid: list[list[str]], moves: str) -> None:
    pos = next(
        (y, x)
        for y, row in enumerate(grid)
        for x, square in enumerate(row)
        if square == "@"
    )
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

    gps_sum = sum(
        y * 100 + x
        for y, row in enumerate(grid)
        for x, square in enumerate(row)
        if square == "O"
    )
    for row in grid:
        print("".join(row))
    print(gps_sum)


def expand_grid(grid: list[list[str]]) -> list[list[str]]:
    char_map = {"#": ["#", "#"], ".": [".", "."], "@": ["@", "."], "O": ["[", "]"]}

    return [
        [char for square in row for char in char_map.get(square, [square, square])]
        for row in grid
    ]


def move_box(grid, y, x, instruction):
    if grid[y][x] == "]":
        x = x - 1
    next_y, next_x = move(y, x, instruction)
    if instruction in ["^", "v"]:
        grid[next_y][x] = grid[y][x]
        grid[next_y][x + 1] = grid[y][x + 1]
        grid[y][x] = "."
        grid[y][x + 1] = "."

    elif instruction == ">":
        grid[y][x + 2] = "]"
        grid[y][x + 1] = "["
        grid[y][x] = "."
    elif instruction == "<":
        grid[y][x - 1] = "["
        grid[y][x] = "]"
        grid[y][x + 1] = "."


def solve_part_two(grid: list[list[str]], moves: str) -> None:
    grid = expand_grid(grid)

    pos = next(
        (y, x)
        for y, row in enumerate(grid)
        for x, square in enumerate(row)
        if square == "@"
    )
    grid[pos[0]][pos[1]] = "."
    for row in grid:
        print("".join(row))

    for instruction in moves:
        ny, nx = move(*pos, instruction)
        if grid[ny][nx] == ".":
            pos = (ny, nx)
        elif grid[ny][nx] in ["[", "]"]:
            if instruction in [">", "<"]:
                # detect if box is blocked. If not blocked, move each box and robot

                box_y, box_x = ny, nx
                boxes_to_move = []
                while grid[box_y][box_x] in ["[", "]"]:
                    box_y, box_x = move(box_y, box_x, instruction)

                if grid[box_y][box_x] == ".":
                    boxes_to_move = (abs(box_x - nx) + 1) // 2
                    for i in range(boxes_to_move):
                        move_box(grid, box_y, box_x, instruction)
                        # important to start moving the box closest to the empty spot
                        """opposite_instructions = {"<": ">", ">": "<"}
                        opposite_instruction = opposite_instructions[instruction]
                        next_y, next_x = move(box_y, box_x, opposite_instruction)
                        grid[box_y][box_x] = grid[next_y][next_x]
                        box_y = next_y
                        box_x = next_x"""
                    for row in grid:
                        print("".join(row))

                    # grid[box_y][box_x] = "O"
                    # move all boxes one step in direction
                    pos = (ny, nx)

            else:
                # 1. check if the boxes can be moved
                # If not, don't do anything
                # 2. if they can be moved, move all boxes affected one square
                # have to consider such use cases, where it is possible to move up...
                #   #
                # [] []
                #  [][]
                #   []
                #   @
                #

                # check which x-es that are covered by box to be moved
                # there can at most be one more box that is to be moved for each
                box_x = nx
                box_y = ny
                if grid[ny][box_x] == "]":
                    box_x = nx - 1
                boxes_to_move = [(box_y, box_x)]

                # check both x-values of the boxes

                # for box in boxes_to_move:
                #    if move(box[0],box[1]-1, instruction)

                # Her må det loopes gjennom linjer oppover / nedover
                #

                continue
            # TODO: implement

            #    continue

    gps_sum = sum(
        y * 100 + x
        for y, row in enumerate(grid)
        for x, square in enumerate(row)
        if square == "["
    )
    for row in grid:
        print("".join(row))

    print(gps_sum)

    # follow same procedure as in part one, but handle larger boxes
    # moves left and right will be almost the same as part one


def main() -> None:
    grid, moves = read_input()
    solve_part_one(copy.deepcopy(grid), moves)
    solve_part_two(copy.deepcopy(grid), moves)


if __name__ == "__main__":
    main()
