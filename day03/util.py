from typing import List


def parse_lines(filename: str) -> List[str]:
    result = []
    with open(filename, "r") as file:
        for line in file:
            result.append(line.strip())
    return result
