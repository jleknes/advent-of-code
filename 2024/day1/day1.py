import fileinput
from typing import List, Tuple

def read_input() -> Tuple[List[int], List[int]]:
    lines = [line.split() for line in fileinput.input()]
    left = [int(parts[0]) for parts in lines]
    right = [int(parts[1]) for parts in lines]
    return left, right

def solve_part_one(left: List[int], right: List[int]):
    sorted_left = sorted(left)
    sorted_right = sorted(right)
    similarity_score = sum(abs(l - r) for l, r in zip(sorted_left, sorted_right))
    print("part one:", similarity_score)

def solve_part_two(left: List[int], right: List[int]):
    similarity_score = sum(l * right.count(l) for l in left)
    print("part two:", similarity_score)

def main():
    left, right = read_input()
    solve_part_one(left, right)
    solve_part_two(left, right)

if __name__ == "__main__":
    main()