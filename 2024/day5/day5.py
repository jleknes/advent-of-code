import fileinput
from typing import List, Tuple, Dict


def read_input() -> Tuple[Dict[int, List[int]], List[List[int]]]:
    ordering_rules = {}
    updates = []
    for line in fileinput.input():
        line = line.strip()
        if "|" in line:
            key, value = map(int, line.split("|"))
            ordering_rules.setdefault(key, []).append(value)
        elif "," in line:
            updates.append(list(map(int, line.split(","))))
    return ordering_rules, updates


def correct_update(ordering_rules: Dict[int, List[int]], update: List[int]) -> bool:
    return all(
        second_element not in ordering_rules
        or first_element not in ordering_rules[second_element]
        for i, first_element in enumerate(update)
        for second_element in update[i + 1 :]
    )


def custom_comparator(ordering_rules: Dict[int, List[int]]):
    def comparator(element1, element2) -> int:
        if element2 in ordering_rules and element1 in ordering_rules[element2]:
            return -1
        elif element1 in ordering_rules and element2 in ordering_rules[element1]:
            return 1
        else:
            return 0

    return comparator


def order_update(ordering_rules: Dict[int, List[int]], update: List[int]) -> List[int]:
    comparator = custom_comparator(ordering_rules)
    return sorted(update, key=lambda x: [comparator(x, y) for y in update])


def get_middle_element(lst: List[int]) -> int:
    return lst[len(lst) // 2]


def solve_part_two(ordering_rules: Dict[int, List[int]], updates: List[List[int]]):
    print(
        sum(
            get_middle_element(order_update(ordering_rules, update))
            for update in updates
            if not correct_update(ordering_rules, update)
        )
    )


def solve_part_one(ordering_rules: Dict[int, List[int]], updates: List[List[int]]):
    print(
        total_sum=sum(
            get_middle_element(update)
            for update in updates
            if correct_update(ordering_rules, update)
        )
    )


def main():
    ordering_rules, updates = read_input()
    solve_part_one(ordering_rules, updates)
    solve_part_two(ordering_rules, updates)


if __name__ == "__main__":
    main()
