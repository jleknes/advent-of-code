import fileinput
from typing import List, Tuple
import itertools

def read_input() -> List[Tuple[int, List[int]]]:
    equations = []
    for line in fileinput.input():
        value, elements = line.strip().split(":")
        equations.append((int(value.strip()), list(map(int, elements.strip().split()))))
    return equations

def test_equation(test_result: int, elements: List[int], part: str) -> bool:
    operator_combinations = generate_operator_combinations(len(elements) - 1, part)
    for operator_list in operator_combinations:
        result = elements[0]
        for operator, element in zip(operator_list, elements[1:]):
            if operator == "*":
                result *= element
            elif operator == "+":
                result += element
            else:
                result = int(f"{result}{element}")
        if result == test_result:
            return True
    return False

def generate_operator_combinations(length: int, task: str) -> List[List[str]]:
    operators = ["+", "*"] if task == "PART_ONE" else ["+", "*", "||"]
    return list(itertools.product(operators, repeat=length))

def solve_part(equations: List[Tuple[int, List[int]]], part: str) -> int:
    total_calibration_result = sum(value for value, elements in equations if test_equation(value, elements, part))
    print(total_calibration_result)
    return total_calibration_result

def main() -> None:
    equations = read_input()
    solve_part(equations, "PART_ONE")
    solve_part(equations, "PART_TWO")

if __name__ == "__main__":
    main()
