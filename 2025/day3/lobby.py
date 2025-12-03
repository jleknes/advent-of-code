import fileinput


def read_input() -> list[str]:
    return [line.strip() for line in fileinput.input()]


def max_joltage(bank: str, length: int) -> int:
    joltage_digits = []
    position = 0
    while len(joltage_digits) < length:
        for digit in range(9, -1, -1):
            str_digit = str(digit)
            digit_pos = bank.find(str_digit, position)
            remaining_needed = length - len(joltage_digits) - 1
            if digit_pos != -1 and len(bank) - digit_pos - 1 >= remaining_needed:
                joltage_digits.append(str_digit)
                position = digit_pos + 1
                break
    return int("".join(joltage_digits))


def solve_part_one(battery_banks: list[str]) -> int:
    total = sum(max_joltage(bank, 2) for bank in battery_banks)
    print(total)


def solve_part_two(battery_banks: list[str]) -> int:
    total = sum(max_joltage(bank, 12) for bank in battery_banks)
    print(total)


def main() -> None:
    battery_banks = read_input()
    solve_part_one(battery_banks)
    solve_part_two(battery_banks)


if __name__ == "__main__":
    main()
