import fileinput


def read_input() -> str:
    return next(fileinput.input()).strip()


def solve_part_one(disk_map: str):
    print(disk_map)
    disk = []
    for i, c in enumerate(disk_map):
        for j in range(int(c)):
            if i % 2 == 0:
                disk.append(int(i / 2))
            else:
                disk.append(".")
    print(disk)
    i = 0
    j = len(disk) - 1
    while i < j:
        if disk[i] != ".":
            i += 1
        else:
            disk[i] = disk[j]
            del disk[j]
            j -= 1

    print(disk)
    checksum = 0
    for i in range(len(disk)):
        checksum += i * disk[i]
    print(checksum)


def main() -> None:
    disk_map = read_input()
    solve_part_one(disk_map)
    # solve_part_two(disk_map)


if __name__ == "__main__":
    main()
