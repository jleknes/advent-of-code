
import fileinput
from itertools import groupby


def read_input() -> tuple[list[tuple[int, int]], list[int]]:
    lines = [line.strip() for line in fileinput.input()]
    groups = [list(group) for key, group in groupby(lines, key=bool) if key]
    
    ranges = sorted([tuple(map(int, line.split('-'))) for line in groups[0]])
    ingredients = [int(line) for line in groups[1]]
    
    return ranges, ingredients



def solve_part_one(fresh_ranges: list[tuple[int, int]], ingredients: list[int]) -> None:
    fresh_count = sum(
        any(r_start <= ingredient <= r_end for r_start, r_end in fresh_ranges)
        for ingredient in ingredients
    )
    print(fresh_count)


def solve_part_two(fresh_ranges: list[tuple[int, int]]) -> None:
    merged = [fresh_ranges[0]]
    
    for current_start, current_end in fresh_ranges[1:]:
        last_start, last_end = merged[-1]
        
        if current_start <= last_end:
            # Overlap: merge by updating the end of the last interval
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            # No overlap: append the current interval
            merged.append((current_start, current_end))
    
    total = sum(end - start + 1 for start, end in merged)
    print(total)


def main() -> None:
    fresh_ranges, ingredients = read_input()
    solve_part_one(fresh_ranges, ingredients)
    solve_part_two(fresh_ranges)


if __name__ == "__main__":
    main()
