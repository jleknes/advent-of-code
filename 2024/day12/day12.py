import fileinput


def read_input() -> list[str]:
    return [line.strip() for line in fileinput.input()]


def neighbouring_points(y: int, x: int):
    moves = {
        "NORTH": (-1, 0),
        "EAST": (0, 1),
        "SOUTH": (1, 0),
        "WEST": (0, -1),
    }
    neighbours = []
    for direction in moves.keys():
        dy, dx = moves[direction]
        neighbours.append((y + dy, x + dx))
    return neighbours


def neighbours(y: int, x: int, gridsize):
    for ny, nx in neighbouring_points(y, x):
        if 0 <= ny < gridsize and 0 <= nx < gridsize:
            yield (ny, nx)


def calculate_border(region):
    fences = []
    for y, x in region:
        for neighbour in neighbouring_points(y, x):
            if neighbour not in region:
                fences.append(neighbour)
    return fences


def find_region(grid, start):
    region = set()
    region.add(start)
    queue = [start]
    region_id = grid[start[0]][start[1]]
    while queue:
        y, x = queue.pop(0)
        for neighbour in neighbours(y, x, len(grid)):
            if (
                neighbour not in region
                and grid[neighbour[0]][neighbour[1]] == region_id
            ):
                queue.append(neighbour)
                region.add(neighbour)
    return region


def border_cost(border):
    # for each remaining border point:
    # check if any other points are on a straight line
    # -+ +-
    # A| |A
    # A+-+A
    # AAAAA
    # if they are on a line, add

    # All squares with more than one point is a cross.
    # change data structure?
    remaining_points = list(border)
    (y, x) = remaining_points[0]
    remaining_points.remove((y,x))
    price=1
    #current_fence = [(y,x)]

    while remaining_points:
        # check all neighbours. If there is a neighbouring border,
        # check all neighbours in both directions on the same line. do so until
        # no more neighbours in those directions.
        # of we have to turn, start a new "collection"
        neighbours = neighbouring_points(y, x)
        for neighbour in neighbours:
            if neighbour in remaining_points:
                remaining_points.remove(neighbour)
                if neighbour[0]!=y:
                    #look for vertical points
                else:
                    #look for horizontal points
                break
        (y, x) = remaining_points[0]
        remaining_points.remove((y,x))
        price+=1

        # for neighbour in remaining_points:
        #    if neighbour in
    return price

def solve_part_one(grid):
    gridsize = len(grid)
    regions = []
    visited = set()
    for y in range(gridsize):
        for x in range(gridsize):
            if (y, x) not in visited:
                region = find_region(grid, (y, x))
                regions.append(region)
                visited.update(region)
    price = 0
    for region in regions:
        border = calculate_border(region)
        price += len(border) * len(region)
        # print region in a grid
        for y in range(-1, gridsize + 1):
            for x in range(-1, gridsize + 1):
                if (y, x) in region:
                    print("o", end="")
                elif (y, x) in border:
                    print(border.count((y, x)), end="")
                else:
                    print(".", end="")
            print()
        print()
    print(price)


def solve_part_two(grid):
    print(grid)


def main() -> None:
    grid = read_input()
    solve_part_one(grid)
    # solve_part_two(grid)


if __name__ == "__main__":
    main()
