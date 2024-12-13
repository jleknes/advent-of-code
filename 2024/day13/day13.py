import fileinput
import re

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
    min_tokens=10000
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
        if tokens_spent!=10000:
            tokens+=tokens_spent
    print(tokens)

def solve_part_two(machines):
    tokens = 0
    for machine in machines:
        #tokens_spent = min_tokens(machine)
        #if tokens_spent!=10000:
        #    tokens+=tokens_spent
    print(tokens)


def main() -> None:
    machines = read_input()
    print(machines)
    solve_part_one(machines)
    solve_part_two(machines)


if __name__ == "__main__":
    main()