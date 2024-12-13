import fileinput
import re
import math


def read_input():
    machines = []
    lines = []
    for line in fileinput.input():
        lines.append(line.strip())
        if len(lines) == 3:
            button_a = None
            button_b = None
            prize = None
            for l in lines:
                if l.startswith("Button A:"):
                    match_a = re.match(r"Button A: X([+-]\d+), Y([+-]\d+)", l)
                    if match_a:
                        button_a = {
                            "x": int(match_a.group(1)),
                            "y": int(match_a.group(2)),
                        }
                elif l.startswith("Button B:"):
                    match_b = re.match(r"Button B: X([+-]\d+), Y([+-]\d+)", l)
                    if match_b:
                        button_b = {
                            "x": int(match_b.group(1)),
                            "y": int(match_b.group(2)),
                        }
                elif l.startswith("Prize:"):
                    match_prize = re.match(r"Prize: X=(\d+), Y=(\d+)", l)
                    if match_prize:
                        prize = {
                            "x": int(match_prize.group(1)),
                            "y": int(match_prize.group(2)),
                        }
            if button_a and button_b and prize:
                machines.append(
                    {"button_a": button_a, "button_b": button_b, "prize": prize}
                )
            lines = []
    return machines

def solve_two(machine, prize):
    costs = []
    tokens = 10000000000000
    x_factors = get_factors(machine["prize"]["x"])
    y_factors = get_factors(machine["prize"]["y"])
    for a in range(math.sqrt(prize["x"])):
        for b in range(math.sqrt(prize["y"])):
            if (a*machine["a_button"]["x"]+b*machine["b_button"]["x"] in x_factors and 
            a*machine["a_button"]["y"]+b*machine["b_button"]["y"] in y_factors):
                costs+=
                
    # try to solve for all factors up until sqrt(x), sqrt(y)
    # if solution is found, multiply with prize.x/factor

def get_factors(n):
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    factors.sort()
    return factors


# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=10000000008400, Y=10000000005400

# a*94+b*22=10000000008400 
# a*34+b*67=10000000005400
#Button A: X+26, Y+66
#Button B: X+67, Y+21
#Prize: X=10000000012748, Y=10000000012176
# a*26+b*67=10000000008400 
# a*66+b*21=10000000005400




def solve_part_two(machines):
    print(machines)
    for machine in machines:
        print("x factors", get_factors(machine["prize"]["x"] + 10000000000000))
        print("y factors", get_factors(machine["prize"]["y"] + 10000000000000))
        solve_two(machine, {"x":machine["prize"]["x"] + 10000000000000, "y":machine["prize"]["y"] + 10000000000000})


def main() -> None:
    machines = read_input()
    solve_part_two(machines)
    # solve_part_two(grid)


if __name__ == "__main__":
    main()
