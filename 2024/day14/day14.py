import fileinput
import math

def read_input() -> list[str]:
    robots = []
    for line in fileinput.input():
        parts = line.strip().split()
        robot = {}
        robot["x"], robot["y"]= [int(x) for x in parts[0][2:].split(",")]
        robot["vx"], robot["vy"] = [int(x) for x in parts[1][2:].split(",")]
        robots.append(robot)
    return robots

def solve_part_two(robots, gridsize):
    for second in range(10000):
        positions=[]
        for robot in robots:
            x = (robot["x"]+robot["vx"]*second)%gridsize[0]
            y = (robot["y"]+robot["vy"]*second)%gridsize[1]
            positions.append((x,y))        
        if len(positions) == len(set(positions)):
            print (second)
            for y in range (gridsize[1]):
                for x in range (gridsize[0]):
                    if (x,y) in positions:
                        print("1", end="")
                    else:
                        print(".", end="")
                print()
            print()


def solve_part_one(robots, gridsize):
    quadrants = [0] * 4
    mid_x, mid_y = (gridsize[0] - 1) / 2, (gridsize[1] - 1) / 2
    second = 100

    for robot in robots:
        x = (robot["x"]+robot["vx"]*second)%gridsize[0]
        y = (robot["y"]+robot["vy"]*second)%gridsize[1]
        if x == mid_x or y == mid_y:
            continue
        quadrant_index = (int(x > mid_x) + 2 * int(y > mid_y))
        quadrants[quadrant_index] += 1        
    print(math.prod(quadrants))

def main() -> None:
    robots = read_input()
    gridsize = (101,103)
    #gridsize = (11,7)
    solve_part_one(robots, gridsize)
    solve_part_two(robots, gridsize)


if __name__ == "__main__":
    main()