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

def solve_part_two(disk_map: str):
    disk = []
    highest_id=0
    for i, c in enumerate(disk_map):
        for j in range(int(c)):
            if i % 2 == 0:
                disk.append(int(i / 2))
                highest_id=int(i/2)
            else:
                disk.append(".")
    for i in range(highest_id, -1, -1):
        first_pos = disk.index(i)
        last_pos = len(disk) - 1 - disk[::-1].index(i)
        min_length = last_pos-first_pos+1
        start_pos = -1
        count = 0
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
                disk[k] = i
                disk[last_pos-(k-start_pos)]="."

    checksum = 0
    for i in range(len(disk)):
        if disk[i] != ".":
            checksum += i * disk[i]
    print(checksum)



def main() -> None:
    disk_map = read_input()
    solve_part_one(disk_map)
    solve_part_two(disk_map)


if __name__ == "__main__":
    main()
