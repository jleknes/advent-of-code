import fileinput
import functools

def read_input() -> tuple[list[str], list[str]]:
    lines = [line.strip() for line in fileinput.input()]
    return [word.strip() for word in lines[0].split(",")], lines[2:]
    return lines, []

@functools.lru_cache(maxsize=None)
def rec(patterns, design, i):
    if i == len(design):
        return True
    return any(design[i:].startswith(pattern) and rec(patterns, design, i + len(pattern)) for pattern in patterns)

def solve_part_one(patterns, designs):
    print(sum(1 if rec(tuple(patterns), design, 0) else 0 for design in designs))

@functools.lru_cache(maxsize=None)
def rec_two(patterns, design, i):
    if i == len(design):
        return 1
    return sum(rec_two(patterns, design, i + len(pattern)) for pattern in patterns if design[i:].startswith(pattern))

def solve_part_two(patterns, designs):
    print(sum(rec_two(tuple(patterns), design, 0) for design in designs))

def main() -> None:
    patterns, designs = read_input()
    solve_part_one(patterns, designs)
    solve_part_two(patterns, designs)

if __name__ == "__main__":
    main()