import fileinput


def read_input() -> list[tuple[int, int]]:
    line = next(fileinput.input()).strip()
    ranges = line.split(",")
    return [tuple(map(int, r.split("-"))) for r in ranges]


def solve_part_one(product_ids: list[tuple[int, int]]) -> int:
    total = sum(
        i
        for id1, id2 in product_ids
        for i in range(id1, id2 + 1)
        if (s := str(i)) and s[: len(s) // 2] == s[len(s) // 2 :]
    )
    print(total)


def invalid_id(id_num: int) -> bool:
    s = str(id_num)
    return any(
        len(s) % chunk_size == 0
        and all(
            s[j * chunk_size : (j + 1) * chunk_size]
            == s[(j + 1) * chunk_size : (j + 2) * chunk_size]
            for j in range(len(s) // chunk_size - 1)
        )
        for chunk_size in range(1, len(s) // 2 + 1)
    )


def solve_part_two(product_ids: list[tuple[int, int]]) -> int:
    total = sum(
        i for id1, id2 in product_ids for i in range(id1, id2 + 1) if invalid_id(i)
    )
    print(total)


def main() -> None:
    product_ids = read_input()
    solve_part_one(product_ids)
    solve_part_two(product_ids)


if __name__ == "__main__":
    main()
