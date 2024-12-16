
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
    start = next((y, x) for y, row in enumerate(grid) for x, square in enumerate(row) if square == "S")
    end = next((y, x) for y, row in enumerate(grid) for x, square in enumerate(row) if square == "E")    
    q = deque()
    q.append((*start, "RIGHT",0))
    low_cost = {}
    while q:
        y, x, direction, cost = q.popleft()

        ny, nx = move(y,x,direction)
        if grid[ny][nx]!="#":
            key = f"{ny},{nx},{direction}"
            if not key in low_cost or low_cost[key]>cost+1:
                q.append((ny, nx,direction, cost+1))
                low_cost[key]=cost+1
        new_directions = (rotate (direction, True), rotate (direction, False))
        for direction in new_directions:
            key = f"{y},{x},{direction}"
            if not key in low_cost or low_cost[key]>cost+1:
                q.append((y, x,direction, cost+1000))
                low_cost[key]=cost+1000
    for direction in ["UP", "DOWN","LEFT", "RIGHT"]:
        key = f"{end[0]},{end[1]},{direction}"
        if key in low_cost:
            print (low_cost[key])

    


def main() -> None:
    grid = read_input()
    solve_part_one(copy.deepcopy(grid))
    #solve_part_two(copy.deepcopy(grid))

if __name__ == "__main__":
    main()