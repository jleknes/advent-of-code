import fileinput

def read_input() -> list[str]:
    return [line.strip() for line in fileinput.input()]

def neighbours(y: int, x: int, gridsize) -> tuple[int, int]:
    moves = {
        "NORTH": (-1, 0),
        "EAST": (0, 1),
        "SOUTH": (1, 0),
        "WEST": (0, -1),
    }
    neighbours = []
    for direction in moves.keys():
        dy, dx = moves[direction]
        if 0 <= (y + dy) <= gridsize and 0 <= (x + dx) <= gridsize:
            neighbours.append((y + dy, x + dx))
    return neighbours


def calculate_border(region, gridsize):
    # for each point, check if there are neighbours in all directions
    # if no neighbour, that is a fence.
    # dont look at fences as points, but as a point and a direction
    fences=set()
    for (y,x) in region:
        for neighbours in neighbours(y,x,gridsize):
            if neighbour not in region:
                fences.add(neighbour)

def solve_part_one(grid):
    regions = []
    for i, c in enumerate(grid):
        for j, c in enumerate(grid[i]):
            print(j,c)
    print(grid)

def solve_part_two(grid):
    print(grid)


def main() -> None:
    grid = read_input()
    solve_part_one(grid)
    #solve_part_two(grid)


if __name__ == "__main__":
    main()
