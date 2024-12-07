import fileinput
from typing import List, Tuple
import itertools

def read_input() -> List[Tuple[int, List[int]]]:
    lines = [line.strip() for line in fileinput.input()]
    equations = []
    for line in lines:
        value=int(line.split(":")[0].strip())
        elements = list(map(int, line.split(":")[1].strip().split(" ")))
        equations.append((value, elements))
    return equations

def test_equation(test_result, elements, part:str):
    operator_combinations = generate_operator_combinations(len(elements) - 1, part)
    # Process each combination of operators with the elements
    for operator_list in operator_combinations:
        sum=elements[0]
        for operator, element in zip(operator_list, elements[1:]):
            if operator=="*":
                sum*=element
            elif operator=="+":
                sum+=element
            else:
                sum=int(str(sum)+str(element))
        
        if sum==test_result:
            print(test_result, elements, operator_list)
            return True
    return False

def generate_operator_combinations(length: int, task:str) -> List[List[str]]:
    if task =="PART_ONE":
        operators = ["+", "*"]
    else: 
        operators = ["+", "*", "||"]
    return list(itertools.product(operators, repeat=length))


def solve_part_one(equations):
    total_calibration_result = 0
    for equation in equations:
        value, elements = equation
        if test_equation(value,elements,"PART_ONE"):
            total_calibration_result+=value
            # Implement the logic to test the equation with the given operators
        #    pass
    print(total_calibration_result)
    return

def solve_part_two(equations):
    total_calibration_result = 0
    for equation in equations:
        value, elements = equation
        if test_equation(value,elements,"PART_TWO"):
            total_calibration_result+=value
            # Implement the logic to test the equation with the given operators
        #    pass
    print(total_calibration_result)
    return


def main() -> None:
    equations = read_input()
    print(equations)
    solve_part_one(equations)
    solve_part_two(equations)
   


if __name__ == "__main__":
    main()
