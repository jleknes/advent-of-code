import fileinput
from typing import List


def read_input() -> List[str]:
    ordering_rules = []
    updates = []
    for line in fileinput.input():
        line = line.strip()
        print(line)
        if "|" in line:
            ordering_rules.append((int(line.split("|")[0]),int(line.split("|")[1])))
        elif "," in line:
            update = [int(element) for element in line.split(",")]
            updates.append(update)
    return ordering_rules, updates    

def correct_update(ordering_rules, update):
    for rule in ordering_rules:
        for i in range(len(update)):
            for j in range(i, len(update)):
                if update[i]==rule[1] and update[j]==rule[0]:
                    return False
            
    return True

def custom_comparator(ordering_rules):
    def comparator(element1, element2) -> int:
        for rule in ordering_rules:
            if element1 == rule[1] and element2 == rule[0]:
                return -1
            elif element1 == rule[0] and element2 == rule[1]:
                return 1
        return 0
    return comparator

def order_update(ordering_rules, update):
    comparator = custom_comparator(ordering_rules)
    return sorted(update, key=lambda x: [comparator(x, y) for y in update])

def solve_part_two(ordering_rules, updates):
    total_sum = 0
    for update in updates:
        if not correct_update(ordering_rules, update):
            ordered_update = order_update(ordering_rules, update)
            # get middle element of update
            total_sum += ordered_update[int((len(ordered_update) - 1) / 2)]
    print(total_sum)
    return

def solve_part_one(ordering_rules, updates):
    total_sum=0
    for update in updates:
        if correct_update(ordering_rules, update):
            #get middle element of update
            total_sum+=update[int((len(update)-1)/2)]
    print(total_sum)
    return

def main():
    ordering_rules, updates = read_input()
    print(ordering_rules)
    print(updates)
    solve_part_one(ordering_rules, updates)
    solve_part_two(ordering_rules, updates)



if __name__ == "__main__":
    main()
