import fileinput


def read_input() -> list[str]:
    return [line.strip() for line in fileinput.input()]


def solve_part_one(rotations: list[str]) -> int:
    position = 50
    zeros = 0
    for rotation in rotations:
        direction, steps = rotation[0], int(rotation[1:])
        position += steps if direction == "R" else -steps
        position %= 100
        zeros += position == 0
    print(zeros)
    return zeros


def solve_part_two(rotations: list[str]) -> int:
    position = 50
    zeros = 0
    for rotation in rotations:
        direction, steps = rotation[0], int(rotation[1:])
        if direction == "R":
            position += steps
            zeros += position // 100
        else:  # direction == "L"
            new_position = position - steps
            zeros += abs(new_position) // 100 + (0 < position <= steps)
            position = new_position
        position %= 100
    print(zeros)
    return zeros


def main() -> None:
    rotations = read_input()
    solve_part_one(rotations)
    solve_part_two(rotations)


if __name__ == "__main__":
    main()
