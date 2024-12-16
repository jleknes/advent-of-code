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
    print(remaining_points)
    # current_fence = [(y,x)]
    price = 0
    while remaining_points:
        (y, x) = remaining_points[0]
        remaining_points.remove((y, x))
        price += 1

        print("starting at ", y, x)
        # check all neighbours. If there is a neighbouring border,
        # check all neighbours in both directions on the same line. do so until
        # no more neighbours in those directions.
        neigbours = neighbouring_points(y, x)
        for neighbour in neigbours:
            if neighbour in remaining_points:
                print(neighbour)
                remaining_points.remove(neighbour)
                if neighbour[0] != y:
                    low_y = min(y, neighbour[0])
                    high_y = max(y, neighbour[0])
                    changed = True
                    while changed:
                        changed = False
                        if (low_y - 1, x) in remaining_points:
                            remaining_points.remove((low_y - 1, x))
                            low_y -= 1
                            changed = True
                        if (high_y + 1, x) in remaining_points:
                            remaining_points.remove((high_y + 1, x))
                            high_y += 1
                            changed = True
                else:
                    changed = True
                    low_x = min(x, neighbour[1])
                    high_x = max(x, neighbour[1])
                    while changed:
                        changed = False
                        if (y, low_x - 1) in remaining_points:
                            remaining_points.remove((y, low_x - 1))
                            low_x -= 1
                            changed = True
                        if (y, high_x + 1) in remaining_points:
                            remaining_points.remove((y, high_x + 1))
                            high_x += 1
                            changed = True
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
    print("part two")
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
        cost = border_cost(border)
        price += len(region) * cost
        region_id = grid[(list(region))[0][0]][(list(region))[0][1]]
        print(
            f"region id: {region_id}, region size: {len(region)} ",
            len(region),
            " number of sides: ",
            cost,
            " price: ",
            len(region) * cost,
        )
    print(price)


def main() -> None:
    grid = read_input()
    solve_part_one(grid)
    solve_part_two(grid)


if __name__ == "__main__":
    main()
