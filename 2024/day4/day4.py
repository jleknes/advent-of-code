import fileinput
from typing import List


def read_input() -> List[str]:
    return [line.strip() for line in (fileinput.input())]


def check(word_search: List[str]) -> bool:
    diagonals = (
        word_search[0][0] + word_search[1][1] + word_search[2][2],
        word_search[0][2] + word_search[1][1] + word_search[2][0],
    )
    return (diagonals[0] in {"MAS", "SAM"}) and (diagonals[1] in {"MAS", "SAM"})


def reverse(word_search: List[str]) -> List[str]:
    return [line[::-1] for line in word_search]


def transpose(word_search: List[str]) -> List[str]:
    return [''.join(row) for row in zip(*word_search)]


def count_xmas(word_search: List[str]):
    sum=0
    for line in word_search:
        sum+=line.count("XMAS")
    return sum


def get_diagonals(word_search: List[str]) -> List[str]:
    n = len(word_search)
    m = len(word_search[0]) if n > 0 else 0
    diagonals = []

    # Get main diagonals
    for d in range(n + m - 1):
        diag1 = []
        diag2 = []
        for i in range(max(0, d - m + 1), min(n, d + 1)):
            diag1.append(word_search[i][d - i])
            diag2.append(word_search[i][m - 1 - (d - i)])
        diagonals.append(''.join(diag1))
        diagonals.append(''.join(diag2))
    return diagonals


def solve_part_one(word_search: List[str]):
    total_sum=0
    total_sum+=count_xmas(word_search)
    total_sum+=count_xmas(reverse(word_search))
    total_sum+=count_xmas(transpose(word_search))
    total_sum+=count_xmas(reverse(transpose(word_search)))
    total_sum+=count_xmas(get_diagonals(word_search))
    total_sum+=count_xmas(reverse(get_diagonals(word_search)))
    print(total_sum)


def solve_part_two(word_search: List[str]):
    total_sum = sum(
        1
        for i in range(len(word_search) - 2)
        for j in range(len(word_search[i]) - 2)
        if check([row[j : j + 3] for row in word_search[i : i + 3]])
    )
    print(total_sum)


def main():
    word_search = read_input()
    solve_part_one(word_search)
    solve_part_two(word_search)


if __name__ == "__main__":
    main()
