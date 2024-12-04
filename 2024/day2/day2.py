import fileinput
from typing import List

def read_input() -> List[List[int]]:
    return [[int(token) for token in line.split()] for line in fileinput.input()]

def is_safe(sequence: List[int]) -> bool:
    return (all(0 < sequence[i] - sequence[i-1] < 4 for i in range(1, len(sequence))) or 
            all(0 < sequence[i-1] - sequence[i] < 4 for i in range(1, len(sequence))))

def solve_part_two(lines: List[List[int]]):
    safe_reports = sum(
        1 for line in lines
        if any(is_safe(line[:i] + line[i+1:]) for i in range(len(line)))
    )
    print(safe_reports)

def solve_part_one(lines: List[List[int]]):
    safe_reports = sum(1 for line in lines if is_safe(line))
    print(safe_reports)

def main():
    lines = read_input()
    solve_part_one(lines)
    solve_part_two(lines)

if __name__ == "__main__":
    main()