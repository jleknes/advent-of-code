import fileinput
from typing import List
import functools


def read_input() -> List[int]:
    return [int(x) for x in next(fileinput.input()).strip().split()]


@functools.lru_cache(maxsize=None)
def num_stones(stone_id: int, blinks_left: int) -> int:
    if blinks_left == 0:
        return 1
    elif stone_id == 0:
        return num_stones(1, blinks_left - 1)
    if len(str(stone_id)) % 2 == 0:
        middle = len(str(stone_id)) // 2
        left_half = int(str(stone_id)[:middle])
        right_half = int(str(stone_id)[middle:])
        return num_stones(left_half, blinks_left - 1) + num_stones(
            right_half, blinks_left - 1
        )
    else:
        return num_stones(stone_id * 2024, blinks_left - 1)


def main() -> None:
    stones = read_input()
    print(sum(num_stones(stone, 25) for stone in stones))
    print(sum(num_stones(stone, 75) for stone in stones))


if __name__ == "__main__":
    main()
