import fileinput
from typing import List


def read_input() -> List[str]:
    return [line.strip() for line in (fileinput.input())]

def check(word_search: List[str]) -> bool:
    diagonals = (
        word_search[0][0] + word_search[1][1] + word_search[2][2],
        word_search[0][2] + word_search[1][1] + word_search[2][0]
    )

    return (diagonals[0] in {"MAS", "SAM"}) and (diagonals[1] in {"MAS", "SAM"})


def solve_part_two(word_search: List[str]):
    total_sum = sum(
        1
        for i in range(len(word_search) - 2)
        for j in range(len(word_search[i]) - 2)
        if check([row[j:j+3] for row in word_search[i:i+3]])
    )
    print(total_sum)
    
def main():
    word_search = read_input()
    
    #solve_part_one(word_search)
    solve_part_two(word_search)

if __name__ == "__main__":
    main()