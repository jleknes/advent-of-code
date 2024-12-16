import fileinput
import re
import math

def read_input() -> list[str]:
    # I want a list of cases. each case are three lines, then follow a newline
    # parse three lines including this text:
    # Button A: X+94, Y+34
    #Button B: X+22, Y+67
    #Prize: X=8400, Y=5400
    machines = []
    lines = [line.strip() for line in fileinput.input() if line.strip()]

    for i in range(0, len(lines), 3):
        button_a = re.findall(r'X\+(\d+), Y\+(\d+)', lines[i])
        button_b = re.findall(r'X\+(\d+), Y\+(\d+)', lines[i+1])
        prize = re.findall(r'X=(\d+), Y=(\d+)', lines[i+2])

        if button_a and button_b and prize:
            machines.append({
                "button_a": {"x": int(button_a[0][0]), "y": int(button_a[0][1])},
                "button_b": {"x": int(button_b[0][0]), "y": int(button_b[0][1])},
                "prize": {"x": int(prize[0][0]), "y": int(prize[0][1])}

            })

    return machines    
    

def min_tokens(machine):
    print(machine)
    min_tokens=1000000
    for a in range(0,101):
        for b in range(0,101):
            if (machine["button_a"]["x"]*a+machine["button_b"]["x"]*b==machine["prize"]["x"] and
            machine["button_a"]["y"]*a+machine["button_b"]["y"]*b==machine["prize"]["y"] and a+b<min_tokens):
                min_tokens=3*a+b
    return min_tokens


def solve_part_one(machines):
    tokens = 0
    for machine in machines:
        tokens_spent = min_tokens(machine)
        if tokens_spent!=1000000:
            tokens+=tokens_spent
    print(tokens)

"""
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=10000000008400, Y=10000000005400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=10000000012748, Y=10000000012176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=10000000007870, Y=10000000006450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=10000000018641, Y=10000000010279
"""

def solve_two(machine, prize):
    # finn alle faktorer i x og y.
    # sjekk par av faktorer. det må finnes en x-faktor og y-faktor som tilfredsstiller x/xfaktor =y/yfaktor
    

    costs = []
    tokens = 10000000000000
    x_factors = get_factors(machine["prize"]["x"])
    y_factors = get_factors(machine["prize"]["y"])
    for x_factor in x_factors:
        for y_factor in y_factors:
            if machine["prize"]["x"]//x_factor==machine["prize"]["y"]//y_factor:
                print (x_factor, y_factor)
                machine_2 = dict.copy(machine)
                machine_2["prize"]["x"]=x_factor
                machine_2["prize"]["y"]=y_factor
                multiplier = machine["prize"]["x"]//x_factor
                print (min_tokens(machine_2)*multiplier)
                cost = min_tokens(machine_2)
                if cost!=1000000:
                    costs.append(min_tokens(machine_2)*multiplier)
    if (len(costs)>1):
        print(min(costs))
    else:
        print(-1)
    #for a in range(int(max(math.sqrt(prize["x"]), math.sqrt(prize["y"])))):
        #for b in range(int(max(math.sqrt(prize["x"]), math.sqrt(prize["y"])))):
            #c=a*b
            #if (a*machine["a_button"]["x"]+b*machine["b_button"]["x"] in x_factors and 
            #a*machine["a_button"]["y"]+b*machine["b_button"]["y"] in y_factors):
            #    costs+=
                
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
    for i, machine in enumerate(machines):
        print(f"machine nr {i+1}")
        print("x factors", get_factors(machine["prize"]["x"] + 10000000000000))
        print("y factors", get_factors(machine["prize"]["y"] + 10000000000000))
        solve_two(machine, {"x":machine["prize"]["x"] + 10000000000000, "y":machine["prize"]["y"] + 10000000000000})


def main() -> None:
    machines = read_input()
    print(machines)
    solve_part_one(machines)
    solve_part_two(machines)


if __name__ == "__main__":
    main()