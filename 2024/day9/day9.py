import fileinput

def read_input() -> str:
    return next(fileinput.input()).strip()

def get_disk(disk_map:str):
    return [
        int(i / 2) if i % 2 == 0 else "."
        for i, c in enumerate(disk_map)
        for _ in range(int(c))
    ]

def get_checksum(disk):
    return sum(i * val for i, val in enumerate(disk) if val != ".")

def solve_part_one(disk_map: str):
    disk = get_disk(disk_map)

    i, j = 0, len(disk) - 1
    while i < j:
        if disk[i] != ".":
            i += 1
        else:
            disk[i], disk[j] = disk[j], disk[i]
            j -= 1
    print(get_checksum(disk))

def solve_part_two(disk_map: str):
    disk = get_disk(disk_map)
    highest_id = max(val for val in disk if val != ".")

    for i in range(highest_id, -1, -1):
        first_pos = disk.index(i)
        last_pos = len(disk) - 1 - disk[::-1].index(i)
        min_length = last_pos - first_pos + 1

        start_pos, count = -1, 0
        for k in range(first_pos):
            if disk[k] == ".":
                if count == 0:
                    start_pos = k
                count += 1
                if count == min_length:
                    break
            else:
                count = 0

        if count == min_length:
            for k in range(start_pos, start_pos + min_length):
                disk[k], disk[last_pos - (k - start_pos)] = i, "."

    print(get_checksum(disk))

def main() -> None:
    disk_map = read_input()
    solve_part_one(disk_map)
    solve_part_two(disk_map)

if __name__ == "__main__":
    main()
