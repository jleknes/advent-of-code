import fileinput
from collections import deque

def read_input() -> list[list[str]]:
    return [tuple(int(x) for x in line.strip().split(",")) for line in fileinput.input()]



def move(y: int, x: int, direction: str) -> tuple[int, int]:
    moves = {
        "NORTH": (-1, 0),
        "EAST": (0, 1),
        "SOUTH": (1, 0),
        "WEST": (0, -1),
    }
    dy, dx = moves[direction]
    return y + dy, x + dx

def distance(coordinates, gridsize):
    start = (0,0)
    end = (gridsize-1,gridsize-1)
    min_dist = {}
    q = deque([start])
    min_dist[start]=0
    while q:
        y,x = q.popleft()
        #print(y,x)
        #print(min_dist)
        dist = min_dist[(y,x)]
        for direction in ["NORTH", "EAST", "SOUTH", "WEST"]:
            ny, nx = move(y, x, direction)
            #print(f"testing {ny},{nx}")
            if 0 <= ny < gridsize and 0 <= nx < gridsize and (nx,ny) not in coordinates:
                if (ny,nx) not in min_dist or min_dist[(ny,nx)]>dist+1:
                     min_dist[(ny,nx)]=dist+1
                     q.append((ny,nx))
    if end not in min_dist:
        return -1
    else:
        return min_dist[end]


def solve_part_one(coordinates, gridsize):
    print(distance(coordinates, gridsize))
    for y in range(gridsize):
        for x in range(gridsize):
            if (x,y) in coordinates:
                print("#", end="")
            else:
                print(".", end="")
        print()

def solve_part_two(coordinates, gridsize, min_bytes):
    upper = len(coordinates)
    lower = min_bytes
    while upper>lower+1:
        mid = lower+(upper-lower)//2
        if distance(coordinates[:mid], gridsize)==-1:
            upper=mid
        else:
            lower=mid
    print(lower)
    print(coordinates[lower])

def main() -> None:
    #gridsize=7
    #num_bytes=12
    gridsize = 71
    num_bytes = 1024
    coordinates = read_input()
    solve_part_one(coordinates[:num_bytes], gridsize)
    solve_part_two(coordinates, gridsize, num_bytes)

if __name__ == "__main__":
    main()