import fileinput
from itertools import combinations
from collections import deque


def read_input() -> dict[str, list[str]]:
    connections = {}
    for line in fileinput.input():
        connection = line.strip().split("-")
        connections.setdefault(connection[0], []).append(connection[1])
        connections.setdefault(connection[1], []).append(connection[0])
    return connections


def solve_part_one(connections: dict[str, list[str]]) -> None:
    three_computer_sets = {
        frozenset((key, *pair))
        for key in connections
        for pair in combinations(connections[key], 2)
        if pair[1] in connections[pair[0]]
    }

    t_lan_parties = sum(
        1
        for triad in three_computer_sets
        if any(computer.startswith("t") for computer in triad)
    )

    print(t_lan_parties)


def solve_part_two(connections: dict[str, list[str]]) -> None:
    largest_party: set[str] = set()
    for key in connections:
        party: set[str] = {key}
        unchecked_connections = deque(connections[key])
        while unchecked_connections:
            connection = unchecked_connections.popleft()
            if all(connection in connections[computer] for computer in party):
                party.add(connection)
        if len(party) > len(largest_party):
            largest_party = party
    print(", ".join(sorted(largest_party)))


def main() -> None:
    connections = read_input()
    solve_part_one(connections)
    solve_part_two(connections)


if __name__ == "__main__":
    main()
