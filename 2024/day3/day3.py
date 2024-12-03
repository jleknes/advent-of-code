import fileinput
import re
from typing import List


def read_input() -> List[str]:
    return ''.join(fileinput.input())

def solve_part_two(memory:str):
    total_sum=0
    enabled = True
    pos=0
    while pos<len(memory) and pos!=-1:
        if enabled:
            substr_end = memory.find("don't()", pos)
            if substr_end==-1:
                substr_end=len(memory)
            total_sum+=process_line(memory[pos:substr_end])
            pos=substr_end
            enabled = False
        else:
            pos=memory.find("do()", pos)
            enabled = True
    print(total_sum)


def process_line(line: str) -> int:
    mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(mul_pattern, line)
    return sum(int(num1) * int(num2) for match in matches for num1, num2 in [match[4:-1].split(",")])

def solve_part_one(memory: str):
    print(process_line(memory))

def main():
    memory = read_input()
    solve_part_one(memory)
    solve_part_two(memory)

if __name__ == "__main__":
    main()