import fileinput
import math
import time

def read_input() -> list[str]:
    robots = []
    for line in fileinput.input():
        parts = line.strip().split()

        pos = [int(x) for x in parts[0][2:].split(",")]
        velocity = [int(x) for x in parts[1][2:].split(",")]
        robots.append((pos, velocity))
    return robots

def solve_part_two(robots, gridsize):
    for second in range(10000):
        end_states=[]
        for robot in robots:
            x,y = (robot[0][0]+robot[1][0]*second)%gridsize[0], (robot[0][1]+robot[1][1]*second)%gridsize[1]
            end_states.append((x,y))        
        if len(end_states) == len(set(end_states)):
            print (second)
            for y in range (gridsize[1]):
                for x in range (gridsize[0]):
                    if (x,y) in end_states:
                        print("1", end="")
                    else:
                        print(".", end="")
                print()
            print()


def solve_part_one(robots, gridsize):
    quadrants = [0] * 4
    mid_x, mid_y = (gridsize[0] - 1) / 2, (gridsize[1] - 1) / 2

    for robot in robots:
        x = (robot[0][0]+robot[1][0]*100)%gridsize[0]
        y = (robot[0][1]+robot[1][1]*100)%gridsize[1]
        if x == mid_x or y == mid_y:
            continue # Skip to the next robot
        
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